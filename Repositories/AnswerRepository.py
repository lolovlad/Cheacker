from .minioRepository import MinioRepository
from .IAnswerRepository import IAnswerRepository


class AnswerMinioRepository(IAnswerRepository):
    def __init__(self, path_file: str, extension: str):
        self.__bucket: str = path_file.split("/")[0]
        self.__key_file: str = "/".join(path_file.split("/")[1:])
        self.__extension: str = extension
        self.__session: MinioRepository = MinioRepository()

    @property
    def extension(self) -> str:
        return self.__extension

    def save_answer(self, path_save: str):
        self.__session.get_file_and_download(self.__bucket,
                                             self.__key_file,
                                             path_save)
