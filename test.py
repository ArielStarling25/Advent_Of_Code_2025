import pprint
def parse_vertical_columns(lines):
    if not lines:
        return []

    # 1. Normalize: Pad all lines to the length of the longest line
    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]

    # 2. Find Boundaries: Scan vertically to find where columns start and end
    column_slices = []
    in_column = False
    start_index = 0

    for i in range(max_len):
        # Check if the vertical slice at index 'i' is empty across ALL rows
        # We use isspace() to handle spaces, tabs, or non-breaking spaces
        is_gutter = all(line[i].isspace() for line in padded_lines)

        if not in_column and not is_gutter:
            # We just hit a character in a new column
            in_column = True
            start_index = i
        elif in_column and is_gutter:
            # We just hit a vertical gap, so the previous column ended
            column_slices.append((start_index, i))
            in_column = False

    # Capture the last column if the string ends with data
    if in_column:
        column_slices.append((start_index, max_len))

    # 3. Slice: Use the boundaries to cut up the original lines
    output = []
    for line in padded_lines:
        row = []
        for start, end in column_slices:
            row.append(line[start:end])
        output.append(row)

    return output

# --- Test ---
input_array = [
    '123 3285 51 6488888 234  69 ', 
    ' 45 64   87 23      34   67 ', 
    '  6 987  15 314     1222 427', 
    '*   +    *  +       *    +  '
]

result = parse_vertical_columns(input_array)

# Formatting for display
import pprint
pprint.pprint(result)