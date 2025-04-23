from picross_solver.puzzle import Line

cells = [None, True, None, None, None, None, None, None, None, None]
clues = [2]

line = Line(cells, clues)

for possible_line in line.get_all_possible_lines():
    print(possible_line)
