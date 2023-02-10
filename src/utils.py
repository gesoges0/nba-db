import time
from typing import Iterator, TypeVar, Any
from src.db import db

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


def display_func_name(func):
    def display(*args):
        arg_str: str = ", ".join(repr(arg) for arg in args)
        func_name: str = func.__name__
        print(f"execute: {func_name}({arg_str})")
        return func(*args)

    return display


def bulk_insert(datas: list[Any]):
    try:
        db.db_session.bulk_save_objects(datas)
    except Exception as e:
        raise RuntimeError(f"bulk insert: {datas}")
    else:
        db.db_session.commit()
