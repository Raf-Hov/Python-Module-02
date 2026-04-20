def input_temperature(temp: str) -> int:
    tm = int(temp)
    return tm


def print_test(number: int) -> None:
    print(f"Testing operation {number}...")


def test_error_types() -> None:
    k = 0
    print("=== Garden Error Types Demo ===")
    while k <= 4:
        try:
            if k == 0:
                input_temperature("abc")
            elif k == 1:
                k / 0
            elif k == 2:
                open("/non/existent/file")
            elif k == 3:
                "b" + 5
        except ValueError as e:
            print_test(k)
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print_test(k)
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print_test(k)
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print_test(k)
            print(f"Caught TypeError: {e}")
        else:
            print_test(k)
            print("Operation completed successfully")
        k += 1
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
