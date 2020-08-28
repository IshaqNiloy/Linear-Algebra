import numpy

class Numpy():
    def __init__(self, arr):
        self.arr = arr

    def find_determinant(self):
        determinant = numpy.linalg.det(arr)
        print('{}'.format(round(determinant,2)))

if __name__ == '__main__':
    dimension = int(input())
    arr = numpy.array([input().split() for _ in range(dimension)], float)
    my_object = Numpy(arr)
    my_object.find_determinant()