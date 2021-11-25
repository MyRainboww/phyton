i = 0
"""while i <= 10:
    print(i)
    i += 1"""

"""list = [1,2,3,4,5,6,7,True]
while i < len(list):
    print(list[i])
    i += 1"""

"""while input("Stop?").lower() != "stop":
    print(i)
    i += 1"""
    
"""lista vacia en un inicio, 
tiene que ir guardando del 1 al 10"""

list = []
flag = False
while flag == False:
    list.append(input("Ingresa el valor (n para detener)").lower())
    print(list)
    if list[i] == "n":
        flag = True
    i += 1