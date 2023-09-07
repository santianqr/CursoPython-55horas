def my_sum(*numbers):
    """
    Función que suma los elementos que introduzcamos por parámetro
    """
    result = 0
    for n in numbers:
        result += n
  
    return result
  
def my_prod(*numbers):
    """
    Función que multiplica los elementos que introduzcamos por parámetro
    """
    result = 1
    for n in numbers:
        result *= n
  
    return result
    
def my_description():
    print("Este módulo tiene 3 funciones: ")
    print("\t- la que muestra la descripción del módulo")
    print("\t- la que suma los números que introduzcamos por parámetro")
    print("\t- la que multiplica los números que introduzcamos por parámetro")
    
sum1to10 = my_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
prod1to10 = my_prod(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)