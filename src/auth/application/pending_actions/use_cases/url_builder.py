from dataclasses import dataclass
from typing import Dict

from src.auth.domain.interfaces.token_path_finder import CallbackData
from src.common.domain.entities.pending_action import PendingAction
from src.common.domain.enums.auth import PendingActionNamespace
from src.common.domain.interfaces.services import Service


@dataclass
class PendingActionUrlBuilder(Service):
    pending_action: PendingAction
    namespace: PendingActionNamespace
    hostnames_map: Dict[PendingActionNamespace, CallbackData]
    default_token_path: CallbackData

    def execute(self, *args, **kwargs):
        token_path: CallbackData = self.hostnames_map.get(self.namespace, self.default_token_path)
        return token_path.apply_token(self.pending_action.token)
