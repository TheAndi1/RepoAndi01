import re

# 1. RegEx‑Muster kompilieren (nur einmal, später schnell)
CMD_RE = re.compile(r'^(turn )?(on|off|toggle) (\d+),(\d+) through (\d+),(\d+)$')

def parse_line(line: str):
    """
    Parse a command line with a regular expression.
    Returns a tuple: (action, (x1, y1), (x2, y2))
    """
    m = CMD_RE.match(line.strip())
    if not m:
        raise ValueError(f"Ungültige Zeile: {line!r}")

    # m.group(2) enthält die Aktion: 'on', 'off' oder 'toggle'
    action = m.group(2)

    # Die nächsten Gruppen sind die Koordinaten (als Strings)
    x1, y1, x2, y2 = map(int, (m.group(3), m.group(4), m.group(5), m.group(6)))
    return action, (x1, y1), (x2, y2)

# ---------------------------------------------
# Das restliche Programm bleibt unverändert
# ---------------------------------------------
def run(instructions):
    lights = [[False]*1000 for _ in range(1000)]

    for line in instructions:
        action, (x1, y1), (x2, y2) = parse_line(line)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if action == 'on':
                    lights[x][y] = True
                elif action == 'off':
                    lights[x][y] = False
                else:  # 'toggle'
                    lights[x][y] = not lights[x][y]

    return sum(light for row in lights for light in row)

# Beispielnutzung
if __name__ == "__main__":
    with open('day06_input.txt') as f:
        data = f.read().strip().splitlines()
    print("Anzahl an Lichtern:", run(data))