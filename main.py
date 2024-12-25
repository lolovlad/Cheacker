from time import sleep
from settings import settings
import redis
from sys import argv

from Repositories import RedisRepository
from Classes.CheckingAnswers import check_answer

#id_container = argv[1]

print("start_docker")

redis_repository = RedisRepository()
while True:
    message = redis_repository.get_message_in_start_check()
    answer = check_answer(message)
    print(message.id_trase, message.lang, message.path_file_answer)
    redis_repository.send_message(answer.model_dump_json())


