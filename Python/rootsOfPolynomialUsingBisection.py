class RootsOfPolynomialUsingBisection:
    def __init__(self, polynomial_as_function):
        self.polynomial = polynomial_as_function
        self.a=[]
        self.b=[]
        self.num_iterations = 0
    def _is_positive(self, num):
        return num > 0
    def _is_negative(self, num):
        return num < 0
    def get_roots(self, a, b, tolerance):
        if (self._is_positive(self.polynomial(a)) and self._is_negative(self.polynomial(b))) or (self._is_positive(self.polynomial(b)) and self._is_negative(self.polynomial(a))):
            pass
        else:
            raise ValueError("The given interval does not contain a root")
        self.a.append(a)
        self.b.append(b)
        self.num_iterations += 1
        while True:
            value_by_a=self.polynomial(a)
            value_by_b=self.polynomial(b)
            if abs(value_by_a) <= tolerance:
                return [a,value_by_a]
            if abs(value_by_b) <= tolerance:
                return [b,value_by_b]
            negative_sider= a if value_by_a < 0 else b
            positive_sider= a if value_by_a > 0 else b
            bisection_point = (negative_sider + positive_sider) / 2
            value_by_bisection_point = self.polynomial(bisection_point)
            if abs(value_by_bisection_point) <= tolerance:
                return [bisection_point,value_by_bisection_point]
            if value_by_bisection_point < 0:
                negative_sider= bisection_point
            else:
                positive_sider= bisection_point
            a=negative_sider
            b=positive_sider
            self.num_iterations += 1
            self.a.append(a)
            self.b.append(b)
def polynomial_as_function(x):
    return x**3 - 3*x - 5
rootFinder = RootsOfPolynomialUsingBisection(polynomial_as_function)
root_and_value=rootFinder.get_roots(2,3, 0.0022)
print("Root: ", root_and_value[0])
print("Value at root: ", root_and_value[1])
print("All values of a taken: ", rootFinder.a)
print("All values of b taken: ", rootFinder.b)
print("Number of iterations: ", rootFinder.num_iterations)
