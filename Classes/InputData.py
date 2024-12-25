from .InputStream import InputStream
from .InputFileStream import InputFileStream
from Models.Settings import TypeInput

from pathlib import Path

from Repositories.minioRepository import MinioRepository


class InputData:
    def __init__(self, path):
        self.__file_data = InputFileStream(path)
        self.__input_data = InputStream(path)
        self.__input_stream = None
        self.__repo = MinioRepository()
        self.__path = path

    def creating_input_data(self, type_data):
        if type_data == TypeInput.STREAM:
            self.__input_stream = self.__input_data
        elif type_data == TypeInput.FILE:
            self.__input_stream = self.__file_data

    def start_stream(self, input_data: Path):

        input_data = self.__repo.get_file(input_data.parts[0], "/".join(input_data.parts[1: ])).decode("utf-8")
        return self.__input_stream.start_stream(input_data)


