class OutputFileStream:
    def __init__(self, path_dir):
        self.__path_dir = path_dir

    def read_output(self, output_data):
        try:
            with open(str(self.__path_dir) + "/output.txt", "r") as file:
                output = file.readlines()
                return "".join(output) #list(map(lambda x: x.replace("\n", ""), output))
        except FileNotFoundError:
            return "FileNotFound"
