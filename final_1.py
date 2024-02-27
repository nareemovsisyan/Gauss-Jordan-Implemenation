import numpy as np


def no_zero(res):
    rows, cols = res.shape
    for i in range(rows):
        if i == cols - 1:
            break
        j = 0
        while True:
            if res[i, i] or rows - 1 < i + j:
                break
            if res[i, i] == 0:
                res[i, :], res[(rows - 1 - j), :] = (
                    res[(rows - 1 - j), :],
                    res[i, :].copy(),
                )
                j += 1
    return res


def no_one(res):
    rows, cols = res.shape
    for i in range(rows):
        for j in range(cols):
            if res[i, j] == 0:
                continue
            if res[i, j] == 1:
                break
            else:
                print(f"R{i + 1}/{res[i, j]}")
                res[i, :] /= res[i, j]
                res = np.round(res, decimals=2)
                for d in range(rows):
                    if i == d:
                        continue
                    else:
                        print(f"R{d + 1} - {res[d, i]}*R{i + 1}")
                        res[d, :] -= res[d, j] * res[i, :]
                        res = np.round(res, decimals=2)
                        print(res, "\n")
                break
    return res


def augmented_matrix(res):
    rows, cols = res.shape
    for i in range(rows):
        if res[i, i] == 0:
            continue
        if i == cols - 1:
            break
        print(f"R{i + 1}/{res[i, i]}")
        res[i, :] /= res[i, i]
        res = np.round(res, decimals=2)
        for j in range(rows):
            if i == j:
                continue
            else:
                print(f"R{j + 1} - {res[j, i]}*R{i + 1}")
                res[j, :] -= res[j, i] * res[i, :]
                res = np.round(res, decimals=2)

                print(res, "\n")
    final = no_one(res)
    final = np.around(final, 6)
    return final


def answer(res):
    rows, cols = res.shape

    for i in range(rows - 1, -1, -1):
        if np.sum(res[i, :]) == 0:
            res = np.delete(res, [i], axis=0)

    b_v = res[:, -1]
    res = np.delete(res, [-1], axis=1)

    rows, cols = res.shape

    for i in range(rows):
        if np.sum(res[i, :]) == 0:
            return print("There is no solution")

    for i in range(rows):
        if np.sum(res[i, :]) != 1:
            return print("Infinity solution")

        elif np.sum(res[i, :]) == 1:
            print("There is a unique solution")
            b_v = map(str, b_v)
            return print(" ".join(b_v))

    return print("Infinity solution")


# res = np.array(  # one solution
#     [
#         [1.0, -1.0, 0.0, 3.0, 8.0, 2.0],
#         [4.0, 2.0, 0.0, -1.0, 0.0, -3.0],
#         [-2.0, -4.0, 0.0, 7.0, 7.0, 7.0],
#         [4.0, 7.0, 0.0, -1.0, 11.0, -3.0],
#         [-2.0, -4.0, 8.0, 7.0, 7.0, 7.0],
#     ]
# )

# res = np.array( # Infinity solution
#     [
#         [1.0, -1.0, 3.0, 1.0],
#         [4.0, 2.0, -1.0, -3.0],
#     ]
# )

# res = np.array(  # no solution
#     [
#         [5.0, -3.0, 1.0],
#         [2.0, 1.0, 18.0],
#         [5.0, -3.0, 6.0],
#     ]
# )


# A matrix dimensions
nr = int(input("Enter Number of rows: "))
nc = int(input("Enter Number of columns: "))

# A matrix elements input
matrix = np.zeros((nr, nc))
for i in range(nr):
    for j in range(nc):
        num = float(input(f"Enter Numbers in Matrix A {str(i + 1) + str(j + 1)}: "))
        matrix[i, j] = num

# b vector input
b_vector = np.zeros((nr, 1))
for i in range(nr):
    num = float(input(f"Enter Numbers in Vector b {i + 1}: "))
    b_vector[i, 0] = num

# res A & b matrices concatenation
res = np.concatenate((matrix, b_vector), axis=1)
print(res)

# Display the augmented matrix after Gaussian elimination

print("Original")
print(res)

res_zero = no_zero(res)
print("Final zero")

print(res_zero)
print("Augmented Matrix after Gaussian elimination:")
res_eliminated = augmented_matrix(res_zero)

print("Answers")
end = answer(res_eliminated)