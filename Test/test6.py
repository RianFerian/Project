def process_map(rows, cols, kingdom_map):
    visited = [[False] * cols for _ in range(rows)]
    factions = {}
    print(rows, len(kingdom_map))
    print(cols, len(kingdom_map[0]))



    alphabetic_coordinates = {}

    # Iterate through each row and column
    for row_idx, row in enumerate(kingdom_map):
        for col_idx, char in enumerate(row):
            if char.isalpha():
                if char not in alphabetic_coordinates:
                    alphabetic_coordinates[char] = []
                alphabetic_coordinates[char].append((row_idx, col_idx))




    def dfs(alphabetic, coord_x, coord_y, last_move = None):
        # print(coord_x, coord_y)
        # Check if the indices are within the valid range
        # Function to go bottom
        if 0 <= coord_x < rows and 0 <= coord_y+1 < cols and kingdom_map[coord_x][coord_y+1] == "." and last_move != "Bottom":
            new_coordinate = (coord_x, coord_y+1)
            if new_coordinate not in alphabetic_coordinates[alphabetic]:
                alphabetic_coordinates[alphabetic].append((coord_x, coord_y+1))
                dfs(alphabetic, coord_x, coord_y+1, last_move="Top")
        # Function to go up
        if 0 <= coord_x < rows and 0 <= coord_y-1 < cols and kingdom_map[coord_x][coord_y-1] == "." and last_move != "Top":
            new_coordinate = (coord_x, coord_y-1)
            # Check if the coordinate was already inside the bank
            if new_coordinate not in alphabetic_coordinates[alphabetic]:
                alphabetic_coordinates[alphabetic].append((coord_x, coord_y-1))
                dfs(alphabetic, coord_x, coord_y-1, last_move="Bottom")
        # Function untuk ke kanan
        if 0 <= coord_x+1 < rows and 0 <= coord_y < cols and kingdom_map[coord_x+1][coord_y] == "." and last_move != "Left":
            new_coordinate = (coord_x+1, coord_y)
            # Check if the coordinate was already inside the bank
            if new_coordinate not in alphabetic_coordinates[alphabetic]:
                alphabetic_coordinates[alphabetic].append((coord_x+1, coord_y))
                dfs(alphabetic, coord_x+1, coord_y, last_move="Right")
        # Function untuk ke kiri
        if 0 <= coord_x-1 < rows and 0 <= coord_y < cols and kingdom_map[coord_x-1][coord_y] == "." and last_move != "Right":
            new_coordinate = (coord_x-1, coord_y)
            # Check if the coordinate was already inside the bank
            if new_coordinate not in alphabetic_coordinates[alphabetic]:
                alphabetic_coordinates[alphabetic].append((coord_x-1, coord_y))
                dfs(alphabetic, coord_x-1, coord_y, last_move="Left")
        return

    # def dfs(row_index, col_index, alphabetic, coord, kingdom_map, last_move = None):
    #     # Check if the indices are within the valid range
    #     if 0 <= row_index < len(kingdom_map) and 0 <= col_index < len(kingdom_map[0]):
    #         if kingdom_map[coord[0],coord[1]] != ".":
    #             return
    #         if kingdom_map[coord[0], coord[1]+1] == ".":
    #             alphabetic_coordinates[char].append((coord[0], coord[1]+1))
    #             dfs()
            
    #         # asaf
    #         print("a")
    #     return

    # alphabetic = [a,b,c]
    for alphabetic in alphabetic_coordinates:
        # alphabetic_coord = (3,5), (6,4)
        for alphabetic_coord in alphabetic_coordinates.get(alphabetic, []):
            # run dfs function
            # print(alphabetic_coord[0], alphabetic_coord[1])
            dfs(alphabetic, alphabetic_coord[0], alphabetic_coord[1], kingdom_map)
    
    # Result
    print(alphabetic_coordinates)


    # for alphabet in :
    #     print(alphabet)

    # def dfs(row, col, faction):
    #     if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col] or kingdom_map[row][col] == '#':
    #         return

    #     visited[row][col] = True

    #     if kingdom_map[row][col] == '.':
    #         return

    #     current_faction = kingdom_map[row][col]
    #     if current_faction not in factions:
    #         factions[current_faction] = 1
    #     else:
    #         factions[current_faction] += 1

    #     for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    #         dfs(row + dr, col + dc, faction)

    # case_number = 1
    # contested_regions = 0

    # for i in range(rows):
    #     for j in range(cols):
    #         if not visited[i][j] and kingdom_map[i][j] != '#':
    #             faction = kingdom_map[i][j]
    #             dfs(i, j, faction)

    # print(f"Case {case_number}:")
    # for faction, regions in sorted(factions.items()):
    #     print(f"{faction} {regions}")

    # for i in range(rows):
    #     for j in range(cols):
    #         if not visited[i][j] and kingdom_map[i][j] != '#':
    #             contested_regions += 1

    # print(f"contested {contested_regions}")


def main():
    T = int(input("Enter the number of test cases: "))

    for _ in range(T):
        N = int(input())
        M = int(input())
        kingdom_map = [input().strip() for _ in range(N)]

        process_map(N, M, kingdom_map)

if __name__ == "__main__":
    main()
