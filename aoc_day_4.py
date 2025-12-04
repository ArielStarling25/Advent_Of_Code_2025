import time, os, threading, copy, math, pprint
from AOC_Loader import AOCLoader

YEAR = 2025
DAY = 4

class Part1:
    def __init__(self, raw_input, eg_input=""):
        self.raw_input = raw_input
        if eg_input == None or len(raw_input) < 1:
            print("No Example Input")
        if raw_input == None or len(raw_input) < 1:
            raise KeyError("Forgor input value")
        self.eg_input = eg_input.split("\n")
        self.input = self.raw_input.split("\n")
        #self.input = self.eg_input 
        self.accessible_roll_count = 0

        for i in range(0, len(self.input)):
            self.input[i] = [self.input[i][j] for j in range(0, len(self.input[i]))]
        self.input.insert(0, ['.' for i in range(0, len(self.input[0]))])
        self.input.append(['.' for i in range(0, len(self.input[0]))])
        for i in range(0, len(self.input)):
            self.input[i].insert(0, '.')
            self.input[i].append('.')
    
    def solve(self):
        for y in range(1, len(self.input)-1):
            for x in range(1, len(self.input[y])-1):
                if self.input[x][y] == '@' or self.input[x][y] == 'X':
                    grid_array = [self.input[x-1][y-1],
                                  self.input[x][y-1],
                                  self.input[x+1][y-1],
                                  self.input[x+1][y],
                                  self.input[x+1][y+1],
                                  self.input[x][y+1],
                                  self.input[x-1][y+1],
                                  self.input[x-1][y]
                                  ]
                    count = grid_array.count('@') + grid_array.count('X')
                    if count < 4:
                        self.input[x][y] = 'X'
                        self.accessible_roll_count += 1
        return self.accessible_roll_count

    def __str__(self):
        return str(self.__dict__)
    
class Part2:
    def __init__(self, raw_input, eg_input=""):
        self.raw_input = raw_input
        if raw_input == None or len(raw_input) < 1:
            raise KeyError("Forgor input value")
        self.eg_input = eg_input.split("\n")
        self.input = self.raw_input.split("\n")
        #self.input = self.eg_input 
        self.accessible_roll_count = 0

        for i in range(0, len(self.input)):
            self.input[i] = [self.input[i][j] for j in range(0, len(self.input[i]))]
        self.input.insert(0, ['.' for i in range(0, len(self.input[0]))])
        self.input.append(['.' for i in range(0, len(self.input[0]))])
        for i in range(0, len(self.input)):
            self.input[i].insert(0, '.')
            self.input[i].append('.')
        
    def solve(self):
        curr_area_count = 99999
        while curr_area_count >= 1:
            curr_area_count = 0
            x_logger = []
            for y in range(1, len(self.input)-1):
                for x in range(1, len(self.input[y])-1):
                    if self.input[x][y] == '@' or self.input[x][y] == 'X':
                        grid_array = [self.input[x-1][y-1],
                                    self.input[x][y-1],
                                    self.input[x+1][y-1],
                                    self.input[x+1][y],
                                    self.input[x+1][y+1],
                                    self.input[x][y+1],
                                    self.input[x-1][y+1],
                                    self.input[x-1][y]
                                    ]
                        count = grid_array.count('@') + grid_array.count('X')
                        if count < 4:
                            self.input[x][y] = 'X'
                            x_logger.append([x,y])
                            self.accessible_roll_count += 1
                            curr_area_count += 1
            for coordinate in x_logger:
                self.input[coordinate[0]][coordinate[1]] = '.'
        return self.accessible_roll_count

    def __str__(self):
        return str(self.__dict__)

class Runner:
    def __init__(self):
        try:
            self.loader = AOCLoader(year=YEAR, day=DAY)
            self.puzzle_input, self.eg_input = self.loader.load_input()
            print(f"Successfully read data!")
        except ValueError as e:
            print(e)

        self.part1 = self._run_and_time("Part 1", Part1, copy.deepcopy(self.puzzle_input), copy.deepcopy(self.eg_input))
        self.part2 = self._run_and_time("Part 2", Part2, copy.deepcopy(self.puzzle_input), copy.deepcopy(self.eg_input))

    def _run_and_time(self, label, func, *args):
        runnable = func(*args)
        start_time = time.perf_counter()
        result = runnable.solve()
        end_time = time.perf_counter()
        duration_ms = (end_time - start_time) * 1000
        if '67' in f"{duration_ms:.4f}":
            print("6767676767676767676767676767676767676767676767")
            print(f"{label} | Result: [{result}] | Execution Time: {duration_ms:.4f} ms | ")
            print("6767676767676767676767676767676767676767676767")
        elif '69' in f"{duration_ms:.4f}":
            print("6969696969696969696969696969696969696969696969")
            print(f"{label} | Result: [{result}] | Execution Time: {duration_ms:.4f} ms | ")
            print("6969696969696969696969696969696969696969696969")
        else:
            print("=============================================")
            print(f"{label} | Result: [{result}] | Execution Time: {duration_ms:.4f} ms | ")
            print("=============================================")
        return result