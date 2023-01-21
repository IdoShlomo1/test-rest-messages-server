from typing import Any

from .api_client import ApiClient


class MessageApi(ApiClient):
    BASE_PATH = '/api'

    def get_messages_by_value(self, key, value):
        return self.get(self.url + "/GetMessages", params={key: value})

    def get_all_messages(self):
        return self.get(self.url + '/GetMessages')

    def add_message(self, message: Any):
        return self.post(self.url + "/AddMessage", json=message)

    def delete_messages(self, key, value):
        return self.delete(self.url + "/DeleteMessage", params={key: value})
