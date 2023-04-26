class Vector():

    def __init__(self, *vector : list[float]):
        if len(vector) > 1:
            listed_vector = []
            for i in vector:
                listed_vector.append(i) 
            self._vector = listed_vector
        elif vector == ():
            self._vector = []
        else:
            vector = vector[0]
            self._vector = vector[:]

    def __str__(self):
        string = "<"
        if self._vector == []:
            return ("<>")
        for i in range(len(self._vector) - 1):
            string = string + f"{float(self._vector[i])}, "
        string = string + f"{float(self._vector[len(self._vector) - 1])}>"
        return(string)

    def __getitem__(self, index : int):
        return self.get(index)

    def __setitem__(self, index : int, value : int):
        self.set(index, value)

    def __eq__(self, other_vector):
        try:
            returning = self.equals(other_vector)
        except TypeError:
            return False
        return returning

    def __ne__(self, other_vector):
        if self.__eq__(other_vector):
            return False
        return True

    def __add__(self, other_vector):
        return(self.add(other_vector))

    def __iadd__(self, other_vector):
        return(self.__add__(other_vector))

    def __mul__(self):
        raise TypeError

    def __rmul__(self, scalar : float):
        return (self.scalar_product(scalar))

    def __imul__(self, scalar : float):
        if not isinstance(scalar, int):
            raise TypeError
        return (self.__rmul__(scalar))

    def dim(self):
        return len(self._vector)

    def get(self, index : int):
        return self._vector[index]

    def set(self, index : int, value : int):
        self._vector[index] = value

    def scalar_product(self, scalar : float):

        if self._vector == []:
            return Vector()
        new_vector = Vector([(self._vector[0]*scalar),
                     (self._vector[1]*scalar), (self._vector[2]*scalar)])
        return new_vector
    
    def add(self, other_vector):
        if isinstance(other_vector, Vector) == False:
            raise TypeError
        if self.dim() != other_vector.dim():
            raise ValueError
        new_vector = Vector([(self._vector[0] + other_vector._vector[0]),
                            (self._vector[1] + other_vector._vector[1]),
                            (self._vector[2] + other_vector._vector[2]),])
        return new_vector
    
    def equals(self, other_vector):
        if isinstance(other_vector, Vector) == False:
            raise TypeError
        if len(self._vector) != len(other_vector._vector):
            return False
        for i in range(len(self._vector)):
            if self._vector[i] != other_vector._vector[i]:
                return False
        return True

def __main__():
    
    return ("pass")

__main__()