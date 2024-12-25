from abc import ABC, abstractmethod, abstractproperty


class IAnswerRepository(ABC):

    @abstractmethod
    def save_answer(self, *args, **kwargs):
        pass

    @property
    def extension(self) -> str:
        pass

