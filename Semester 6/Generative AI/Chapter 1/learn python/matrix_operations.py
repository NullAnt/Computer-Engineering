import numpy as np
import pandas as pd
import time

def display_options():
    print("This is a matrix operation HUB!")
    print("1. Add matrices")
    print("2. Subtract matrices")
    print("3. Matrix multiplication")
    print("4. Transpose a matrix")
    print("5. Determinant of a matrix")
    print("6. Inverse a matrix")
    print("7. Exit")


def take_matrix():
    mat = []
    

    number_of_rows = int(input("Enter the number of rows: "))
    number_of_columns = int(input("Enter the number of columns: "))

    for i in range(number_of_rows):
        row = []
        for j in range(number_of_columns):
            num = int(input("Enter a number: "))
            row.append(num)
        print("Now for next row...")
        mat.append(row)

    # mat = [[1,2],[3,4]]
    # print(mat)
    return np.array(mat)


def add_matrices(mat_A, mat_B):
    return np.add(mat_A, mat_B)

def subtract_matrices(mat_A, mat_B):
    return np.subtract(mat_A, mat_B)

def matrix_multiplication(mat_A, mat_B):
    return np.matmul(mat_A, mat_B)

def transpose_matrix(mat_A):
    return np.transpose(mat_A)

def determinant(mat_A):
    return np.linalg.det(mat_A)

def inverse_matrix(mat_A):
    return np.linalg.inv(mat_A)

def df_from_matrix(mat):
    dim = mat.shape
    print(dim)
    row_labels = [f"Row {i}" for i in range(dim[0])]
    col_labels = [f"Col {i}" for i in range(dim[1])]

    return pd.DataFrame(mat, index=row_labels, columns=col_labels)

def main():
    display_options()

    option = int(input("Enter your choice (1-7): "))

    match option:
        case 1:
            print("Enter the first matrix:")
            mat_A = take_matrix()
            print("Enter the second matrix:")
            mat_B = take_matrix()

            start_time = time.time()
            print("Addition is:")
            print(df_from_matrix(add_matrices(mat_A, mat_B)))

        case 2:
            print("Enter the first matrix:")
            mat_A = take_matrix()
            print("Enter the second matrix:")
            mat_B = take_matrix()

            start_time = time.time()
            print("Subtraction is:")
            print(df_from_matrix(subtract_matrices(mat_A, mat_B)))

        case 3:
            print("Enter the first matrix:")
            mat_A = take_matrix()
            print("Enter the second matrix:")
            mat_B = take_matrix()

            start_time = time.time()
            print("Matrix multiplication is:")
            print(df_from_matrix(matrix_multiplication(mat_A, mat_B)))

        case 4:
            print("Enter the first matrix:")
            mat_A = take_matrix()

            start_time = time.time()
            print("Transpose is:")
            print(df_from_matrix(transpose_matrix(mat_A)))

        case 5:
            print("Enter the first matrix:")
            mat_A = take_matrix()

            start_time = time.time()
            print("The determinant is:")
            print(determinant(mat_A))

        case 6:
            print("Enter the first matrix:")
            mat_A = take_matrix()

            start_time = time.time()
            print("Inverse is:")
            print(df_from_matrix(inverse_matrix(mat_A)))

        case _:
            print("Exit")
            start_time = time.time()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Logic execution time: {total_time:.6f} seconds")





if __name__ == "__main__":
    main()   