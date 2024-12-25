from minio import Minio
from minio.helpers import ObjectWriteResult
from settings import settings

from io import BytesIO


class MinioRepository:
    def __init__(self):
        self.__session = Minio(endpoint=f"{settings.minio_host}:{settings.minio_port}",
                               access_key=settings.minio_access_key,
                               secret_key=settings.minio_secret_key,
                               secure=False)

    def upload_file(self,
                    bucket: str,
                    file_key: str,
                    file: str | bytes,
                    content_type: str) -> ObjectWriteResult:

        if isinstance(file, bytes):
            buffer = BytesIO(file)
        else:
            buffer = BytesIO(file.encode("utf-8"))

        result = self.__session.put_object(bucket,
                                           file_key,
                                           buffer,
                                           -1,
                                           part_size=10 * 1024 * 1024,
                                           content_type=content_type)
        return result

    def get_list_file(self,
                      bucket: str,
                      prefix: str) -> list[str] | None:
        try:
            new_list_file = []
            list_files = self.__session.list_objects(bucket, prefix + "/")
            for file in list_files:
                file_name = file.object_name.split("/")[-1]
                new_list_file.append(file_name)
            return new_list_file
        except Exception:
            return None

    def get_file_and_download(self, bucket: str, file_key: str, download_file):
        file = self.__session.fget_object(bucket, file_key, download_file)

    def get_file(self, bucket: str, file_key: str) -> bytes:
        file = self.__session.get_object(bucket, file_key)
        text = file.read()
        return text


