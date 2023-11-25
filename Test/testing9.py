def permutations():
    global running
    global characters
    global bitmask
    if len(running) == len(characters):
        print(''.join(running), file=output_file)
    else:
        for i in range(len(characters)):
            if ((bitmask >> i) & 1) == 0:
                bitmask |= 1 << i
                running.append(characters[i])
                permutations()
                bitmask &= ~(1 << i)  # Reset the bit when backtracking
                running.pop()

raw = input()
characters = list(raw)
running = []
bitmask = 0
with open("output3.txt", "a") as output_file:
    permutations()

# Open the file in append mode outside the loop

    