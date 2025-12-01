import importlib
import sys

def run_puzzle(day):
    """Dynamically imports the day's module and runs the Runner class."""
    module_name = f"aoc_day_{day}"
    
    try:
        print(f"\n{'='*10} Loading {module_name} {'='*10}")
        
        # 1. Dynamically import the module (e.g., import aoc_day_1)
        # reload is used in case you modify the code while this script is running
        module = importlib.import_module(module_name)
        importlib.reload(module) 

        # 2. Check if the Runner class exists in that module
        if hasattr(module, 'Runner'):
            # 3. Instantiate the class. 
            # Since your logic runs in __init__, this immediately starts the solution.
            app = module.Runner()
        else:
            print(f"Error: The class 'Runner' was not found in {module_name}.py")

    except ModuleNotFoundError:
        print(f"Error: File '{module_name}.py' not found. Make sure it exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    while True:
        print("\n--- Advent of Code Launcher ---")
        user_input = input("Enter the Day number (1-12) to run (or 'q' to quit): ").strip()

        if user_input.lower() == 'q':
            print("Exiting...")
            break

        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        day = int(user_input)

        # Enforce the constraint (Day 1 to 12 only)
        if 1 <= day <= 12:
            run_puzzle(day)
        else:
            print("Input out of range. Please choose a day between 1 and 12.")

if __name__ == "__main__":
    main()