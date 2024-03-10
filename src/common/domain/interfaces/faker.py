from abc import ABC, abstractmethod


class FakerInterface(ABC):
    @abstractmethod
    def word(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def uuid4(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def sentence(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def ascii_free_email(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def paragraph(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def sha256(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def fake_username(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def email(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def first_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def last_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def simple_profile(self) -> dict:
        raise NotImplementedError
