try:
    with open("origen.txt", "w") as f:
        f.write("Esta es la línea 1.\n")
        f.write("Esta es la línea 2.\n")

    datos_binarios = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
    with open("origen.bin", "wb") as f:
        f.write(datos_binarios)
except Exception as e:
    print(f"Error al crear archivos de prueba: {e}")

def copiar_archivo_texto(origen, destino):
    """Copia el contenido de un archivo de texto a otro."""
    try:
        with open(origen, "r") as f_origen:
            contenido = f_origen.read() 
        
        with open(destino, "w") as f_destino:
            f_destino.write(contenido) 
        
        print(f"Copia de texto exitosa: '{origen}' -> '{destino}'")
    except FileNotFoundError:
        print(f"Error: El archivo de origen '{origen}' no fue encontrado.")
    except Exception as e:
        print(f"Error al copiar archivo de texto: {e}")

def copiar_archivo_binario(origen, destino):
    """Copia el contenido de un archivo binario a otro."""
    try:
        with open(origen, "rb") as f_origen:
            data = f_origen.read() 
        
        with open(destino, "wb") as f_destino:
            f_destino.write(data) 
            
        print(f"Copia binaria exitosa: '{origen}' -> '{destino}'")
    except FileNotFoundError:
        print(f"Error: El archivo de origen '{origen}' no fue encontrado.")
    except Exception as e:
        print(f"Error al copiar archivo binario: {e}")

print("\nPRUEBAS DE COPIA DE ARCHIVOS")
copiar_archivo_texto("origen.txt", "destino.txt")
copiar_archivo_binario("origen.bin", "destino.bin")

with open("destino.txt", "r") as f:
    print("\nContenido de destino.txt:")
    print(f.read())