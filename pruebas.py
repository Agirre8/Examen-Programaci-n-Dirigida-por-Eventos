import threading
import random
import time

class Gasolinera:
    def __init__(self, num_surtidores):
        self.num_surtidores = num_surtidores
        self.surtidores_libres = threading.Semaphore(num_surtidores)
        self.cola_pago = threading.Condition()
        self.total_tiempo = 0
        self.num_coches = 0

    def repostar(self, coche):
        tiempo_repostaje = random.randint(5, 10)
        time.sleep(tiempo_repostaje / 100)  # Convertir a centésimas de segundo
        print(f"Coche {coche} ha repostado en {tiempo_repostaje} minutos.")
        self.pagar(coche)

    def pagar(self, coche):
        tiempo_pago = 3
        with self.cola_pago:
            self.cola_pago.wait()  # Esperar a que sea el turno del coche en la cola de pago
            time.sleep(tiempo_pago / 100)  # Convertir a centésimas de segundo
            print(f"Coche {coche} ha pagado en {tiempo_pago} minutos.")
            self.num_coches += 1
            if self.num_coches == 50:
                self.total_tiempo = time.time() - self.total_tiempo
                self.cola_pago.notify_all()  # Notificar a todos los coches que han pagado

    def calcular_tiempo_medio(self):
        return round((self.total_tiempo / 50) * 100, 2)  # Convertir a centésimas de segundo y redondear

def llegada_coches(gasolinera):
    for i in range(1, 51):  # Generar 50 coches
        tiempo_llegada = random.randint(1, 15)
        time.sleep(tiempo_llegada)
        print(f"Coche {i} ha llegado a la gasolinera en {tiempo_llegada} minutos.")
        gasolinera.surtidores_libres.acquire()
        gasolinera.total_tiempo += time.time()  # Registrar el tiempo de llegada del coche
        threading.Thread(target=gasolinera.repostar, args=(i,)).start()

def main():
    gasolinera = Gasolinera(1)  # Crear gasolinera con 1 surtidor
    llegada_coches(gasolinera)

    # Esperar a que todos los coches hayan terminado
    while gasolinera.num_coches < 50:
        pass

    # Calcular y mostrar el tiempo medio de repostaje y pago
    tiempo_medio = gasolinera.calcular_tiempo_medio()
    print(f"Tiempo medio de repostaje y pago: {tiempo_medio} minutos.")
