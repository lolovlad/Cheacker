class InputStream:
    def __init__(self, name_dir):
        self.__name_dir = name_dir

    def start_stream(self, input_data):
        return "".join(input_data).encode()