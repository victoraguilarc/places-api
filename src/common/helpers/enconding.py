import base64
import json
from typing import List, Union


def encode_base64(message: str) -> str:
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode('ascii')


def decode_base64(base64_message: str) -> str:
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('ascii')


def json_dumps_batch(to_convert: List[object]):
    return json.dumps([item_to_dump.to_dict for item_to_dump in to_convert])
