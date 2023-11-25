def dfs(char, start_row, start_col, kingdom_map):
    stack = [(start_row, start_col)]
    clean_area = 0

    while stack:
        row, col = stack.pop()

        # Process the current position
        if 0 <= row < len(kingdom_map) and 0 <= col < len(kingdom_map[0]) and kingdom_map[row][col] != "#":
            if kingdom_map[row][col].isalpha() and kingdom_map[row][col] != char:
                clean_area += 1
            kingdom_map[row][col] = '#'

            # Add neighboring positions to the stack
            stack.append((row, col+1))
            stack.append((row, col-1))
            stack.append((row+1, col))
            stack.append((row-1, col))

    return clean_area

def print_step(char, row_index, col_index, clean_area, kingdom_map):
    print(f"Character: {char}")
    print(f"Current Position: ({row_index}, {col_index})")
    print(f"Clean Area: {clean_area[0]}")
    print("Current Kingdom Map:")
    for row in kingdom_map:
        print(''.join(row))
    print()

def process_map(kingdom_map):
    Result = {'contested': 0}

    for row_index, row in enumerate(kingdom_map):
        for col_index, char in enumerate(row):
            if char.isalpha():
                clean_area = [0]
                dfs(char, row_index, col_index, clean_area, kingdom_map)
                if clean_area[0] == 0:
                    Result.setdefault(char, 0)
                    Result[char] += 1
                else:
                    Result['contested'] += 1

    return Result

def main():
    T = int(input("Enter the number of test cases: "))

    for _ in range(T):
        N = int(input("Enter the number of rows: "))
        M = int(input("Enter the number of columns: "))
        kingdom_map = [input().strip() for _ in range(N)]
        
        # Convert each string to a list of characters
        kingdom_map = [list(row) for row in kingdom_map]

        # Print the initial kingdom map
        print("Initial Kingdom Map:")
        for row in kingdom_map:
            print(''.join(row))

        result = process_map(kingdom_map)
        print(result)

        # Print the updated kingdom map after processing each test case
        print("Updated Kingdom Map:")
        for row in kingdom_map:
            print(''.join(row))
        print()  # Add an empty line for better readability

if __name__ == "__main__":
    main()
