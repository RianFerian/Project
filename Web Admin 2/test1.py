raw = input()
raw = eval(raw)

for i in range(len(raw)-1):
    if raw[i] + raw[i+1] > 10:
        print(i, i+1)
        break