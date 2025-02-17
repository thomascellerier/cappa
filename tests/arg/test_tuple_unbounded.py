from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import cappa
from typing_extensions import Annotated

from tests.utils import parse


def test_positional_arg():
    @dataclass
    class ArgTest:
        numbers: Tuple[int, ...]

    test = parse(ArgTest, "1", "2", "3", "4")
    assert test.numbers == (1, 2, 3, 4)


def test_option_flag():
    @dataclass
    class ArgTest:
        numbers: Annotated[Tuple[int, ...], cappa.Arg(short=True)]

    test = parse(ArgTest, "-n", "1", "-n", "2", "-n", "3", "-n", "4")
    assert test.numbers == (1, 2, 3, 4)
