from AOC_Loader import AOCLoader
import os

try:
    loader = AOCLoader(year=2024, day=1)
    puzzle_input = loader.load_input()
    print(f"Success! Input starts with: {puzzle_input[:20]}...")
except ValueError as e:
    print(e)