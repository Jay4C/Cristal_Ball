import unittest
import pymatrices as pm

# https://github.com/M-Kalanithi-14/PyMatrices


class UnitTestsMatrices(unittest.TestCase):
    # ok
    def test_Basic_operations(self):
        print('test_Basic_operations')

        M1 = pm.matrix([[1, -1, 3], [4, 5, 6], [7, 8, 9]])
        M2 = pm.matrix([[1, 2], [3, 4]])
        M3 = pm.I(3)

        print("M1 :\n", M1, sep="")
        print("M2 :\n", M2, sep="")
        print("M3 :\n", M3, sep="")

        print("Transpose of M1 :\n", M1.transpose, sep="")
        print("Transpose of M2 :\n", M2.transpose, sep="")
        print("Transpose of M3 :\n", M3.transpose, sep="")

        print("M1+M3 :\n", M1 + M3, sep="")
        print("M1-M3 :\n", M1 - M3, sep="")

        print("M1*M3 :\n", M1 * M3, sep="")
        print("M1*3 :\n", M3 * 3, sep="")

        print("\nM1[1][1] :", M1.valueAt(1, 1))
        print("M1[1][2] :", M1.valueAt(1, 2))

        print("\nMinor of 1 in M1:\n", M1.minorOfValueAt(1, 1), sep="")
        print("Minor of 2 in M1 :\n", M1.minorOfValueAt(2, 2), sep="")

        print("\nadj M1 :\n", pm.adjoint(M1), sep="")
        print("adj M2 :\n", pm.adjoint(M2), sep="")

        print("Matrix created by Filling a particular value :\n", pm.createByFilling(2, (2, 3)), sep="")

        print("A Sample Column Matrix :\n", pm.createColumnMatrix([2, 3, 4, 5]), sep="")

        print("A Sample Row Matrix :\n", pm.createRowMatrix([2, 3, 4, 5]), sep="")

        print("|M1| :", pm.determinant(M1))
        print("|M2| :", pm.determinant(M2))

        print("\nEigenvalues of M1 :", pm.eigenvalues(M1))
        print("Eigenvalues of M2 :", pm.eigenvalues(M2))

        print("\nInverse of M1 :\n", pm.inverse(M1), sep="")
        print("Inverse of M1 :\n", pm.inverse(M2), sep="")

        print("A 3x3 Identity Matrix :\n", pm.I(3), sep="")

        print("Is M1 a Diagonal Matrix? ", pm.isDiagonal(M1), sep="")
        print("Is M1 a Scalar Matrix? ", pm.isScalar(M1), sep="")
        print("Is M1 a Singular Matrix? ", pm.isSingular(M1), sep="")
        print("Is M1 a Square Matrix? ", pm.isSquare(M1), sep="")
        print("Is M1 a Symmetric Matrix? ", pm.isSymmetric(M1), sep="")
        print("Is M1 a Skew Symmetric Matrix? ", pm.isSkewSymmetric(M1), sep="")
        print("Is M1 a Identity Matrix? ", pm.isIdentity(M1), sep="")


if __name__ == '__main__':
    unittest.main()
