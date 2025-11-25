import time, os, threading, copy
from AOC_Loader import AOCLoader

class Part1:
    def __init__(self, raw_input):
        self.raw_input = raw_input
        if raw_input == None or len(raw_input) < 1:
            raise KeyError("Forgor input value")
        return self
    
    def solve():
        pass

    def __str__(self):
        return str(self.__dict__)
    
class Part2:
    def __init__(self, raw_input):
        self.raw_input = raw_input
        if raw_input == None or len(raw_input) < 1:
            raise KeyError("Forgor input value")
        return self
        
    def solve(self):
        pass

    def __str__(self):
        return str(self.__dict__)

class Runner:
    def __init__(self):
        try:
            self.loader = AOCLoader(year=2024, day=1)
            self.puzzle_input = self.loader.load_input()
            print(f"Success! Input starts with: {self.puzzle_input[:20]}...")
        except ValueError as e:
            print(e)

        self.part1 = self._run_and_time("Part 1", Part1, copy.deepcopy(self.puzzle_input))
        self.part2 = self._run_and_time("Part 2", Part2, copy.deepcopy(self.puzzle_input))

    def _run_and_time(self, label, func, *args):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        duration_ms = (end_time - start_time) * 1000
        print(f"{label} Execution Time: {duration_ms:.4f} ms")
        return result

