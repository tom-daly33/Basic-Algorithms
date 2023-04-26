class Circle():
    def __init__(self, centre : tuple, radius : float):
        self.centre = centre
        self.radius = radius

    def getArea(self):
        pi = 3.141592653589793238462
        area = (self.radius ** 2) * pi
        return area
    
    def getPerimeter(self):
        pi = 3.141592653589793238462
        perimeter = (self.radius * 2) * pi
        return perimeter

class Triangle():
    def __init__(self, vertices : list[tuple]):
        self.vertices = vertices
    
    def getLength(self, vertex1, vertex2):
        sqlength = ((vertex1[0] - vertex2[0]) ** 2) + ((vertex1[1] - vertex2[1]) ** 2)
        return abs(sqlength ** 0.5)

    def getLengths(self):

        lengthAB = self.getLength(self.vertices[0], self.vertices[1])
        lengthBC = self.getLength(self.vertices[1], self.vertices[2])
        lengthCA = self.getLength(self.vertices[2], self. vertices[0])

        return ([lengthAB, lengthBC, lengthCA])

    def getSemiPerimeter(self):
        
        lengths = self.getLengths()

        return ((lengths[0] + lengths[1] + lengths[2]) * 0.5)

    def getArea(self):
        
        lengths = self.getLengths()

        semiPerimeter = (lengths[0] + lengths[1] + lengths[2]) * 0.5

        area = (semiPerimeter * (semiPerimeter - lengths[0])
         * (semiPerimeter - lengths[1]) * (semiPerimeter - lengths[2])) ** 0.5

        return area


    def getAreaWithoutLengths(self):
        area = 0.5 * ((self.vertices[0][0] * (self.vertices[1][1] - self.vertices[2][1]))
        + (self.vertices[1][0] * (self.vertices[2][1] - self.vertices[0][1]))
        + (self.vertices[2][0] * (self.vertices[0][1] - self.vertices[1][1])))
        return abs(area)


    def getPerimeter(self):
        
        lengths = self.getLengths()

        perimeter = (lengths[0] + lengths[1] + lengths[2])

        return perimeter

    def getInscribedCircle(self):
        
        semiPerimeter = self.getSemiPerimeter()
        area = self.getArea()
        circleRadius = area / semiPerimeter

        lengths = self.getLengths()

        circleCentre = ((((lengths[1]*self.vertices[0][0])+(lengths[2]*self.vertices[1][0])
                        +(lengths[0]*self.vertices[2][0])) / sum(lengths)) , 
                        ((((lengths[1]*self.vertices[0][1])+(lengths[2]*self.vertices[1][1])
                        +(lengths[0]*self.vertices[2][1]))) / sum(lengths)))

        inscribedCircle = Circle(circleCentre, circleRadius)
        return inscribedCircle

    def getCicumcenter(self):

        def Cicumcenterhelp(mode,a,b,c):
            if mode == "x":
                return (((a[0] ** 2) + (a[1] ** 2)) * (b[1] - c[1]))
            elif mode == "y":
                return (((a[0] ** 2) + (a[1] ** 2)) * (c[0] - b[0]))


        
        a = self.vertices[0]
        b = self.vertices[1]
        c = self.vertices[2]

        d = 2 * ((a[0] * (b[1] - c[1])) + 
                (b[0] * (c[1] - a[1])) + (c[0] * (a[1] - b[1])))

        u_x = (( Cicumcenterhelp("x",a,b,c) +
                 Cicumcenterhelp("x",b,c,a) + Cicumcenterhelp("x",c,a,b))
                  / d)

        u_y = (( Cicumcenterhelp("y",a,b,c) +
                 Cicumcenterhelp("y",b,c,a) + Cicumcenterhelp("y",c,a,b))
                 / d)

        return (u_x, u_y)



    def getCircumscribedCircle(self):
        
        lengths = self.getLengths()

        area = self.getArea()

        circleRadius = (lengths[0]*lengths[1]*lengths[2]) / (4 * area)

        circleCentre = self.getCicumcenter()

        cicumscribedCicle = Circle(circleCentre, circleRadius)
        return cicumscribedCicle

tri1 = Triangle([(0,0),(0,1),(1,0)])
insCircle = tri1.getInscribedCircle()
cirCircle = tri1.getCircumscribedCircle()

print(f"tri1 Inscribed Circle : {insCircle.centre}, {insCircle.radius} ")

print(f"tri1 Circumscribed Circle : {cirCircle.centre}, {cirCircle.radius} ")#
