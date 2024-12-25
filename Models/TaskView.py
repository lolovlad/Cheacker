from typing import List
from pydantic import BaseModel


class SubTest(BaseModel):
    score: int
    filling_type_variable: List[str]
    answer: List[str]


class SettingsTest(BaseModel):
    limitation_variable: List[str]
    necessary_test: List[int]
    check_type: int


class Test(BaseModel):
    type_test: str
    settings_test: SettingsTest
    tests: List[SubTest]


class TaskToTest(BaseModel):
    setting_tests: List[Test]


class Tabel(BaseModel):
    str_limited: str
    necessary_test: str


class Example(BaseModel):
    filling_type_variable: List[str]
    answer: List[str]


class TaskView(BaseModel):
    test: List[Tabel]
    example: Example
