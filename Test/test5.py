def find_words(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    value = 0

    # Check horizontally
    for row in matrix:
        start_index = 0
        for i in range(len(row)):
            string_representation = ''.join(row)
            start_index = string_representation.find(target, start_index)
            if start_index != -1:
                value += string_representation.count(target, i, len(row))
                start_index += 1


    # # Check horizontally from left to right
    for row in reversed(matrix):
        row = row[::-1]
        start_index = 0
        for i in range(len(row)):
            string_representation = ''.join(row)
            start_index = string_representation.find(target, start_index)
            if start_index != -1:
                value += string_representation.count(target, i, len(row))
                start_index += 1

    # # Check vertically
    for col in range(cols):        
        words = ''.join(matrix[row][col] for row in range(rows))
        start_index = 0

        # Di loop untuk masing" huruf
        for i in range(len(words)):
            # Kalau ketemu, ambil indexnya
            start_index = words.find(target, start_index)

            if start_index != -1:
                value += words.count(target, start_index, len(words))
                start_index += 1

    # Check vertically from bottom to top
    for col in range(cols):
        words = ''.join(matrix[row][col] for row in range(rows))
        words = words[::-1]
        start_index = 0

        # Di loop untuk masing" huruf
        for i in range(len(words)):
            # Kalau ketemu, ambil indexnya
            start_index = words.find(target, start_index)

            if start_index != -1:
                value += words.count(target, start_index, len(words))
    #             start_index += 1

    # # # Check diagonally from top-left to bottom-right
    for k in range(-rows + 1, cols):
        words = ''.join(matrix[row][row + k] for row in range(max(0, -k), min(rows, cols - k)))
        start_index = 0

        # Di loop untuk masing" huruf
        for i in range(len(words)):
            # Kalau ketemu, ambil indexnya
            start_index = words.find(target, start_index)

            if start_index != -1:
                i = start_index
                value += words.count(target, start_index, len(words))
                start_index += 1

        
    # # Check diagonally from bottom-left to top-right
    for k in range(rows + cols - 1):
        words = ''.join(matrix[row][row + k] for row in range(max(0, -k), min(rows, cols - k)))
        words = words[::-1]
        start_index = 0

        # Di loop untuk masing" huruf
        for i in range(len(words)):
            # Kalau ketemu, ambil indexnya
            start_index = words.find(target, start_index)

            if start_index != -1:
                i = start_index
                value += words.count(target, start_index, len(words))
                start_index += 1


    # Check diagonally from top-right to bottom-left
    for k in range(rows + cols - 1):
        words = ''.join(matrix[row][k - row] for row in range(max(0, k - cols + 1), min(rows, k + 1)))
        start_index = 0

        # Di loop untuk masing" huruf
        for i in range(len(words)):
            # Kalau ketemu, ambil indexnya
            start_index = words.find(target, start_index)

            if start_index != -1:
                value += words.count(target, start_index, len(words))
                start_index += 1


    # # Check diagonally from top-right to bottom-left in reversed order
    for k in range(rows + cols - 1):
        words = ''.join(matrix[row][k - row] for row in range(max(0, k - cols + 1), min(rows, k + 1)))
        words = words[::-1]
        start_index = 0

        # Di loop untuk masing" huruf
        for i in range(len(words)):
            # Kalau ketemu, ambil indexnya
            start_index = words.find(target, start_index)

            if start_index != -1:
                value += words.count(target, start_index, len(words))
                start_index += 1

    return value



def main():
    # Number of cases
    T = int(input("Enter the number of test cases (T): "))

    # Bank result
    results = []  # List to store the results

    for case_number in range(1, T + 1):
        N = int(input())
        M = int(input())

         # Initialize an empty list to store the matrix
        matrix = []

        # Input N strings to form the matrix
        for i in range(N):
            # Get the input string from the user
            input_string = input("Enter the string: ")

            row = []
            for j in input_string:
                row.append(j)
            matrix.append(row)

        for i in range(N):
            print(matrix[i])

        # Now, 'matrix' contains the final matrix formed by N input strings
        # Print the matrix for verification

        target = input("String target: ")

        result = find_words(matrix, target)
        results.append(result)

    # Print results
    for case_number, result in enumerate(results, start=1):
        print(f"Case {case_number}: {result}")

if __name__ == "__main__":
    main()
