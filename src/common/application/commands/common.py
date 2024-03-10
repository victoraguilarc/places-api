# -*- coding: utf-8 -*-

from dataclasses import asdict, dataclass
from typing import List, Optional

from src.common.domain.messaging.commands import Command


@dataclass
class SendEmailCommand(Command):
    to_emails: List[str]
    template_name: str
    context: dict
    subject: Optional[str] = None
    from_email: Optional[str] = None

    @property
    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, kwargs: dict) -> 'SendEmailCommand':
        return cls(**kwargs)
