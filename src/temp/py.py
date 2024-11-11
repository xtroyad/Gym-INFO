# Nombre del archivo de entrada y salida
archivo_entrada = './myEntre.csv'
archivo_salida = './myEntre.csv'

# Leer el contenido del archivo original
with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()

# Reemplazar los caracteres ';' por ','
contenido_modificado = contenido.replace(';', ',')

# Guardar el contenido modificado en un nuevo archivo
with open(archivo_salida, 'w', encoding='utf-8') as archivo:
    archivo.write(contenido_modificado)

print(f"El archivo {archivo_entrada} ha sido procesado y guardado como {archivo_salida}.")
