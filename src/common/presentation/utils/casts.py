from typing import Optional


def clean_boolean(item: Optional[str] = None):
    """Parse string boolean values."""
    if item is not None:
        if isinstance(item, str):
            return item.lower() == 'true'
        elif isinstance(item, bool):
            return item
    return False
