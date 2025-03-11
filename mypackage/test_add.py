from mypackage.add import add  # Instead of from mypackage.app import add


def test_add():
    assert add(2, 3) == 5
