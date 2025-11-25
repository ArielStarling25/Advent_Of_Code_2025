import shutil
import os
import sys

def duplicate_template():
    source_file = "template.py"
    if not os.path.exists(source_file):
        print(f"Error: Could not find '{source_file}' in the current directory.")
        return
    if len(sys.argv) > 1:
        new_filename = sys.argv[1]
    else:
        new_filename = input("Enter the name for the new file (e.g., day_01.py): ").strip()
    if not new_filename:
        print("Operation cancelled: No filename provided.")
        return
    if not new_filename.endswith(".py"):
        new_filename += ".py"
    if new_filename == source_file:
        print("Error: You cannot name the new file the same as the source.")
        return
    try:
        shutil.copy(source_file, new_filename)
        print(f"✅ Success! Copied '{source_file}' to '{new_filename}'")
    except Exception as e:
        print(f"❌ Error copying file: {e}")

if __name__ == "__main__":
    duplicate_template()