import time, os, threading, copy, math
from AOC_Loader import AOCLoader

YEAR = 2025
DAY = 3

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
        self.joltages = []
    
    def solve(self):
        for bank in self.input:
            # ????????????????????????????????????????????????????????????????????
            # pointer_1 = [len(bank)-2, bank[len(bank)-2]]
            # for i in range(len(bank)-2, -1, -1):
            #     if bank[i] >= pointer_1[1]:
            #         pointer_1[0] = i
            #         pointer_1[1] = bank[i]
            # ???????????????????????????????????????????????????????????????????? WHY NO WORK FROM RIGHT TO LEFT
            pointer_1 = [0, bank[0]]
            for i in range(0, len(bank)-1):
                if bank[i] > pointer_1[1]:
                    pointer_1[0] = i
                    pointer_1[1] = bank[i]
            # ????????????????????????????????????????????????????????????????????
            pointer_2 = [pointer_1[0]+1, bank[pointer_1[0]+1]]
            for i in range(pointer_1[0]+1, len(bank)):
                if bank[i] > pointer_2[1]:
                    pointer_2[0] = i
                    pointer_2[1] = bank[i]

            final = str(pointer_1[1]+pointer_2[1])
            #print(f"Final:[{final}] | For:[{bank}]")
            self.joltages.append(int(final))
        return sum(self.joltages)

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
        #self.input = self.eg_input
        self.num_of_required_digits = 12
        self.joltages = []
        
    def solve(self):
        for bank in self.input:
            if self.num_of_required_digits > len(bank):
                print("Too large")
                return
            if self.num_of_required_digits == len(bank):
                self.joltages.append(int(bank))
                continue
            final = ""
            pointer = self.finder([0, bank[0]], bank, 0, len(bank)-self.num_of_required_digits)
            final += pointer[1]
            for i in range(0, self.num_of_required_digits-1):
                pointer = self.finder([pointer[0]+1, bank[pointer[0]+1]], bank, (pointer[0]+1), (len(bank)-(self.num_of_required_digits-(i+1))))
                final += pointer[1]
            self.joltages.append(int(final))
        return sum(self.joltages)
    
    # def solve(self):
    #     answer = 0
    #     for bank in self.input:
    #         for index in range(self.num_of_required_digits-1, -1, -1):
    #             if index:
    #                 answer += 10 ** index * int(max(bank[: -index]))
    #                 bank = bank[bank.index(max(bank[: -index])) + 1:]
    #             else:
    #                 answer += int(max(bank))
    #     return answer

    # def solve(self):
    #     total = 0
    #     for bank in self.input:
    #         curr = 0
    #         n = len(bank)
    #         r = n
    #         k = self.num_of_required_digits
    #         start = 0
    #         while k > 0:
    #             print("===")
    #             w = r - k + 1
    #             print("w", w)
    #             window = bank[start:(start+w)]
    #             print("window", window)
    #             max_val, idx = self.max_idx(window)
    #             print("max_val", max_val)
    #             print("idx", idx)
    #             curr = (curr*10)+(int(max_val))
    #             print("curr", curr)
    #             r = n - start - idx - 1
    #             print("r", r)
    #             k -= 1
    #             print("k", k)
    #             start = start + idx + 1
    #             print("start", start)
    #         total += curr
    #     return total

    # def max_idx(self, window):
    #     max_val = "0"
    #     idx = 0
    #     for i in range(len(window)-1, -1, -1):
    #         if window[i] > max_val:
    #             idx = i
    #             max_val = window[i]
    #     return max_val, idx
    
    def finder(self, pointer, bank, start_pos, end_pos):
        for i in range(start_pos, end_pos+1):
            if bank[i] > pointer[1]:
                pointer[0] = i
                pointer[1] = bank[i]
        return pointer

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