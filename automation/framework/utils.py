import uuid
import random
from dataclasses import dataclass

from faker.providers import BaseProvider


def get_random_number(a: int = 100000, b: int = 1000000000000) -> int:
    return random.randint(a, b)


class UUID(BaseProvider):
    @staticmethod
    def uuid() -> str:
        return str(uuid.uuid4())


class ApplicationId(BaseProvider):
    @staticmethod
    def application_id() -> int:
        return get_random_number()


def get_test_data(msg="") -> str:
    return f'Test{msg}{get_random_number()}'


@dataclass
class DictFormat:
    @property
    def body(self) -> dict:
        return self.__dict__
