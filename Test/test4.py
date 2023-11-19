# Function to count the result
def count_result(A, B, K):
    # count as variable for result
    count = 0
    for num in range(A, B + 1):
        # modulo num with k
        if num % K == 0:
            count += 1
    return count

def main():
    # Number of cases
    T = int(input("Enter the number of test cases (T): "))

    # Bank result
    results = []  # List to store the results

    for case_number in range(1, T + 1):
        A = int(input())
        B = int(input())
        K = int(input())

        result = count_result(A, B, K)
        results.append(result)

    # Print results
    for case_number, result in enumerate(results, start=1):
        print(f"Case {case_number}: {result}")

if __name__ == "__main__":
    main()
