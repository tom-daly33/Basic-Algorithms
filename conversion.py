import math

def kmToM(km):
    return(km * 1000)
def mToKm(m):
    return(m * 0.001)

def kmToMi(km):
    return(km * 0.62)
def miToKm(mi):
    return(mi * 1.609344)

def mToFe(m):
    return(m * 3.28)
def feToM(fe):
    return(fe * 0.3048)

def kgToPo(kg):
    return(kg * 2.2046)
def poToKg(po):
    return(po * 0.454)


def kgToPoundsAndStones(kg):
    totalPounds = kgToPo(kg)
    pounds = (totalPounds % 14)
    stones = math.floor((totalPounds / 14))
    return(stones, pounds)

def poundsAndStonesToKg(stones, pounds):
    totalPounds = (stones * 14) + pounds
    return (poToKg(totalPounds))



print(kgToPoundsAndStones(int(input(">> "))))

print(poundsAndStonesToKg(int(input(">> ")), int(input(">> "))), "kg")

    
