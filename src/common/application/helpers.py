from datetime import datetime

from pytz import utc




def utc_now():
    """Returns timezoned now date."""
    return datetime.utcnow().replace(tzinfo=utc)

def build_domain(
    hostname: str,
    https: bool = True,
):
    protocol = 'https' if https else 'http'
    return f'{protocol}://{hostname}/'
