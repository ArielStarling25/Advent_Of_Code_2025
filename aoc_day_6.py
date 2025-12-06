import time, os, threading, copy, math, pprint, csv
from AOC_Loader import AOCLoader

YEAR = 2025
DAY = 6

class Part1:
    def __init__(self, raw_input, eg_input=""):
        self.raw_input = raw_input
        if eg_input == None or len(raw_input) < 1:
            print("No Example Input")
        if raw_input == None or len(raw_input) < 1:
            raise KeyError("Forgor input value")
        self.eg_input = eg_input.split('\n')
        self.input = self.raw_input.split('\n')
        #self.input = self.eg_input
        self.input_parsed = []
        for i in range(len(self.input)):
            self.input_parsed.append(self.input[i].split())
        self.grand_total = 0
        #pprint.pprint(self.input_parsed)
    
    def solve(self):
        for x in range(len(self.input_parsed[0])):
            column_total = 0
            for y in range(len(self.input_parsed)-1):
                if self.input_parsed[len(self.input_parsed)-1][x] == '+':
                    column_total += int(self.input_parsed[y][x])
                elif self.input_parsed[len(self.input_parsed)-1][x] == '*':
                    if column_total == 0:
                        column_total = 1
                    column_total *= int(self.input_parsed[y][x])
            self.grand_total += column_total
        return self.grand_total
                
    def __str__(self):
        return str(self.__dict__)
    
class Part2:
    def __init__(self, raw_input, eg_input=""):
        self.raw_input = raw_input
        if eg_input == None or len(raw_input) < 1:
            print("No Example Input")
        if raw_input == None or len(raw_input) < 1:
            raise KeyError("Forgor input value")
        self.eg_input = eg_input.split('\n')
        self.input = self.raw_input.split('\n')
        #self.input = self.eg_input
        self.grand_total = 0
        self.input_parsed = []
        
    def solve(self):
        self.input_parsed = self.parse_columns(self.input)
        columns = list(zip(*self.input_parsed))
        parsed_columns = []
        operators = []
        vertical_nums = []
        for item in columns:
            parsed_columns.append(list(item))
        for item in parsed_columns:
            operators.append(item[len(item)-1].replace(" ", ""))
            item.pop()
            vertical_nums.append(["".join(chars).replace(" ","") for chars in zip(*item)])
        if len(vertical_nums) != len(operators):
            print(f"Error: length of operators doesnt match with vertical_nums")
        try:
            for i in range(len(operators)):
                column_total = 0
                for number in vertical_nums[i]:
                    if number == '':
                        continue
                    #print(f"cumulative:{column_total}|number:{number}|operator:{operators[i]}")
                    if operators[i] == "+":
                        column_total += int(number)
                    elif operators[i] == "*":
                        if column_total == 0:
                            column_total = 1
                        column_total *= int(number)
                self.grand_total += column_total
        except Exception as e:
            print(e.__traceback__)
        return self.grand_total
    
    def parse_columns(self, input_arr):
        # print("INPUT")
        # pprint.pprint(input_arr)
        column_slices = []
        output_array = []
        in_column = False
        start = 0
        combined_max_len = max(len(string) for string in input_arr)
        for i in range(combined_max_len):
            in_empty_column = all(line[i].isspace() for line in input_arr)
            if not in_column and not in_empty_column:
                in_column = True
                start = i
            elif in_column and in_empty_column:
                column_slices.append([start, i])
                in_column = False
        if in_column:
            column_slices.append([start, combined_max_len])
        for string in input_arr:
            row = []
            for item in column_slices:
                row.append(string[item[0]:item[1]])
            output_array.append(row)
        # print("OUTPUT")
        # pprint.pprint(output_array)
        return output_array

    def __str__(self):
        return str(self.__dict__)

class Runner:
    def __init__(self):
        try:
            self.loader = AOCLoader(year=YEAR, day=DAY, strip_input=False)
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