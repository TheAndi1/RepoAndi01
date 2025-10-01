def parse_line(line):
    # liefert (op, (x1, y1), (x2, y2))
    parts = line.split()
    if parts[0] == 'turn':
        op = parts[1]            # "on" oder "off"
        start = parts[2]
        end   = parts[4]
    else:                         # "toggle"
        op = 'toggle'
        start = parts[1]
        end   = parts[3]
    x1, y1 = map(int, start.split(','))
    x2, y2 = map(int, end.split(','))
    return op, (x1, y1), (x2, y2)

def run(instructions):
    lights = [[False]*1000 for _ in range(1000)]

    for line in instructions:
        op, (x1, y1), (x2, y2) = parse_line(line)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if op == 'on':
                    lights[x][y] = True
                elif op == 'off':
                    lights[x][y] = False
                else:  # toggle
                    lights[x][y] = not lights[x][y]

    return sum(light for row in lights for light in row)

# Beispielnutzung:
if __name__ == "__main__":
    with open('day06_input.txt') as f:
        data = f.read().strip().splitlines()
    print("Anzahl an Lichtern:", run(data))