from pydantic import BaseModel
from typing import List
from enum import Enum


class Rating(Enum):
    OK = 1
    COMPILATION_ERROR = 2
    WRONG_ANSWER = 3
    PRESENTATION_ERROR = 4
    TIME_LIMIT_EXCEEDED = 5
    MEMORY_LIMIT_EXCEEDED = 6
    OUTPUT_LIMIT_EXCEEDED = 7
    RUN_TIME_ERROR = 8
    PRECOMPILE_CHECK_FAILED = 9
    IDLENESS_LIMIT_EXCEEDED = 10


class ReportTesting(BaseModel):
    out: str = None
    errors: Rating = Rating.WRONG_ANSWER
    time: int = 0
    memory: float = 0.0
