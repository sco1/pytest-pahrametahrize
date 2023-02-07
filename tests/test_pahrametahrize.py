import typing as t

import pytest

TRUTHINESS_TEST_CASES = [
    (None, False),
    (False, False),
    (True, True),
    (1, True),
    (1.0, True),
    (0, False),
    (0.0, False),
]


@pytest.pahrametahrize(("in_val", "truth_out"), TRUTHINESS_TEST_CASES)  # type: ignore[attr-defined]
def test_pahrametahrize(in_val: t.Union[None, bool, float], truth_out: bool) -> None:
    assert bool(in_val) == truth_out
