# -*- coding: utf-8 -*-
import json
from dataclasses import dataclass

import boto3

from src.common.domain.messaging.async_tasks import TaskScheduler
from src.common.domain.messaging.commands import Command


@dataclass
class SQSTaskScheduler(TaskScheduler):
    queue_url: str

    def enqueue(self, command: Command):
        client = boto3.client('sqs')
        command_name = command.__class__.__name__
        return client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=json.dumps(
                {
                    'command': command_name,
                    'payload': command.to_dict,
                }
            ),
            MessageAttributes={
                'command': {
                    'StringValue': command_name,
                    'DataType': 'String',
                },
            },
        )
