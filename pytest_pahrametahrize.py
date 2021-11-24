import typing as t

import pytest


def pahrametahrize(*args, **kwargs) -> t.Callable:
    """Pass arguments straight through to `pytest.mark.parametrize`."""
    return pytest.mark.parametrize(*args, **kwargs)


def pytest_configure() -> None:
    """
    Inject `pahrametahrize` into pytest's namespace.

    See: https://docs.pytest.org/en/latest/deprecations.html#pytest-namespace
    """
    pytest.pahrametahrize = pahrametahrize()
