# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Dict, Optional, Type

from src.common.domain.messaging.queries import Query, QueryBus, QueryHandler
from src.common.infrastructure.messaging._exceptions import (
    QueryAlreadyExistException,
    QueryHandlerDoesNotExistException,
)


@dataclass
class MemoryQueryBus(QueryBus):
    def __init__(self):
        self._queries: Dict[Type[Query], QueryHandler] = {}

    def subscribe(self, query: Type[Query], handler: QueryHandler):
        if query in self._queries:
            raise QueryAlreadyExistException
        self._queries[query] = handler

    def ask(self, query: Query) -> Optional[object]:
        if query.__class__ not in self._queries:
            raise QueryHandlerDoesNotExistException(query.__class__)
        return self._queries[query.__class__].execute(query)
