with open("number.txt", "r") as file:
    a = file.read()
b = list((sum(int(a[j]) for j in range(i, i + 7) if j < len(a) - 1)) for i in range(len(a)))
print(b, "\n" + str(max(b)))

print(max(list((sum(int(open("number.txt", "r").read()[j]) for j in range(i, i + 7) if j < len(open("number.txt", "r").read()) - 1)) for i in range(len(open("number.txt", "r").read())))))