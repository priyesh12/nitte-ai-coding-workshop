from bug_01_greeting import greet, greet_all


def test_greets_one_student():
    assert greet("Asha", "Infosys") == "Hello Asha, welcome to your Infosys interview!"


def test_greets_everyone():
    out = greet_all(["Asha", "Bhavya"], "TCS")
    assert len(out) == 2, f"expected 2 greetings, got {len(out)}"
    assert out[1] == "Hello Bhavya, welcome to your TCS interview!"


def test_handles_empty_list():
    assert greet_all([], "Wipro") == []
