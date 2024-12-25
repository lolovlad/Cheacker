from pydantic import BaseModel
from .Settings import Settings


class StartCheckMessage(BaseModel):
    id_trase: str
    lang: str
    path_file_test: str
    path_file_answer: str
    settings: Settings


class ResultCheckMessage(BaseModel):
    trace_uuid: str = None
    total: str = None
    memory_size: float = None
    points: int = None
    number_test: int = None
    time: str = None
    path_report_file: str = None

