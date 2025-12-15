class OperadorInvalidoError(Exception):
    """Excepción lanzada cuando el operador de la operación no es válido."""
    def __init__(self, operador):
        self.operador = operador
        super().__init__(f"El operador '{operador}' es inválido. Los operadores permitidos son: + - * /")

def calculadora_string(operacion_str):
    """
    Procesa un string de operación (ej: "10/2"), realiza el cálculo
    y maneja las excepciones.
    """
    operadores_validos = ['+', '-', '*', '/']
    
    try:
        operador = None
        for op in operadores_validos:
            if op in operacion_str:
                operador = op
                break
        
        if operador is None:
            raise OperadorInvalidoError("No se pudo identificar el operador")
        
        partes = operacion_str.split(operador, 1)
        if len(partes) != 2:
            raise ValueError("Formato de operación incorrecto. Debe ser 'numero1 operador numero2'.")

        numero1_str, numero2_str = partes
        try:
            numero1 = float(numero1_str.strip())
            numero2 = float(numero2_str.strip())
        except ValueError:
            raise ValueError("Uno o ambos números ingresados son inválidos.")
            
        resultado = None

        if operador == '+':
            resultado = numero1 + numero2
        elif operador == '-':
            resultado = numero1 - numero2
        elif operador == '*':
            resultado = numero1 * numero2
        elif operador == '/':
            if numero2 == 0:
                raise ZeroDivisionError()
            resultado = numero1 / numero2
        else:
            raise OperadorInvalidoError(operador)


        print(f"Resultado de '{operacion_str}': {resultado:.2f}")

    except ZeroDivisionError:
        print("Error personalizado: No se puede dividir entre cero.")
    except ValueError as e:
        print(f"Error de valores inválidos: {e}")
    except OperadorInvalidoError as e:
        print(f"Error de operador inválido: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

print("PRUEBAS DE LA CALCULADORA")
calculadora_string("10/2") 
calculadora_string("5 * 4.5")
calculadora_string("10/0")
calculadora_string("a + 5") 
calculadora_string("10 $ 5") 
calculadora_string("20+3")