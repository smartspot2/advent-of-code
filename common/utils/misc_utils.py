from collections import Iterable

import networkx as nx
import numpy as np
from rich import print as rprint


def solve_mapping(possibilities: dict[any, Iterable]) -> dict:
    """
    Takes a dict of possible values each key can take on,
    and applies a bipartite maximum matching to solve the constraints.

    :param possibilities: dict of sets or dict of lists,
        denoting the possibilities for each key
    :return: dict mapping each key to a unique value
    """
    as_list = {k: list(v) for k, v in possibilities.items()}
    G = nx.Graph(as_list)
    solution = nx.bipartite.maximum_matching(G)
    # nx produces edges in both directions, so we need to filter them
    solution = {k: v for k, v in solution.items() if k in possibilities}
    missing = [k for k in possibilities if k not in solution]
    if missing:
        rprint('[red]solve_mapping was not able to get a full mapping'
               f' for all keys! (missing {missing})[/red]')
    return solution


def print_coords(*coords: Iterable[tuple[int, int]], mapping: list = None,
                 empty: str = None, rc: bool = True,
                 limit_height: int = -1) -> None:
    """
    Prints out a board, filling in coordinates for each
    coordinate list according to ``mapping``.

    If no mapping is specified (``mapping=None``), then
    all spots will be filled in with the same value.

    :param coords: any amount of coordinate lists/containers to draw
    :param mapping: list of characters (must match length of ``coords``)
        to draw, corresponding to each coordinate list
    :param empty: character for empty element
    :param rc: whether coordinates are in (r, c) order, i.e. (y, x)
    :param limit_height: maximum number of lines to draw
    """
    if empty is None:
        empty = '\u2591' if mapping is None else '`'
    min_r, min_c = np.min(
        [np.min(tuple(coord_list), axis=0) for coord_list in coords],
        axis=0
    )
    max_r, max_c = np.max(
        [np.max(tuple(coord_list), axis=0) for coord_list in coords],
        axis=0
    )
    if not rc:  # switch if (x, y), as we're using an array
        min_r, min_c, max_r, max_c = min_c, min_r, max_c, max_r
    board = np.full((max_r - min_r + 1, max_c - min_c + 1), -1)
    for coord_list_idx, coord_list in enumerate(coords):
        for coord in coord_list:
            if not rc:  # switch because we're using an array
                coord = coord[::-1]
            r, c = coord
            board[r - min_r, c - min_c] = coord_list_idx
    if limit_height != -1:
        board = board[:limit_height]
    # reference text
    print(f'topleft: x={min_c}, y={min_r}')
    # draw board
    s = '\n'.join(
        ''.join(
            empty if val == -1 else mapping[val]
            for val in row
        ) for row in board
    )
    print(s)
