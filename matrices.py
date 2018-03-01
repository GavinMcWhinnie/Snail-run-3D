class Vector():

    def __init__(self, height, data=None):
        self.height = height
        if data == None:
            self.data = []
            for row in range(0, self.height):
                self.data.append(0)
                setattr(self, ("v" + str(row)), 0)
        else:
            self.data = data
            for row in range(0, self.height):
                setattr(self, ("v" + str(row)), self.data[row])

    def display(self):
        for row in range(0, self.height):
            print("["+str(self.data[row])+"]")

    def get(self, row):
        return self.data[row]

    def set(self, row, value):
        self.data[row] = value
        setattr(self, ("v" + str(row)), value)

    def magnitude(self):
        count = 0
        for item in data:
            count += item**2
        return math.sqrt(count)
        
class Matrix():

    def __init__(self, height, width, data=None):
        self.width = width
        self.height = height
        self.data = []
        if data == None:
            for row in range(0, height):
                column = []
                for col in range(0, width):
                    column.append(0)
                    setattr(self, "m"+(str(row)+str(col)), 0)
                self.data.append(column)
        else:
            self.create_data(data)

    def create_data(self,data):
        for row in range(0, self.height):
            self.data.append(data[row])
            for column in range(0, self.width):
                setattr(self, ("m" + str(row) + str(column)), data[row][column])

    def create_no_data(self):
        for row in range(0, self.height):
            column = []
            for column in range(0, self.width):
                column.append(0)
            self.data.append(column)

    def display(self):
        for row in self.data:
            print(str(row))

    def get(self, row, column):
        return self.data[row][column]

    def get_row(self, row):
        return self.data[row]

    def get_column(self, column):
        total = []
        for row in self.data:
            total.append(row[column])
        return total

    def set(self, row, column, value):
        self.data[row][column] = value
        setattr(self, ("m" + str(row) + str(column)), value)

class plane():

    def __init__(self, data):
        self.data = data
        self.a, self.b, self.c, self.d = self.data
        
    
def matrix_addition(matrix1, matrix2):
    if (matrix1.width != matrix2.width) or (matrix1.height != matrix2.height):
        return(-1)
    else:
        height = matrix1.height
        width = matrix1.width
        total = Matrix(height, width)
        for row in range(0, height):
            for column in range(0, width):
                total.set(row, column, matrix1.get(row, column) + matrix2.get(row, column))
        return total

def matrix_product(matrix1, matrix2):
    if  matrix1.width == matrix2.height:
        product = Matrix(matrix1.height, matrix2.width)
        for row in range(0, product.height):
            for column in range(0, product.width):
                product.set(row, column, (dot_product(matrix1.get_row(row), matrix2.get_column(column))))
        return product
    elif matrix1.width == matrix2.height:
        pass
    else:
        return(-1)

def matrix_vector_vector_product(matrix1, vector1):
    if matrix1.width == vector1.height:
        product = Vector(vector1.height)
        for row in range(0, matrix1.height):
            product.set(row, dot_product(matrix1.data[row], vector1.data))
        return product
    else:
        return -1

def vector_subtraction(vector1, vector2):
    if vector1.height == vector2.height:
        total = Vector(vector1.height)
        for row in range(0, vector1.height):
            total.set(row, (vector1.get(row) - vector2.get(row)))
        return total
    else:
        return -1

def vector_addition(vector1, vector2):
    if vector1.height == vector2.height:
        total = Vector(vector1.height)
        for row in range(0, vector1.height):
            total.set(row, (vector1.get(row) + vector2.get(row)))
        return total
    else:
        return -1

def scalar_vector_product(scalar1, vector1):
    product = Vector(vector1.height)
    for row in range(0, vector1.height):
        product.set(row, vector1.get(row) * scalar1)
    return product

def dot_product(x,y):
    if len(x) == len(y):
        total = 0
        for n in range(0, len(x)):
            total += x[n] * y[n]
        return total
    else:
        return -1
