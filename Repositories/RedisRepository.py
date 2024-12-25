from settings import settings
from redis import Redis
from Models import StartCheckMessage


class RedisRepository:
    def __init__(self):
        self.__client = Redis(host=settings.redis_host,
                              port=settings.redis_port,
                              db=0,
                              username=settings.redis_user,
                              password=settings.redis_user_password,
                              decode_responses=True,
                              encoding="utf-8")

    def get_message_in_start_check(self) -> StartCheckMessage:
        with self.__client.client() as c:
            message = c.brpop(["load_review"])
            return StartCheckMessage.model_validate_json(message[1])

    def send_message(self, message: str):
        with self.__client.client() as c:
            c.lpush("container_message", message)

