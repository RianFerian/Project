def process_map(rows, cols):
    
    global clean_area
    global kingdom_maps

    Result = {}

    def dfs(char, row_index, col_index):
        global clean_area
        global kingdom_maps

        # print(coord_x, coord_y)
        # Check if the indices are within the valid range
        # Function to right
        if  0 <= row_index < rows and 0 <= col_index+1 < cols and kingdom_maps[row_index][col_index+1] != "#":
            if kingdom_maps[row_index][col_index+1].isalpha() and kingdom_maps[row_index][col_index+1] != char:
                clean_area += 1
            kingdom_maps[row_index][col_index+1] = '#'
            dfs(char, row_index, col_index+1)

        if  0 <= row_index < rows and 0 <= col_index-1 < cols and kingdom_maps[row_index][col_index-1] != "#":
            if kingdom_maps[row_index][col_index-1].isalpha() and kingdom_maps[row_index][col_index-1] != char:
                clean_area += 1
            kingdom_maps[row_index][col_index-1] = '#'
            dfs(char, row_index, col_index-1)
        
        if  0 <= row_index+1 < rows and 0 <= col_index < cols and kingdom_maps[row_index+1][col_index] != "#":
            if kingdom_maps[row_index+1][col_index].isalpha() and kingdom_maps[row_index+1][col_index] != char:
                clean_area += 1
            kingdom_maps[row_index+1][col_index] = '#'
            dfs(char, row_index+1, col_index)

        if  0 <= row_index-1 < rows and 0 <= col_index < cols and kingdom_maps[row_index-1][col_index] != "#":
            if kingdom_maps[row_index-1][col_index].isalpha() and kingdom_maps[row_index-1][col_index] != char:
                clean_area += 1
            kingdom_maps[row_index-1][col_index] = '#'
            dfs(char, row_index-1, col_index)

        return
      

    Result['contested'] = 0

    for kingdom_map in kingdom_maps:
        for row_index, row in enumerate(kingdom_map):
            for col_index, char in enumerate(row):     
                # If it was characther:
                if char.isalpha():
                    clean_area = 0
                    dfs(char, row_index, col_index)
                    if clean_area == 0:
                        Result.setdefault(char, 0)
                        Result[char] += 1
                    else:
                        print(kingdom_map)
                        Result['contested'] += 1


    print(Result)



clean_area = 0
kingdom_maps = []

def main():
    T = int(input("Enter the number of test cases: "))

    global kingdom_maps

    for case_number in range(1, T+1):
        N = int(input())
        M = int(input())
        kingdom_maps = [input().strip() for _ in range(N)]

        
        # Convert each string to a list of characters
        kingdom_maps = [list(row) for row in kingdom_maps]


        process_map(N, M)

        print(kingdom_maps[9][3])

if __name__ == "__main__":
    main()
