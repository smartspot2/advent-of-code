from copy import deepcopy
from typing import Union, Dict, Tuple, Callable, List


class GameConsole:
    def __init__(self, data: Union[str, list]):
        """
        Creates and initializes the ``GameConsole`` class.

        :param data: instruction data; if given a string,
            it will be parsed and split into a nested list
        """
        if isinstance(data, str):
            data = [instr.split() for instr in data.lower().split('\n')]
        self._data: List[List[str]] = data
        self.data = deepcopy(self._data)
        self.acc = 0
        self.cur = 0

        # (num args, func)
        self.ops: Dict[str, Tuple[int, Callable]] = {
            'acc': (1, self._op_acc),
            'jmp': (1, self._op_jmp),
            'nop': (-1, lambda *_: ...)  # does nothing
        }

        # instructions that do not require the pointer to be autoincremented
        self.no_autoincrement = {'jmp'}

    def reset(self) -> None:
        """
        Resets the internal state to its originally defined data.
        """
        self.data = deepcopy(self._data)
        self.acc = 0
        self.cur = 0

    def evaluate(self, detect_infinite_loops: bool = False) -> bool:
        """
        Evaluates the stored data of the ``GameConsole`` object.
        
        :param detect_infinite_loops: whether the program should stop when an
            instruction has been encountered twice.
        :return: true if exited normally, false otherwise.
        """
        if detect_infinite_loops:
            visited = set()  # set of indices already visited
        while 0 <= self.cur < len(self.data):
            if detect_infinite_loops:
                if self.cur in visited:
                    break  # already visited, we're in an infinite loop
                visited.add(self.cur)
            op, *args = self.data[self.cur]
            numargs, opfunc = self.ops[op]

            if numargs != -1 and len(args) != numargs:
                raise ValueError('number of arguments not equal to expected '
                                 f'(expected {numargs}, expected {len(args)})')

            opfunc(*args)  # execute instruction with arguments
            if op not in self.no_autoincrement:
                self.cur += 1
        else:
            return True  # exited normally
        return False  # exited with a break

    def swap_instr_at(self, idx: int, swap_dict: Dict[str, str] = None) -> None:
        """
        Swaps the instruction at ``idx`` according to the ``swap_dict``.

        Does no modification if the instruction is not in the dict,
        or if the index is out of bounds.

        :param idx: the index of the modified instruction
        :param swap_dict: the mapping used to replace instructions
        """
        if swap_dict is None or not (0 <= idx < len(self.data)):
            return

        cur_instr = self.data[idx][0]
        if cur_instr not in swap_dict:
            return
        self.modify_instr_at(idx, swap_dict[cur_instr])

    def modify_instr_at(self, idx: int, new_instr: str) -> None:
        """
        Sets the instruction at ``idx`` to become ``new_instr``.

        Does no modification if the index is out of bounds.

        :param idx: the index of the modified instruction
        :param new_instr: the new instruction
        """
        if 0 <= idx < len(self.data):
            self.data[idx][0] = new_instr

    def _op_acc(self, x) -> None:
        """
        Adds ``x`` to the accumulator register.

        :param x: amount to add to register
        """
        self.acc += int(x)

    def _op_jmp(self, x) -> None:
        """
        Increments the pointer position by ``x``.

        :param x: difference in pointer index
        """
        self.cur += int(x)
