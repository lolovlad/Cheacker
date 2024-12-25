from typing import List
import subprocess
import shlex
from pathlib import Path


class Compiler:
    def __init__(self, file_compiler: str):
        self.__file_compiler: Path = Path(Path.cwd(), file_compiler)
        self.__commands_preprocess: List[str] = []
        self.__start_file_program: str = ""
        self.__command: str = ""

    @property
    def command(self):
        return self.__command

    def __split_commands(self):
        with open(self.__file_compiler, "r") as file:
            lines = file.readlines()
            self.__commands_preprocess = lines[:-1]
            self.__start_file_program = lines[-1]

    def __file_program(self, paths: dict) -> str:
        return self.__start_file_program.format(**paths)

    def __preprocess_start_file(self, paths: dict) -> bool:
        for command in self.__commands_preprocess:
            command = command.format(**paths)
            proces = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            outs, errs = proces.communicate()
            outs = str(outs.decode())
            errs = str(errs.decode())
            if len(errs) > 0:
                return True
        return False

    def run_preprocess(self, paths: dict) -> bool:
        self.__split_commands()
        self.__command = self.__file_program(paths)
        error = self.__preprocess_start_file(paths)
        return error

