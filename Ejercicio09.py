import time
import random
import threading
import asyncio
import multiprocessing

consultas = [random.randint(1, 5) for _ in range(3)] 

print(f"Tiempos de respuesta (simulados) para 3 consultas: {consultas} segundos")

def simular_consulta_hilo(consulta_id, tiempo):
    """Función que simula una consulta con tiempo de espera."""
    print(f"[Hilo {consulta_id}] Iniciando consulta. Tiempo estimado: {tiempo}s")
    time.sleep(tiempo)
    print(f"[Hilo {consulta_id}] Finalizó la consulta.")

def ejecutar_hilos():
    print("\nEJECUCIÓN CON HILOS (Threading)")
    inicio = time.time()
    hilos = []
    
    for i, t in enumerate(consultas):
        h = threading.Thread(target=simular_consulta_hilo, args=(i+1, t))
        hilos.append(h)
        h.start()
    
    for h in hilos:
        h.join() 
        
    tiempo_total = time.time() - inicio
    print(f"Tiempo total con Hilos: {tiempo_total:.2f} segundos")

async def simular_consulta_asyncio(consulta_id, tiempo):
    """Función que simula una consulta usando Asyncio."""
    print(f"[Asyncio {consulta_id}] Iniciando consulta. Tiempo estimado: {tiempo}s")
    await asyncio.sleep(tiempo)
    print(f"[Asyncio {consulta_id}] Finalizó la consulta.")

async def ejecutar_asyncio():
    print("\nEJECUCIÓN CON ASYNCIO")
    inicio = time.time()
    
    tareas = [simular_consulta_asyncio(i+1, t) for i, t in enumerate(consultas)]
    
    await asyncio.gather(*tareas) 
    
    tiempo_total = time.time() - inicio
    print(f"Tiempo total con Asyncio: {tiempo_total:.2f} segundos")

def simular_consulta_proceso(consulta_id, tiempo):
    """Función que simula una consulta con tiempo de espera."""
    print(f"[Proceso {consulta_id}] Iniciando consulta. Tiempo estimado: {tiempo}s")
    time.sleep(tiempo)
    print(f"[Proceso {consulta_id}] Finalizó la consulta.")

def ejecutar_procesos():
    print("\nEJECUCIÓN CON PROCESOS (Multiprocessing)")
    inicio = time.time()
    procesos = []
    
    for i, t in enumerate(consultas):
        p = multiprocessing.Process(target=simular_consulta_proceso, args=(i+1, t))
        procesos.append(p)
        p.start()
    
    for p in procesos:
        p.join() 
        
    tiempo_total = time.time() - inicio
    print(f"Tiempo total con Procesos: {tiempo_total:.2f} segundos")

if __name__ == "__main__":
    ejecutar_hilos()
    
    asyncio.run(ejecutar_asyncio()) 
    
    ejecutar_procesos()
