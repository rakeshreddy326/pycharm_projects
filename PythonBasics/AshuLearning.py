def check_status(j_angry, s_angry):
    if (j_angry and s_angry) or (not j_angry and not s_angry):
        # Case 2: Both a and b are negative, and flag is true
        return True
    else:
        # Case 1: Either a or b (not both) is non-negative, and flag is false
        return False  # XOR logic for one but not both non-negative

# Example usage
print(check_status(True, True))  # True
print(check_status(True, False))  # True
print(check_status(False, False))   # False
print(check_status(False, True)) # False
