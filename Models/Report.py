from pydantic import BaseModel
from typing import List


class TestReport(BaseModel):
    state_test: str = "skip test"
    point_sum: int = 0
    time: List[int] = []
    list_test_report: List[str] = []
    state_report: bool = False
    number_test: int = 1
    memory: List[float] = []


class Report(BaseModel):
    list_report: List[TestReport] = []
