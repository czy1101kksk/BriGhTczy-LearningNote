strings = input().split()
outputs = [i.rjust(8) for i in strings]
print(*outputs)