import time, os, threading, copy
from AOC_Loader import AOCLoader

YEAR = 2025
DAY = 1

class Part1:
    def __init__(self, raw_input, eg_input=None):
        self.raw_input = raw_input
        if eg_input == None or len(raw_input) < 1:
            print("No Example Input")
        else:
            self.eg_input = eg_input.split("\n")
        if raw_input == None or len(raw_input) < 1:
            raise KeyError("Forgor input value")
        self.input = self.raw_input.split("\n")
        self.counter = 50
        #self.input = self.eg_input
        self.zero_count = 0
    
    # Optimised
    def solve(self):
        for i in range(len(self.input)):
            num = int(self.input[i][1:])
            if self.input[i][0] == 'R':
                self.counter = self.counter + num
            elif self.input[i][0] == 'L':
                self.counter = self.counter - num
            self.counter = self.counter % 100
            if self.counter == 0:
                self.zero_count += 1
        return self.zero_count

    def __str__(self):
        return str(self.__dict__)
    
class Part2:
    def __init__(self, raw_input, eg_input=None):
        self.raw_input = raw_input
        if eg_input == None or len(raw_input) < 1:
            print("No Example Input")
        else:
            self.eg_input = eg_input.split("\n")
        if raw_input == None or len(raw_input) < 1:
            raise KeyError("Forgor input value")
        self.input = self.raw_input.split("\n")
        self.counter = 50
        self.zero_count = 0
        
    def solve(self):
        for i in range(len(self.input)):
            start_on_0 = False
            num = int(self.input[i][1:])
            if self.counter == 0:
                start_on_0 = True
            if self.input[i][0] == 'R':
                self.counter = self.counter + num
            elif self.input[i][0] == 'L':
                self.counter = self.counter - num
            self.counter = self.circular_motion(self.counter, start_on_0)
        return self.zero_count

    # Optimised
    def circular_motion(self, counter, started_on_0):
        if counter == 0:
            self.zero_count += 1
        elif counter > 0:
            self.zero_count += counter // 100
        else:
            self.zero_count += ((abs(counter) // 100) + 1) - int(started_on_0)
        return counter % 100

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
        print("=============================================")
        print(f"{label} | Result: [{result}] | Execution Time: {duration_ms:.4f} ms | ")
        print("=============================================")
        return result