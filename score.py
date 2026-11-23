scores = list(map(int, input("Enter scores separated by spaces: ").split()))

total = sum(scores)
average = total / len(scores)

print("Scores:", scores)
print("Sum:", total)
print("Average:", average)

maximum = max(scores)
minimum = min(scores)

print("Maximum score:", maximum)
print("Minimum score:", minimum)
