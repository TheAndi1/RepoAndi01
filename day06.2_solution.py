from __future__ import annotations

import re
from typing import Iterable, Tuple, List

# --------------------------------------------------------------------------- #
# 1. RegEx – Einmal kompilieren (ein Pattern reicht)
# --------------------------------------------------------------------------- #
_CMD_RE = re.compile(
    r"^(turn )?(on|off|toggle) (\d+),(\d+) through (\d+),(\d+)$"
)


def parse_line(line: str) -> Tuple[str, Tuple[int, int], Tuple[int, int]]:
    m = _CMD_RE.match(line.strip())
    if not m:
        raise ValueError(f"Ungültige Zeile: {line!r}")

    action = m.group(2)  # 'on', 'off' oder 'toggle'
    x1, y1, x2, y2 = map(int, (m.group(3), m.group(4), m.group(5), m.group(6)))
    return action, (x1, y1), (x2, y2)



def total_brightness(instructions: Iterable[str]) -> int:
    lights: List[List[int]] = [[0] * 1000 for _ in range(1000)]

    for line in instructions:
        action, (x1, y1), (x2, y2) = parse_line(line)

        for x in range(x1, x2 + 1):
            row = lights[x]          # lokale Referenz
            for y in range(y1, y2 + 1):
                if action == "on":
                    row[y] += 1
                elif action == "off":
                    if row[y] > 0:
                        row[y] -= 1
                else:  # toggle
                    row[y] += 2

    # Summe aller Werte im Raster
    return sum(sum(row) for row in lights)


def _run_tests() -> None:
    assert total_brightness(["turn on 0,0 through 0,0"]) == 1
    assert total_brightness(["toggle 0,0 through 999,999"]) == 2_000_000
    assert total_brightness(
        [
            "turn on 0,0 through 0,0",
            "toggle 0,0 through 0,0",
            "turn off 0,0 through 0,0",
        ]
    ) == 2
    assert total_brightness(["turn off 0,0 through 0,0"]) == 0
    print("Alle Tests erfolgreich!")


if __name__ == "__main__":
    _run_tests()  # Selbst‑tests
    try:
        with open("day06_input.txt") as f:
            data = f.read().strip().splitlines()
        print("Gesamthelligkeit:", total_brightness(data))
    except FileNotFoundError:
        pass