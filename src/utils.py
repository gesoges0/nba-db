import time
from typing import Iterator, TypeVar

T = TypeVar("T")

# default config
DEFAULT_SLEEPING_TIME = 1

# default ids
DEFAULT_ACTIVE_PLAYER_ID: int = 202331  # Paul George
DEFAULT_INACTIVE_PLAYER_ID: int = 2747  # JR Smith
DEFAULT_TEAM_ID: int = 1610612746  # LA Clippers


def iterate_and_wait(
    iter: Iterator[T], sleeping_sec: int = DEFAULT_SLEEPING_TIME
) -> Iterator[T]:
    for i in iter:
        yield i
        time.sleep(sleeping_sec)
