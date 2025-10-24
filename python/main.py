from Matrix import Matrix

mtrixA = Matrix([
    [1, 2, 3],
    [4, 5, 6]
])

mtrixB = Matrix([
    [7, 8],
    [9, 10],
    [11, 12]
])

print("A\n")
print(mtrixA)
print("\nX\n")
print("B\n")
print(mtrixB)
print("\n=\n")

mtrixC = mtrixA * mtrixB

print("C\n")
print(mtrixC)

normalized = mtrixC.normalize()

print(normalized.data)

