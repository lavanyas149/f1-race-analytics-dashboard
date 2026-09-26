from validators import is_valid_position, is_valid_compound
from strategy_simulator import simulate_one_stop


def test_validation():
    assert is_valid_position("5") == True
    assert is_valid_position("25") == False
    assert is_valid_compound("SOFT") == True
    assert is_valid_compound("RAIN") == False
    print("✓ Validator tests passed!")


def test_strategy():
    plan = simulate_one_stop(50, "MEDIUM", "HARD")
    assert plan["pit_lap"] == 25
    assert plan["est_time"] > 0
    print("✓ Strategy simulator tests passed!")


if __name__ == "__main__":
    test_validation()
    test_strategy()
    print("All tests ran successfully!")
