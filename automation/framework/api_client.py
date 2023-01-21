from typing import Optional, Callable
from requests import Session, Response
from dataclasses import dataclass


@dataclass
class ParsedResponse:
    data: object


@dataclass
class CustomResponse:
    status_code: int
    obj: object


class ApiClient:
    BASE_PATH = ''

    def __init__(self, session: Session, url: str, hooks: Optional[Callable] = None):
        self._url = url
        self.session = session
        if hooks:
            session.hooks['response'].extend(hooks)

    @property
    def url(self) -> str:
        return self._url + self.BASE_PATH

    def _call(self, method, *args, **kwargs) -> Optional[Response]:
        """
        :param method:
        :param args:
        :param kwargs:
        :return: Response
        """
        response = self.session.request(method, *args, **kwargs)

        response.raise_for_status()
        return response

    def get(self, *args, **kwargs) -> Optional[Response]:
        return self._call('GET', *args, **kwargs)

    def post(self, *args, **kwargs) -> Optional[Response]:
        if 'json' in kwargs:
            if hasattr(kwargs['json'], 'body'):
                kwargs['json'] = kwargs['json'].body

        return self._call('POST', *args, **kwargs)

    def put(self, *args, **kwargs) -> Optional[Response]:
        return self._call('put', *args, **kwargs)

    def delete(self, *args, **kwargs) -> Optional[Response]:
        return self._call('DELETE', *args, **kwargs)

    def patch(self, *args, **kwargs) -> Optional[Response]:
        return self._call('PATCH', *args, **kwargs)
