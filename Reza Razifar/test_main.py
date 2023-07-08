import main


def test_name():
    assert main.name() == "Reza"
    assert main.name() != "Ali"
