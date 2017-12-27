def py_function(x):
    """
    :param x: An integer
    :return: x to the power of 2
    """
    if x == 0:
        return 100
    return x**2


class PyClass():

    counter = 0

    def __init__(self):
        self.id = self.counter
        self.counter += 1

    def get_id(self):
        return self.id

    def unstable_method(self):
        pass