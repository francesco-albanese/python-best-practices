from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, recipient: str, subject: str, message: str):
        pass
