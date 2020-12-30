from functools import reduce


def knot_hash_round(inp: list[int], seq: list[int], skip: int, pos: int,
                    in_place: bool = True) -> tuple[list[int], int, int]:
    """
    Performs one round of a knot hash on the input sequence.

    :param inp: input sequence of lengths
    :param seq: sequence to modify
    :param skip: current skip size
    :param pos: current pointer position in the sequence
    :param in_place: whether to hash in place
    :return:
    """
    if not in_place:
        seq = seq.copy()
    for length in inp:
        sub = [seq[i % 256] for i in range(pos, pos + length)][::-1]
        for i in range(pos, pos + length):
            seq[i % 256] = sub[i - pos]
        pos += length + skip
        skip += 1
    return seq, skip, pos


def knot_hash(s: str) -> str:
    """Performs a knot hash on the string."""
    inp = [ord(c) for c in s] + [17, 31, 73, 47, 23]
    seq = [*range(256)]
    skip, pos = 0, 0
    for _ in range(64):
        seq, skip, pos = knot_hash_round(inp, seq, skip, pos, in_place=False)
    seq = [reduce(lambda a, b: a ^ b, seq[i:i + 16]) for i in range(0, 256, 16)]
    return ''.join(hex(k)[2:].zfill(2) for k in seq)
