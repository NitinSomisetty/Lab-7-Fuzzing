import pytest
from hypothesis import given, strategies as st
from processor import parse_int_list, sanitize_string, is_palindrome


# ─────────────────────────────────────────────
# parse_int_list
# ─────────────────────────────────────────────

@given(st.text())
def test_parse_int_list_no_crash(s):
    """parse_int_list should never raise an unhandled exception."""
    try:
        result = parse_int_list(s)
        assert isinstance(result, list)
    except ValueError:
        pass  # expected for non-integer content


@given(st.none())
def test_parse_int_list_none(s):
    """parse_int_list should handle None gracefully."""
    try:
        parse_int_list(s)
    except (TypeError, ValueError):
        pass


@given(st.lists(st.integers()).map(lambda lst: ','.join(map(str, lst))))
def test_parse_int_list_valid_input(s):
    """parse_int_list on a valid comma-separated int string returns a list of ints."""
    result = parse_int_list(s)
    assert isinstance(result, list)
    assert all(isinstance(x, int) for x in result)


# ─────────────────────────────────────────────
# sanitize_string
# ─────────────────────────────────────────────

@given(st.text())
def test_sanitize_string_no_crash(s):
    """sanitize_string should never crash on any string."""
    result = sanitize_string(s)
    assert isinstance(result, str)


@given(st.none())
def test_sanitize_string_none(s):
    """sanitize_string should handle None gracefully."""
    try:
        sanitize_string(s)
    except (TypeError, AttributeError):
        pass


@given(st.text())
def test_sanitize_string_only_alnum(s):
    """Result of sanitize_string should contain only alphanumeric characters."""
    result = sanitize_string(s)
    assert all(c.isalnum() for c in result)


# ─────────────────────────────────────────────
# is_palindrome
# ─────────────────────────────────────────────

@given(st.text())
def test_is_palindrome_no_crash(s):
    """is_palindrome should never crash on any string."""
    try:
        result = is_palindrome(s)
        assert isinstance(result, bool)
    except Exception as e:
        assert False, f"is_palindrome crashed with: {e}"


@given(st.none())
def test_is_palindrome_none(s):
    """is_palindrome should handle None gracefully."""
    try:
        is_palindrome(s)
    except (TypeError, AttributeError):
        pass


@given(st.text().map(lambda s: s + s[::-1]))
def test_is_palindrome_symmetric(s):
    """A string concatenated with its reverse should always be a palindrome."""
    result = is_palindrome(s)
    assert result is True
