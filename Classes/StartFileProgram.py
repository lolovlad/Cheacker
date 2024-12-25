import subprocess
import time
from pathlib import Path
from subprocess import Popen, TimeoutExpired
import asyncio
import shlex

from .InputData import InputData
from .OutputData import OutputData
from .Compiler import Compiler
from .VirtualEnvironment import VirtualEnvironment
from Models.ReportTesting import ReportTesting
from Models.ReportTesting import Rating


class StartFileProgram:
    def __init__(self, virtual: VirtualEnvironment, input_stream: InputData,
                 output_stream: OutputData, type_compilation: Compiler):
        self.__venv = virtual
        self.__input_stream = input_stream
        self.__output_stream = output_stream
        self.__process: Popen = None
        self.__compiler = type_compilation

    def __create_sub_proces(self):
        self.__process = Popen(shlex.split(self.__compiler.command),
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               cwd=self.__venv.path_virtual_environment)

    def start_process(self, input_in_process: Path, time_out: int) -> ReportTesting:
        input_data = self.__input_stream.start_stream(input_in_process)
        self.__create_sub_proces()
        report_testing = ReportTesting()
        try:
            outs = self.__process.communicate(input=input_data, timeout=time_out)

            report_testing.out = self.__output_stream.read_output(str(outs[0].decode('utf-8')))

            if len(outs[1].decode().split("\n")) > 2:
                raise Exception

            mt_out = str(outs[1].decode()).replace("\n", "").split()

            memory, time_work = map(float, mt_out)

            report_testing.memory = round((int(memory) / 2**10), 3)
            report_testing.time = int(time_work * 1000)
            report_testing.errors = Rating.OK
            self.__process.kill()
            return report_testing
        except Exception:
            self.__process.kill()
            report_testing.errors = Rating.COMPILATION_ERROR
            return report_testing
        except TimeoutExpired:
            self.__process.kill()
            outs, errs = self.__process.communicate()
            report_testing.errors = Rating.TIME_LIMIT_EXCEEDED
            return report_testing
