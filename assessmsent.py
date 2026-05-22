def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        # move left pointer to next alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        # move right pointer to previous alphanumeric
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


s = "was it a car or a cat i saw"

print("Palindrome" if is_palindrome(s) else "Not a palindrome")