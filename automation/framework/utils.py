import json
import uuid
import random
from dataclasses import dataclass

import allure
from allure import attachment_type
from requests import Response
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


def report_response(response, *args, **kwargs):
    with allure.step("Api Call"):
        if isinstance(response, Response):
            allure.attach(f"{response.request.method}", name="response.request.method", attachment_type=attachment_type.TEXT)
            allure.attach(f"{response.request.url}", name="response.request.url", attachment_type=attachment_type.TEXT)
            allure.attach(f'{response.status_code}', name="response.status_code", attachment_type=attachment_type.TEXT)
            allure.attach(json.dumps(response.json(), indent=4), name="response.json", attachment_type=attachment_type.JSON)
            try:
                allure.attach(json.dumps(json.loads(response.request.body), indent=4), name="response.request.body",
                              attachment_type=attachment_type.JSON)
            except TypeError:
                pass
