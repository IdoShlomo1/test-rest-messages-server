import pytest
from requests import Session

from .settings import URL
from .framework.messages_api import MessageApi
from .framework.message_model import MessageFactory
from .framework.utils import report_response


@pytest.fixture
def messages_api() -> MessageApi:
    session = Session()
    return MessageApi(session=session, url=URL, hooks=[report_response])


@pytest.fixture
def add_multiple_massages(messages_api):
    def _add_massages(size=5, **pair):
        messages = MessageFactory.create_batch(size=size, **pair)
        for message in messages:
            messages_api.add_message(message.body)
        return messages

    return _add_massages

