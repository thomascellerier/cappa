from __future__ import annotations

from dataclasses import dataclass

import cappa
from typing_extensions import Annotated

from tests.utils import invoke


def level_three():
    return {"level_three": True}


def level_two(level_three: Annotated[dict, cappa.Dep(level_three)]):
    return {"level_two": {**level_three}}


def level_one(level_two: Annotated[dict, cappa.Dep(level_two)]):
    return {"level_one": {**level_two}}


def command(levels: Annotated[dict, cappa.Dep(level_one)]):
    return levels


@cappa.command(invoke=command)
@dataclass
class Command:
    ...


def test_invoke_top_level_command():
    result = invoke(Command)
    assert result == {"level_one": {"level_two": {"level_three": True}}}
