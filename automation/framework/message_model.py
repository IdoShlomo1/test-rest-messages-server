from typing import Optional
from dataclasses import dataclass

import factory
from automation.framework.utils import ApplicationId, UUID, DictFormat

factory.Faker.add_provider(ApplicationId)
factory.Faker.add_provider(UUID)


@dataclass
class Message(DictFormat):
    application: int
    session_id: str
    message_id: str
    participants: Optional[list]
    content: str


class MessageFactory(factory.Factory):
    class Meta:
        model = Message

    application = factory.Faker('application_id')
    session_id = factory.Faker('uuid')
    message_id = factory.Faker('uuid')
    participants = ["ascdzxd zdvcszd", "szdvksnz xzdv", "zvdcxk aksjhc"]
    content = factory.Faker('text')
