from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Union

import pytest

from tests.utils import parse


@dataclass
class ArgTest:
    name: Union[Literal["one"], Literal["two"], Literal["three"], Literal[4]]


def test_valid():
    test = parse(ArgTest, "two")
    assert test.name == "two"


def test_valid_int():
    test = parse(ArgTest, "4")
    assert test.name == 4


def test_invalid():
    with pytest.raises(
        ValueError,
        match=r"invalid choice: 'thename' \(choose from 'one', 'two', 'three', '4'\)",
    ):
        parse(ArgTest, "thename")
