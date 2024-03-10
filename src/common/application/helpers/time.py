import datetime


def epoch_to_date(epoch: int) -> datetime.date:
    return datetime.datetime.fromtimestamp(epoch).date()
