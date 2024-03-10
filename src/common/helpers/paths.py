def append_schema(url: str) -> str:
    schema = 'http' if 'localhost' in url or '127.0.0.1' in url else 'https'

    if not url.startswith(schema):
        return f'{schema}://{url}'

    return url
