import re


class OutputStream:
    def __init__(self, path_dir):
        self.__path_dir = path_dir

    def read_output(self, output_data):
        '''output_data = re.split(r"[\n]", output_data)
        output_data = list(filter(None, output_data))'''
        return output_data

