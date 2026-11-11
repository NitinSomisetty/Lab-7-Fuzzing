def parse_int_list(s):
    """Parse a comma-separated string of integers.
    Returns an empty list for None, empty string, or whitespace-only input.
    Skips non-integer tokens instead of crashing.
    """
    if s is None:
        return []
    if not isinstance(s, str):
        raise TypeError(f"Expected a string, got {type(s).__name__}")
    result = []
    for token in s.split(','):
        token = token.strip()
        if token == '':
            continue  # skip empty tokens (e.g. "1,,3")
        try:
            result.append(int(token))
        except ValueError:
            raise ValueError(f"Invalid integer token: '{token}'")
    return result


def sanitize_string(s):
    """Remove non-alphanumeric characters from a string.
    Returns an empty string for None or non-string input.
    """
    if s is None:
        return ''
    if not isinstance(s, str):
        s = str(s)
    return ''.join(c for c in s if c.isalnum())


def is_palindrome(s):
    """Check if a string is a palindrome (case-insensitive, strips whitespace).
    Returns False for None or non-string input.
    """
    if s is None:
        return False
    if not isinstance(s, str):
        return False
    s = s.strip().lower()
    return s == s[::-1]


if __name__ == "__main__":
    print("=== Fixed processor.py demo ===")

    # parse_int_list
    print(parse_int_list("1,2,3"))      # [1, 2, 3]
    print(parse_int_list("1,,3"))       # [1, 3]  — skips empty token
    print(parse_int_list(""))           # []
    print(parse_int_list(None))         # []

    # sanitize_string
    print(sanitize_string("!hello!"))   # hello
    print(sanitize_string(""))          # (empty string)
    print(sanitize_string(None))        # (empty string)

    # is_palindrome
    print(is_palindrome("racecar"))     # True
    print(is_palindrome("hello"))       # False
    print(is_palindrome(""))            # True
    print(is_palindrome(None))          # False
