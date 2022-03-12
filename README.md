# pytest-pahrametahrize
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pytest-pahrametahrize)](https://pypi.org/project/pytest-pahrametahrize/)
[![PyPI](https://img.shields.io/pypi/v/pytest-pahrametahrize)](https://pypi.org/project/pytest-pahrametahrize/)
[![PyPI - License](https://img.shields.io/pypi/l/pytest-pahrametahrize?color=magenta)](https://github.com/sco1/pytest-pahrametahrize/blob/main/LICENSE)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sco1/pytest-pahrametahrize/main.svg)](https://results.pre-commit.ci/latest/github/sco1/pytest-pahrametahrize/main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)
[![Open in Visual Studio Code](https://img.shields.io/badge/Open%20in-VSCode.dev-blue)](https://vscode.dev/github.com/sco1/pytest-pahrametahrize)
![Works for me!](https://img.shields.io/badge/works-on%20my%20machine-brightgreen)

Parametrize your tests with a Boston accent!

### Examples
```py
import pytest

TRUTHINESS_TEST_CASES = [
    (None, False),
    (False, False),
]


@pytest.mark.parametrize(("in_val", "truth_out"), TRUTHINESS_TEST_CASES)
def test_pahrametahrize(in_val, truth_out):
    assert bool(in_val) == truth_out
```


becomes: 
```py
import pytest

TRUTHINESS_TEST_CASES = [
    (None, False),
    (False, False),
]


@pytest.pahrametahrize(("in_val", "truth_out"), TRUTHINESS_TEST_CASES)
def test_pahrametahrize(in_val, truth_out):
    assert bool(in_val) == truth_out
```

Wicked pissah.
