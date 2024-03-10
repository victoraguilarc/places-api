def validate_mandatory(data: dict, key: str) -> bool:
    return key in data and data.get(key) is not None
