# pytest-pahrametahrize
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sco1/pytest-pahrametahrize/main.svg)](https://results.pre-commit.ci/latest/github/sco1/pytest-pahrametahrize/main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)
[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/sco1/pytest-pahrametahrize)

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
