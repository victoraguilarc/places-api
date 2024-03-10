from dataclasses import dataclass


@dataclass
class PaginationBoundaries(object):
    limit: int
    offset: int


def get_pagination_boundaries(
    page: int,
    page_size: int,
) -> PaginationBoundaries:
    if page <= 1:
        return PaginationBoundaries(offset=0, limit=page_size)
    return PaginationBoundaries(
        offset=page * page_size,
        limit=page * (page_size + 1),
    )
