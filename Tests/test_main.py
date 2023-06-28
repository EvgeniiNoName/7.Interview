import pytest
from main import balance


@pytest.mark.parametrize(
    "list, expected",
    [
        (r"(((([{}]))))", "Cбалансированно"),
        (r"[([])((([[[]]])))]{()}", "Cбалансированно"),
        (r"{{[()]}}", "Cбалансированно"),
        (r"}{}", "Несбалансированно"),
        (r"{{[(])]}}", "Несбалансированно"),
        (r"[[{())}]", "Несбалансированно"),
    ],
)
def test_balance(list, expected):
    res = balance(list)
    assert res == expected
