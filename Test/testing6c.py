# FINAL

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

def process_map(kingdom_map):
    Result = {'contested': 0}

    for row_index, row in enumerate(kingdom_map):
        for col_index, char in enumerate(row):
            if char.isalpha():
                clean_area = dfs(char, row_index, col_index, kingdom_map)
                if clean_area == 0:
                    Result.setdefault(char, 0)
                    Result[char] += 1
                else:
                    Result['contested'] += 1

    return Result

def main():
    T = int(input("Enter the number of test cases: "))

    answer_bank = []

    for _ in range(T):
        N = int(input("Enter the number of rows: "))
        M = int(input("Enter the number of columns: "))
        kingdom_map = [input().strip() for _ in range(N)]
        
        # Convert each string to a list of characters
        kingdom_map = [list(row) for row in kingdom_map]

        # # Print the initial kingdom map
        # print("Initial Kingdom Map:")
        # for row in kingdom_map:
        #     print(''.join(row))

        result = process_map(kingdom_map)

        result = dict(sorted(result.items()))
        # Separate the 'contested' item
        contested_item = ('contested', result.pop('contested', None))
        # Sort the remaining items based on keys
        sorted_items = sorted(result.items())
        # Add the 'contested' item back at the end
        sorted_items.append(contested_item)
        # Create the sorted dictionary
        sorted_dict = dict(sorted_items)
        answer_bank.append(sorted_dict)

    # Write results to a text file
    with open("output.txt", "w") as output_file:
        for case_number, result in enumerate(answer_bank, start=1):
            print(f"Case {case_number}:", file=output_file)
            for key, value in result.items():
                print(f'{key} {value}', file=output_file)

        # # Print the updated kingdom map after processing each test case
        # print("Updated Kingdom Map:")
        # for row in kingdom_map:
        #     print(''.join(row))
        # print()  # Add an empty line for better readability

if __name__ == "__main__":
    main()
