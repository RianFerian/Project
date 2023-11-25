def dfs(char, row_index, col_index, clean_area, kingdom_map):
    # Check if the indices are within the valid range
    # Function to right
    if 0 <= row_index < len(kingdom_map) and 0 <= col_index+1 < len(kingdom_map[0]) and kingdom_map[row_index][col_index+1] != "#":
        # print(row_index, col_index)
        if kingdom_map[row_index][col_index+1].isalpha() and kingdom_map[row_index][col_index+1] != char:
            clean_area[0] += 1
        kingdom_map[row_index][col_index+1] = '#'
        dfs(char, row_index, col_index+1, clean_area, kingdom_map)

    if 0 <= row_index < len(kingdom_map) and 0 <= col_index-1 < len(kingdom_map[0]) and kingdom_map[row_index][col_index-1] != "#":
        # print(row_index, col_index)
        if kingdom_map[row_index][col_index-1].isalpha() and kingdom_map[row_index][col_index-1] != char:
            clean_area[0] += 1
        kingdom_map[row_index][col_index-1] = '#'
        dfs(char, row_index, col_index-1, clean_area, kingdom_map)

    if 0 <= row_index+1 < len(kingdom_map) and 0 <= col_index < len(kingdom_map[0]) and kingdom_map[row_index+1][col_index] != "#":
        # print(row_index, col_index)
        if kingdom_map[row_index+1][col_index].isalpha() and kingdom_map[row_index+1][col_index] != char:
            clean_area[0] += 1
        kingdom_map[row_index+1][col_index] = '#'
        dfs(char, row_index+1, col_index, clean_area, kingdom_map)

    if 0 <= row_index-1 < len(kingdom_map) and 0 <= col_index < len(kingdom_map[0]) and kingdom_map[row_index-1][col_index] != "#":
        # print(row_index, col_index)
        if kingdom_map[row_index-1][col_index].isalpha() and kingdom_map[row_index-1][col_index] != char:
            clean_area[0] += 1
        kingdom_map[row_index-1][col_index] = '#'
        dfs(char, row_index-1, col_index, clean_area, kingdom_map)

def process_map(kingdom_map):
    Result = {'contested': 0}

    for row_index, row in enumerate(kingdom_map):
        for col_index, char in enumerate(row):
            if char.isalpha():
                print(row_index, col_index)
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

    # Bank result
    answer_bank = []  # List to store the results

    for case_number in range(1, T+1):
        N = int(input("Enter the number of rows: "))
        M = int(input("Enter the number of columns: "))
        kingdom_map = [input().strip() for _ in range(N)]
        
        # Convert each string to a list of characters
        kingdom_map = [list(row) for row in kingdom_map]

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
            
    # print(answer_bank)

    # Print results
    for case_number, result in enumerate(answer_bank, start=1):
        print(f"Case {case_number}:")
        for key, value in result.items():
            print(f'{key}: {value}')

if __name__ == "__main__":
    main()
