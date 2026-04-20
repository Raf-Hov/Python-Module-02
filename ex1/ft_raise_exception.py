def input_temperature(temp: str) -> int:
    tm = int(temp)
    return tm


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    ls = ["25", "abc", "100", "-50"]
    for i in ls:
        print(f"\nInput data is '{i}'")
        try:
            k = input_temperature(i)
            if k > 40:
                print(f"Caught input_temperature error: {i}°C is too", end=" ")
                print("hot for plants (max 40°C)")
            elif k < 0:
                print(f"Caught input_temperature error: {i}°C is too", end=" ")
                print("cold for plants (min 0°C)")
            else:
                print(f"Temperature is now {k}°C")
        except ValueError:
            print("Caught input_temperature error: invalid literal ", end="")
            print(f"for int() with base 10: '{i}'")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
