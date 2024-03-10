# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.common.domain.entities.pending_action import PendingAction


@dataclass
class PendingActionPresenter(object):
    instance: PendingAction

    @property
    def to_dict(self):
        return {
            **self.instance.to_tracking_dict,
            'metadata': self.instance.metadata,
            'expires_at': self.instance.expires_at,
        }
