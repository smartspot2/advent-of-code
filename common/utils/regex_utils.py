import re


def extract_ints(s: str) -> list[int]:
    """Extracts all integers from a string."""
    return [*map(int, re.findall(r'[+\-]?\d+', s))]
