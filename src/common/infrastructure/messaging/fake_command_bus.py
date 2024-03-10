# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import List, Type

from src.common.domain.messaging.commands import Command, CommandBus, CommandHandler


@dataclass
class FakeCommandBus(CommandBus):
    def subscribe(self, command: Type[Command], handler: CommandHandler):
        pass

    def dispatch_batch(self, commands: List[Command], is_async: bool = False):
        pass

    def dispatch(self, command: Command, run_async: bool = False):
        pass
