class RootsOfPolynomialUsingBisection:
    def __init__(self, polynomial_as_function):
        self.polynomial = polynomial_as_function
        self.a_history=[]
        self.b_history=[]
        self.num_iterations = 0
    def get_roots(self, a, b, tolerance=0.001):
        tolerance = abs(tolerance)
        root_lies_between = [a,b]
        try:
            a=list(filter(lambda x: self.polynomial(x)<0, root_lies_between))[0] # this is to filter the value of x from give roots for which the function returns a negative number
            b=list(filter(lambda x: self.polynomial(x)>0, root_lies_between))[0] # this is to filter the value of x from give roots for which the function returns a positive number
        except IndexError:
            raise ValueError("The given interval does not contain a root")
        self.a_history.append(a)
        self.b_history.append(b)
        if abs(a-b) <= tolerance:
            return [(a+b)/2, self.polynomial((a+b)/2)]
        while (abs(a-b)>tolerance):
            self.num_iterations+=1
            bisection=(a+b)/2
            f_bisection=self.polynomial(bisection)
            if f_bisection == 0:
                return [bisection, f_bisection]
            if f_bisection > 0:
                b=bisection
            self.b_history.append(b)
            if f_bisection < 0:
                a=bisection
            self.a_history.append(a)
        self.num_iterations+=1
        return [(a+b)/2, self.polynomial((a+b)/2)]
def polynomial_as_function(x):
    return x**3 - 3*x - 5
rootFinder = RootsOfPolynomialUsingBisection(polynomial_as_function)
root_and_value=rootFinder.get_roots(2, 3, 0.0022)
print("Root: ", root_and_value[0])
print("Value at root: ", root_and_value[1])
print("All values of a taken: ", rootFinder.a_history)
print("All values of b taken: ", rootFinder.b_history)
print("Number of iterations/bisection: ", rootFinder.num_iterations)
