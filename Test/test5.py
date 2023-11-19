def find_words(N,M,K):
    matrix = [[0 for _ in range(N)] for _ in range(M)]
    



def main():
    # Number of cases
    T = int(input("Enter the number of test cases (T): "))

    # Bank result
    results = []  # List to store the results

    for case_number in range(1, T + 1):
        N = int(input())
        M = int(input())
        for i in range(N):
            # Get the input string from the user
            input_string = input("Enter the string: ")

            # Split the input string into a list of words
            words = input_string.split()

        # Create a matrix from the input words
        matrix = [[word[i] if i < len(word) else ' ' for i in range(M)] for word in words]

        target = input("String target: ")

        

        results.append(result)

    # Print results
    for case_number, result in enumerate(results, start=1):
        print(f"Case {case_number}: {result}")

if __name__ == "__main__":
    main()
