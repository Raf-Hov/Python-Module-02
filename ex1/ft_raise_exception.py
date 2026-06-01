def input_temperature(temp: str) -> int:
    tm = int(temp)
    if tm > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif tm < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return tm


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    ls = ["25", "abc", "100", "-50"]
    for i in ls:
        print(f"\nInput data is '{i}'")
        try:
            k = input_temperature(i)
            print(f"Temperature is now {k}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
