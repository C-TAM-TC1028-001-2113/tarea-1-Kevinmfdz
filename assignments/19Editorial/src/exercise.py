import math 
def main():
# escribe tu código abajo de esta línea  
 num_palabras = int(input("Dame el número de palabras: "))
 num_paginas = (num_palabras / 475)

 if num_palabras < 475:
    costo = 60 - (60 * 0.10)
    print("El costo de la publicación es:", costo)
 else:
    num_paginas = math.ceil (num_palabras / 475)
    costo_descuento = (num_paginas * 60) - ((num_paginas * 60) * 0.10)
    print("El costo de la publicación es:", costo_descuento)


if __name__ == '__main__':
    main()
