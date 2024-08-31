base = int(input("Ingrese la medida de la base: "))
altura = int(input("Ingrese la altura: "))

def calcular_area(a = int, b = int):
     if a > 0 and b > 0:
        area = a * b
        print(f"El area del trinagulo es: {area} ")

     else:
        print("Ingrese un número mayor que cero: ")

calcular_area(base,altura)


