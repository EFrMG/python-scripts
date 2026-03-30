def verify_card_number(digits_in):
    # Handle dashes and spaces
    digits_in = digits_in.replace("-", "").replace(" ", "")

    # Convert to list of integers and reverse it
    # Reversing allows us to always double at odd indices
    digits = [int(d) for d in digits_in][::-1]

    total_sum = 0
    for i, digit in enumerate(digits):
        if i % 2 == 1:
            # Double every other digit starting from the second one from the (original) right
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            total_sum += doubled
        else:
            # Keep other digits as they are (including the check digit at index 0)
            total_sum += digit

    if total_sum % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"


if __name__ == "__main__":
    test_cases = [
        ("453914889", "VALID!"),
        ("4111-1111-1111-1111", "VALID!"),
        ("1234 5678 9012 3456", "INVALID!"),
    ]

    for card_num, expected in test_cases:
        result = verify_card_number(card_num)
        print(f"Card Number: {card_num}\tResult: {result}\tExpected: {expected}")
