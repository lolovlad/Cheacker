from pydantic import BaseModel
from enum import Enum


class TypeInput(int, Enum):
    STREAM = 1
    FILE = 2


class TypeOutput(int, Enum):
    STREAM = 1
    FILE = 2


class Settings(BaseModel):
    type_input: TypeInput = 1
    type_output: TypeOutput = 1
    timeout: int = 0
    max_size_memory: int = 0
    path_compiler: str = ""
    path_file_test: str = ""
    path_file_answer: str = ""

