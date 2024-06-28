from typing import List, Union, Tuple

class Array:
    def __init__(self, data: Union[List, List[List]]):
        self.data = data
        self.shape = self._get_shape(data)

    def _get_shape(self, data: Union[List, List[List]]) -> Tuple[int, ...]:
        if isinstance(data[0], list):
            return (len(data), len(data[0]))
        else:
            return (len(data),)

    def __len__(self) -> int:
        return len(self.data)

    def __add__(self, other: Union['Array', int, float]) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les dimensions ne correspondent pas pour l'addition")
            if len(self.shape) == 1:
                return Array([self.data[i] + other.data[i] for i in range(len(self.data))])
            else:
                return Array([[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))])
        elif isinstance(other, (int, float)):
            if len(self.shape) == 1:
                return Array([self.data[i] + other for i in range(len(self.data))])
            else:
                return Array([[self.data[i][j] + other for j in range(len(self.data[0]))] for i in range(len(self.data))])
        else:
            raise TypeError(f"Type d'opérande non pris en charge pour +: 'Array' et '{type(other).__name__}'")

    def __sub__(self, other: Union['Array', int, float]) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les dimensions ne correspondent pas pour la soustraction")
            if len(self.shape) == 1:
                return Array([self.data[i] - other.data[i] for i in range(len(self.data))])
            else:
                return Array([[self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))])
        elif isinstance(other, (int, float)):
            if len(self.shape) == 1:
                return Array([self.data[i] - other for i in range(len(self.data))])
            else:
                return Array([[self.data[i][j] - other for j in range(len(self.data[0]))] for i in range(len(self.data))])
        else:
            raise TypeError(f"Type d'opérande non pris en charge pour -: 'Array' et '{type(other).__name__}'")

    def __mul__(self, other: Union['Array', int, float]) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les formes ne correspondent pas pour la multiplication")
            if len(self.shape) == 1:
                return Array([self.data[i] * other.data[i] for i in range(len(self.data))])
            else:
                return Array([[self.data[i][j] * other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))])
        elif isinstance(other, (int, float)):
            if len(self.shape) == 1:
                return Array([self.data[i] * other for i in range(len(self.data))])
            else:
                return Array([[self.data[i][j] * other for j in range(len(self.data[0]))] for i in range(len(self.data))])
        else:
            raise TypeError(f"Type d'opérande non pris en charge pour *: 'Array' et '{type(other).__name__}'")

    def __truediv__(self, other: Union['Array', int, float]) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les dimensions ne correspondent pas pour la division")
            if len(self.shape) == 1:
                return Array([self.data[i] / other.data[i] for i in range(len(self.data))])
            else:
                return Array([[self.data[i][j] / other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))])
        elif isinstance(other, (int, float)):
            if len(self.shape) == 1:
                return Array([self.data[i] / other for i in range(len(self.data))])
            else:
                return Array([[self.data[i][j] / other for j in range(len(self.data[0]))] for i in range(len(self.data))])
        else:
            raise TypeError(f"Type d'opérande non pris en charge pour /: 'Array' et '{type(other).__name__}'")

    def __matmul__(self, other: 'Array') -> Union['Array', int, float]:
        if len(self.shape) != 1 or len(other.shape) != 1:
            raise ValueError("La methode matmul ne prend en charge que les tableaux 1D")
        if self.shape != other.shape:
            raise ValueError("Les dimensions ne correspondent pas pour matmul")
        return sum([self.data[i] * other.data[i] for i in range(len(self.data))])

    def __contains__(self, item: Union[int, float]) -> bool:
        if len(self.shape) == 1:
            return item in self.data
        else:
            for row in self.data:
                if item in row:
                    return True
            return False

    def __getitem__(self, key: Union[int, slice, Tuple[Union[int, slice], Union[int, slice]]]) -> Union[int, float, List[Union[int, float]], 'Array']:
        if isinstance(key, tuple):
            if isinstance(key[0], slice) or isinstance(key[1], slice):
                rows = self.data[key[0]]
                if isinstance(rows, list):
                    return Array([row[key[1]] for row in rows])
                else:
                    return Array([rows[key[1]]])
            return self.data[key[0]][key[1]]
        elif isinstance(key, slice):
            return self.data[key]
        else:
            return self.data[key]

    def __repr__(self) -> str:
        return f"Array({self.data})"
    
import unittest
from numpy import Array
class TestArray(unittest.TestCase):

    def test_creation(self):
        arr1 = Array([1, 2, 3])
        self.assertEqual(arr1.shape, (3,))
        
        arr2 = Array([[1, 2], [3, 4]])
        self.assertEqual(arr2.shape, (2, 2))

    def test_addition(self):
        arr1 = Array([1, 2, 3])
        arr2 = Array([4, 5, 6])
        result = arr1 + arr2
        self.assertEqual(result.data, [5, 7, 9])
        
        arr3 = Array([[1, 2], [3, 4]])
        arr4 = Array([[5, 6], [7, 8]])
        result = arr3 + arr4
        self.assertEqual(result.data, [[6, 8], [10, 12]])
        
        result = arr1 + 10
        self.assertEqual(result.data, [11, 12, 13])

    def test_subtraction(self):
        arr1 = Array([1, 2, 3])
        arr2 = Array([4, 5, 6])
        result = arr1 - arr2
        self.assertEqual(result.data, [-3, -3, -3])
        
        result = arr1 - 1
        self.assertEqual(result.data, [0, 1, 2])

    def test_multiplication(self):
        arr1 = Array([1, 2, 3])
        arr2 = Array([4, 5, 6])
        result = arr1 * arr2
        self.assertEqual(result.data, [4, 10, 18])
        
        result = arr1 * 2
        self.assertEqual(result.data, [2, 4, 6])

    def test_division(self):
        arr1 = Array([4, 6, 8])
        arr2 = Array([2, 3, 4])
        result = arr1 / arr2
        self.assertEqual(result.data, [2, 2, 2])
        
        result = arr1 / 2
        self.assertEqual(result.data, [2, 3, 4])

    def test_dot_product(self):
        arr1 = Array([1, 2, 3])
        arr2 = Array([4, 5, 6])
        result = arr1 @ arr2
        self.assertEqual(result, 32)

    def test_contains(self):
        arr1 = Array([1, 2, 3])
        self.assertTrue(2 in arr1)
        self.assertFalse(5 in arr1)

    def test_indexing(self):
        arr1 = Array([1, 2, 3])
        self.assertEqual(arr1[1], 2)
        
        
        arr2 = Array([[1, 2], [3, 4]])
        
        
        self.assertEqual(arr2[1, 1], 4)

    def test_slicing(self):
        arr1 = Array([1, 2, 3, 4, 5])
        self.assertEqual(arr1[1:4], [2, 3, 4])
        print(arr1[1:4])
        arr2 = Array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print(arr2[0:2, 1])
        self.assertEqual(arr2[0:2, 1].data, [2, 5])

if __name__ == '__main__':
    # unittest.main()
     # Pour créer une suite de test
    suite = unittest.TestLoader().loadTestsFromTestCase(TestArray)
    # Exécuter la suite en ordre
    unittest.TextTestRunner(verbosity=2).run(suite)