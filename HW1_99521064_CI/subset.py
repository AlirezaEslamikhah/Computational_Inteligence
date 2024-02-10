class Matrix:
    def __init__(self, matrix):
        """
        Initialize a Matrix object with a given list of lists.

        Parameters:
        - matrix (list of lists): Input list of lists representing the matrix.
        """
        self.Matrix = matrix
        self.row_numbers = len(matrix)
        self.column_numbers = len(matrix[0])

    def is_equal(self, second_matrix):
        """
        Check if this Matrix object is equal to another Matrix object.

        Parameters:
        - second_matrix (Matrix): Another Matrix object for comparison.

        Returns:
        - bool: True if the matrices are equal, False otherwise.
        """
        flag = True
        # output = np.zeros((self.row_numbers, self.column_numbers))
        output = [[0 for i in range(self.column_numbers)] for j in range(self.row_numbers)]
        for i in range(self.row_numbers):
            for j in range(self.column_numbers):
                if self.Matrix[i][j] == second_matrix.Matrix[i][j]:
                    output[i][j] = True
                else:
                    output[i][j] = False
                    flag = False
        print("The equality of two Matrices is : ", flag)
        return output

    def is_higher_elementwise(self, second_matrix):
        """
        Check if this Matrix object has higher values element-wise compared to another Matrix object.

        Parameters:
        - second_matrix (Matrix): Another Matrix object for comparison.

        Returns:
        - Matrix: Matrix same shape of the input.
        """

        output = [[0 for i in range(self.column_numbers)] for j in range(self.row_numbers)]
        for i in range(self.row_numbers):
            for j in range(self.column_numbers):
                if self.Matrix[i][j] > second_matrix.Matrix[i][j]:
                    output[i][j] = True
                else:
                    output[i][j] = False
        return output
    
    def is_subset(self, second_matrix):
        # rows1, cols1 = len(matrix1), len(matrix1[0])
        rows2, cols2 = len(second_matrix.Matrix), len(second_matrix.Matrix[0])
        rows1 = self.row_numbers
        cols1 = self.column_numbers
        
        if rows2 > rows1 or cols2 > cols1:
            return False

        for i in range(rows1 - rows2 + 1):
            for j in range(cols1 - cols2 + 1):
                if all(self.Matrix[i + x][j + y] == second_matrix.Matrix[x][y] for x in range(rows2) for y in range(cols2)):
                    return True
        
        return False

    def dot_product(self, second_matrix):
        result = []
        for i in range(self.row_numbers):
            row = []
            for j in range(second_matrix.column_numbers):
                dot_product = 0
                for k in range(self.column_numbers):
                    dot_product += self.Matrix[i][k] * second_matrix.Matrix[k][j]
                row.append(dot_product)
            result.append(row)
        
        return Matrix(result)

matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix4 = Matrix([[5, 6], [8, 9]])
matrix5 = Matrix([[1, 2], [4, 5]])
matrix6 = Matrix([[1, 2], [3, 4]])
# test subset of matrices here and show the result 
flag = matrix1.is_subset(matrix4)
print("The subsetion of Matrices is ", flag)
print(flag)