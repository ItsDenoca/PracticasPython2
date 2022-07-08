print(f"Proporciona los siguientes datos del libro: ")
nombre = input("Proporciona el nombre del libro: ")
id = int(input("Proporciona el id del libro: "))
precio = float(input("Proporciona el coste del libro: "))
envio_gratuito = (input("Indica si es envio gratuito (True/False): "))

if envio_gratuito == "True":
    envio_gratuito = True
elif envio_gratuito == "False":
    envio_gratuito = False
else:
    envio_gratuito = "Valor incorrecto, debe escribir True/False"

print(f'''
Nombre: {nombre}
ID: {id}
Precio: {precio}
¿Cuenta con envio gratuito?: {envio_gratuito}
''')

