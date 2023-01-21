import json
import pytest
import requests
from automation.framework import MessageFactory
from automation.framework.utils import get_test_data, get_random_number


def test_add_message(messages_api):
    message_data = MessageFactory.create()

    add_response = messages_api.add_message(message_data)
    assert add_response.json() == {"Record Added": message_data.body}

    get_response = messages_api.get_messages_by_value('message_id', message_data.message_id)
    assert get_response.json() == [message_data.body]

    with pytest.raises(requests.exceptions.HTTPError) as exeinfo:
        messages_api.add_message(message_data)

    assert exeinfo.value.response.json() == {'Error': 'Record already exists'}
    assert exeinfo.value.response.status_code == 400


@pytest.mark.parametrize('message_data', [
    {},
    {'Some': "Key"},
    [{}],
    MessageFactory.build(application='Kipi ben kipod'),
    MessageFactory.build(application=None),
    MessageFactory.build(content=19238761921),
    MessageFactory(content=None),
    MessageFactory(session_id=757657667),
    MessageFactory(session_id=None),
    MessageFactory(message_id=None),
    MessageFactory(session_id=98787),
    MessageFactory(participants=98787),
    MessageFactory(session_id=None),
    MessageFactory(participants=None),
    MessageFactory(participants='Tea time'),
])
def test_add_invalid_message(messages_api, message_data):
    with pytest.raises(requests.exceptions.HTTPError) as exeinfo:
        messages_api.add_message(message_data)

    assert exeinfo.value.response.json() == {'Error': 'Records data is not valid'}
    assert exeinfo.value.response.status_code == 400


def test_get_all_messages(messages_api, add_multiple_massages):
    messages = list(map(lambda x: x.body, add_multiple_massages()))
    message_list = messages_api.get_all_messages()

    for i in messages:
        assert i in message_list.json()


@pytest.mark.parametrize('size, key, value', [
    (2, 'application', get_random_number()),
    (2, 'content', get_test_data('Content')),
    (1, 'message_id', get_test_data('MessageId')),
    (2, 'session_id', get_test_data('Session')),
    (2, 'participants', [get_test_data('p1'), get_test_data('p1')]),

])
def test_get_messages_by_query(messages_api, add_multiple_massages, key, value, size):
    _messages = add_multiple_massages(size, **{key: value})
    messages = list(map(lambda x: x.__dict__, _messages))
    if key == 'participants':
        value = json.dumps(value)
    message_list = messages_api.get_messages_by_value(key, value)

    assert len(message_list.json()) == size
    for m in messages:
        assert m in message_list.json()


@pytest.mark.parametrize('size, key, value', [
    (2, 'application', get_random_number()),
    (2, 'content', get_test_data('Content')),
    (1, 'message_id', get_test_data('MessageId')),
    (2, 'session_id', get_test_data('Session')),
    (2, 'participants', [get_test_data('p1'), get_test_data('p1')]),
])
def test_delete_messages_by_query(messages_api, add_multiple_massages, size, key, value):
    _messages = add_multiple_massages(size, **{key: value})
    if key == 'participants':
        value = json.dumps(value)
    delete_response = messages_api.delete_messages(key, value)
    assert delete_response.json() == {'Records Deleted': size}

    with pytest.raises(requests.exceptions.HTTPError) as exeinfo:
        messages_api.get_messages_by_value(key, value).json()

    assert exeinfo.value.response.json() == {'Error': 'Record does not exist'}
    assert exeinfo.value.response.status_code == 404


@pytest.mark.parametrize('key, value', [
    ('application', get_random_number()),
    ('content', get_test_data('Content')),
    ('message_id', get_test_data('MessageId')),
    ('session_id', get_test_data('Session')),
    ('test', get_test_data('Test')),
])
def test_delete_non_existing_messages_by_query(messages_api, key, value):
    with pytest.raises(requests.exceptions.HTTPError) as exeinfo:
        messages_api.get_messages_by_value(key, value).json()

    assert exeinfo.value.response.json() == {'Error': 'Record does not exist'}
    assert exeinfo.value.response.status_code == 404


@pytest.mark.parametrize('key, value', [
    ('par', get_random_number()),
    ('content', get_test_data('Content')),
    ('message_id', get_test_data('MessageId')),
    ('session_id', get_test_data('Session')),
    ('test', get_test_data('Test')),
])
def test_delete_non_existing_messages_by_query(messages_api, key, value):
    with pytest.raises(requests.exceptions.HTTPError) as exeinfo:
        messages_api.get_messages_by_value(key, value).json()

    assert exeinfo.value.response.json() == {'Error': 'Record does not exist'}
    assert exeinfo.value.response.status_code == 404
