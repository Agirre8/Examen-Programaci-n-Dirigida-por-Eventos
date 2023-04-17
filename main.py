import threading
import random
import time

class Gasolinera:
    def __init__(self, N):
        self.surtidores = [threading.Lock() for _ in range(N)]
        self.cola = []
        self.tiempo_promedio = 0

    def repostar(self, coche):
        inicio_repostaje = time.perf_counter()
        surtidor = None

        # Buscar surtidor libre o con menos coches en la cola
        while not surtidor:
            for i, lock in enumerate(self.surtidores):
                if lock.acquire(blocking=False):
                    surtidor = i
                    break

            if surtidor is None:
                time.sleep(0.01)  # Esperar si no hay surtidores libres

        # Simular repostaje
        tiempo_repostaje = random.uniform(5, 10)
        time.sleep(tiempo_repostaje)

        # Liberar surtidor
        self.surtidores[surtidor].release()

        # Calcular tiempo de espera en la cola
        fin_repostaje = time.perf_counter()
        tiempo_espera = fin_repostaje - inicio_repostaje
        self.tiempo_promedio += tiempo_espera

        # Ponerse en cola de la caja
        self.cola.append(coche)

    def pagar(self):
        inicio_pago = time.perf_counter()

        # Simular pago
        tiempo_pago = 3
        time.sleep(tiempo_pago)

        # Sacar coche de la cola de la caja
        coche = self.cola.pop(0)

        # Calcular tiempo total en la gasolinera
        fin_pago = time.perf_counter()
        tiempo_total = fin_pago - coche.inicio_gasolinera

        print(f"El coche {coche.nombre} ha tardado {tiempo_total:.2f} segundos en la gasolinera.")

class Coche(threading.Thread):
    def __init__(self, nombre, gasolinera):
        super().__init__()
        self.nombre = nombre
        self.gasolinera = gasolinera
        self.inicio_gasolinera = None

    def run(self):
        llegada_gasolinera = time.perf_counter()

        # Simular llegada a la gasolinera
        tiempo_llegada = random.uniform(0, 15)
        time.sleep(tiempo_llegada)

        self.inicio_gasolinera = time.perf_counter()

        # Realizar repostaje
        self.gasolinera.repostar(self)

        # Realizar pago
        self.gasolinera.pagar()

if __name__ == '__main__':
    N = 1  # Número de surtidores de combustible
    gasolinera = Gasolinera(N)
    coches = []

    # Generar 50 coches
    for i in range(50):
        coche = Coche(f"Coche {i+1}", gasolinera)
        coches.append(coche)
        coche.start()

    # Esperar a que todos los coches terminen
    for coche in coches:
        coche.join()

    # Calcular tiempo promedio
    tiempo_promedio = gasolinera.tiempo_promedio / len(coches)
    
    print(f"El tiempo promedio de un coche en la gasolinera es de {time}")
