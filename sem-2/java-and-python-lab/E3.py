"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Java and Python Lab.
* Lab Experiment 3 - Write a class QuadraticEquationSolver which would have method findRoot to identify
roots of quadratic equation. Quadratic equations take a form of ax2(square)+bx+c=0
Formula to identify roots of quadratic equation. findRoots method would accept coefficients of quadratic equation (i.e. values of a, b & c) and return both roots.
"""

class QuadraticEquationSolver:

    def findRoot(a: int, b: int, c: int):
        if a == 0:
            raise ValueError("Not a valid quadratic equation.")

        det = (b ** 2) - (4 * a * c)

        if det < 0:
            raise ValueError("Real roots do not exist.")

        x1 = (-b - det ** 0.5) / (2 * a)
        x2 = (-b + det ** 0.5) / (2 * a)

        return (x1, x2)


if __name__ == "__main__":
    a, b, c = list(map(int, input('Enter the values of a, b and c separated by spaces: ').split(' ')))
    print(f'\nThe roots of the quadratic equation ax^2 + bx + c where a = {a}, b = {b} and c = {c} are: \n{QuadraticEquationSolver.findRoot(a, b, c)}')