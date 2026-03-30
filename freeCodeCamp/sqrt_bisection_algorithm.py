def square_root_bisection(number_input, tolerance_input=0.01, max_iterations=100):
    if number_input < 0:
        raise ValueError(
            "Square root of negative number is not defined in real numbers"
        )

    if number_input == 0 or number_input == 1:
        print(f"The square root of {number_input} is {number_input}")
        return number_input

    low = 0
    # The square root of a number > 1 lies between 1 and the number
    # The square root of a float between 0 and 1 lies between the number and 1
    # high=max(1, number_input) covers both cases
    high = max(1, number_input)

    for _ in range(max_iterations):
        if high - low <= tolerance_input:
            mid = (low + high) / 2

            print(f"The square root of {number_input} is approximately {mid}")
            return mid

        mid = (low + high) / 2
        # Update the search interval
        if mid**2 < number_input:
            low = mid  # upper half
        else:
            high = mid  # lower half

    print(f"Failed to converge within {max_iterations} iterations")
    return None
