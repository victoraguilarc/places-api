from dataclasses import dataclass

from src.common.domain.messaging.queries import Query




@dataclass
class GetUserByEmailQuery(Query):
    email: str


