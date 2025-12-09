import time, os, threading, copy, math, pprint, csv
from AOC_Loader import AOCLoader
from itertools import combinations

YEAR = 2025
DAY = 8

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
        self.coordinates = []
        for item in self.input:
            parts = list(map(int, item.split(",")))
            self.coordinates.append(tuple(parts))
        self.parent = {i: i for i in range(len(self.coordinates))} # maps a node index to its parent index
        self.size = {i: 1 for i in range(len(self.coordinates))} # maps a root index to the number of nodes in that circuit
        self.connection_limit = len(self.coordinates)
        pprint.pprint(self.coordinates)
    
    def solve(self):
        edges = []
        for i, j in combinations(range(len(self.coordinates)), 2): # Generate all possible pairs (edges) with their distances                  
            dist = self.calc_dist_3d(self.coordinates[i], self.coordinates[j])
            edges.append((dist, i, j))
        edges.sort(key=lambda x: x[0]) # ascending
        for dist, u, v in edges[:1000]: # Process n number of shortest edges
            self.union(u, v)
        circuit_sizes = list(self.size.values()) # Get sizes of all remaining circuits
        circuit_sizes.sort(reverse=True)
        if len(circuit_sizes) >= 3:
            result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
            print(f"Circuit sizes: {circuit_sizes}")
            print(f"Top 3 Product: {result}")
            return result
        else:
            print("Not enough circuits formed to calculate top 3.")
            return 0

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            del self.size[root_j]
            return True # Connection made
        return False # Already connected

    def calc_dist_3d(self, point1, point2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

    def __str__(self):
        return str(self.__dict__)
    
class Part2:
    def __init__(self, raw_input, eg_input=""):
        self.raw_input = raw_input
        if eg_input == None or len(raw_input) < 1:
            print("No Example Input")
        if raw_input == None or len(raw_input) < 1:
            raise KeyError("Forgor input value")
        self.eg_input = eg_input.split("\n")
        self.input = self.raw_input.split("\n")
        self.input = self.eg_input
        self.coordinates = {}
        for item in self.input:
            x, y, z = map(int, item.split(","))
            self.coordinates[(x,y,z)] = []
        # pprint.pprint(self.coordinates)
        
    def solve(self):
        pass

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

        self.part1, time_1 = self._run_and_time("Part 1", Part1, copy.deepcopy(self.puzzle_input), copy.deepcopy(self.eg_input))
        self.part2, time_2 = self._run_and_time("Part 2", Part2, copy.deepcopy(self.puzzle_input), copy.deepcopy(self.eg_input))

        os.makedirs("aoc_outputs", exist_ok=True)

        data_to_write = [
            ['part', 'answer', 'time_taken'],
            [1, self.part1, time_1],
            [2, self.part2, time_2]
        ]

        with open(os.path.join("aoc_outputs", f"day_{DAY}_output.csv"), 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(data_to_write)

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
        return result, f"{duration_ms:.4f}" 