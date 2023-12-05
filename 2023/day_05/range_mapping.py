from typing import List, Tuple


class RangeMapping:
    def __init__(self) -> None:
        self._ranges: List[Tuple[int, int, int]] = []

    def add(self, destenation: int, source: int, delta: int) -> None:
        self._ranges.append((destenation, source, delta))

    def __getitem__(self, key: int) -> int:
        for destenation, source, delta in self._ranges:
            if source <= key < source + delta:
                return destenation + key - source
        return key
