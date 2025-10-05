#Paso1: Crear y escribir en el archivo my_notes.txt

# Abrimos el archivo en modo escritura ('w') para crear o sobrescribir el contenido

with open("my_notes.txt", "w") as file:

    # Escribimos tres líneas de notas personales
    file.write("Hoy aprendi a trabajar con archivos de texto en Python.\n")
    file.write("Me gusta mucho como se puede automatizar la lectura y escritura.\n")
    file.write("Este conocimiento sera muy util si en el furuto me dedico a la programacion.\n")

# El archivo se cierra automáticamente al salir del bloque 'with'


#Paso2: Leer el contenido del archivo línea por línea

# Abrimos el archivo en modo lectura ('r')

with open("my_notes.txt", "r") as file:
    
    # Usamos readline() para leer línea por línea
    line = file.readline()
    while line:
        print(line.strip())  # Mostramos la línea sin saltos de línea extra
        line = file.readline()

# El archivo se cierra automáticamente al salir del bloque 'with'

