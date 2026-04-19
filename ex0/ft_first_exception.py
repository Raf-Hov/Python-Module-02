def input_temperature(temp: str) -> int:
    tm = int(temp)
    return tm


def test_temperature() -> None:
    ls = ["25", "abc"]
    for i in ls:
        print(f"\nInput data is '{i}'")
        try:
            k = input_temperature(i)
            print(f"Temperature is now {k}°C")
        except ValueError:
            print("Caught input_temperature error: invalid literal ", end="")
            print(f"for int() with base 10: '{i}'")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
