from Matrix import Matrix

mtrix = Matrix([
    [999999991, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -999999999912],
])

print("1 X 12\n")
print(mtrix)
print("\n")

mtrix.resize((2, 6))

print("2 X 6\n")
print(mtrix)
print("\n")

mtrix.resize((3, 4))

print("3 X 4\n")
print(mtrix)
print("\n")

mtrix.resize((4, 3))

print("4 X 3\n")
print(mtrix)
print("\n")

mtrix.resize((6, 2))

print("6 X 2\n")
print(mtrix)
print("\n")

mtrix.resize((12, 1))

print("12 X 1\n")
print(mtrix)
print("\n")

