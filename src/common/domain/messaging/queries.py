# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Type


class Query(object):
    pass


@dataclass()
class QueryHandler(ABC):
    @abstractmethod
    def execute(self, query: Query) -> Optional[object]:
        raise NotImplementedError


@dataclass
class QueryBus(ABC):
    @abstractmethod
    def subscribe(self, query: Type[Query], handler: QueryHandler):
        raise NotImplementedError

    @abstractmethod
    def ask(self, query: Query) -> Optional[object]:
        raise NotImplementedError
