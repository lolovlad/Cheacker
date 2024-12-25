from pathlib import Path
from os import environ, getcwd, chdir, name
from uuid import uuid4
from os import mkdir
from pathlib import Path
from shutil import rmtree

from Repositories.IAnswerRepository import IAnswerRepository


class VirtualEnvironment:
    def __init__(self):
        self.__name_folder: str = str(uuid4())
        self.__path_virtual_environment: str = f"virtual_environment/{self.__name_folder}"
        self.__work_folder = getcwd()
        self.__path_file_answer = None

    @property
    def path_file_answer(self):
        return str(self.__path_file_answer)

    @property
    def path_virtual_environment(self):
        return str(self.__path_virtual_environment)

    @property
    def name_folder(self):
        if self.__name_folder is None:
            raise EOFError("not creating virtual folder")
        return self.__name_folder

    def __create_folder(self, path_folder: str) -> Path:
        path_create_folder = Path(self.__work_folder, path_folder)
        try:
            mkdir(path_create_folder)
        except FileNotFoundError:
            mkdir(Path(self.__work_folder, "virtual_environment"))
            mkdir(path_create_folder)
        return path_create_folder

    def __create_file(self, path_folder: Path, name: str):
        open(Path(path_folder, name), "x")

    def create_virtual_folder(self):
        path_create = self.__create_folder(self.__path_virtual_environment)
        self.__create_file(path_create, "input.txt")
        self.__create_file(path_create, "output.txt")
        self.__path_virtual_environment = path_create

    def destruction_virtual_folder(self):
        rmtree(self.__path_virtual_environment)

    def move_answer_file_to_virtual_environment(self, file_answer: IAnswerRepository):
        file_name = f"{self.__name_folder}.{file_answer.extension}"

        path_save = Path(self.__path_virtual_environment, file_name)
        file_answer.save_answer(str(path_save))

        self.__path_file_answer = file_name
