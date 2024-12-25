from .OutputStream import OutputStream
from .OutputFileStream import OutputFileStream
from Models.Settings import TypeOutput


class OutputData:
    def __init__(self, path):
        self.__input_data = OutputStream(path)
        self.__file_data = OutputFileStream(path)
        self.__output_stream = None

    def creating_output_data(self, type_data):
        if type_data == TypeOutput.STREAM:
            self.__output_stream = self.__input_data
        elif type_data == TypeOutput.FILE:
            self.__output_stream = self.__file_data

    def read_output(self, input_data):
        return self.__output_stream.read_output(input_data)