def count_divisible_numbers(A, B, K):
    count = 0
    for num in range(A, B + 1):
        if num % K == 0:
            count += 1
    return count

def main():
    T = int(input("Enter the number of test cases (T): "))
    
    # Input all numbers in a single line
    all_numbers = list(map(int, input().split()))

    # Iterate over the groups of three numbers
    for case_number in range(1, T + 1):
        # Extract A, B, and K from the list
        A, B, K = all_numbers[(case_number - 1) * 3 : case_number * 3]

        result = count_divisible_numbers(A, B, K)
        print(f"Case {case_number}: {result}")

if __name__ == "__main__":
    main()
