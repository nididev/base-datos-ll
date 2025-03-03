nombre = input("Escribe tu nombre: ")


precio_taco_maiz = 35.0
precio_taco_harina = 45.0
precio_bebida = 20.0

def promocion(total):
    descuento = 0.0
    if total > 250:
        descuento = total * 0.2
        print(f"\nTe descontaremos ${descuento}")
    elif total > 150:
        descuento = total * 0.1
        print(f"\nTe descontaremos ${descuento}")
    return total - descuento

tacos_maiz = int(input("Cuantos tacos de maiz quieres? "))
tacos_harina = int(input("Cuantos tacos de harina quieres? "))
bebidas = int(input("Cuantos bebidas quieres? "))

total_maiz = precio_taco_maiz * tacos_maiz
total_harina = precio_taco_harina * tacos_harina
total_bebida = precio_bebida * bebidas
total = total_maiz + total_harina + total_bebida

total = promocion(total)

print("\n")

if total > 0:
    if tacos_maiz:
        print(f"Tacos de maiz: \t\t{tacos_maiz} \t{total_maiz}")
    if tacos_harina:
        print(f"Tacos de harina: \t{tacos_harina} \t{total_harina}")
    if bebidas:
        print(f"Bebidas: \t\t{bebidas} \t{total_bebida}")

    print(f"Total: \t{total_bebida+total_harina+total_maiz}")
else:
    print("\nEntonces pa que vienes??")

print(f"Hola  {nombre}")