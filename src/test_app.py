from app import get_fruit


def test_get_fruit():
    assert "apple" or "banana" or "orange" in get_fruit()