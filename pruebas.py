

"""
Definir constantes:
- T como el tiempo máximo de llegada de coches en minutos
- N como el número de surtidores de combustible
- TOTAL_COCHES como la cantidad total de coches a simular

Definir variables:
- colaCoches como una cola vacía para almacenar los coches en espera
- surtidores como un arreglo de N surtidores de combustible inicialmente libres
- tiempoTotal como la suma acumulada de tiempo de espera de todos los coches
- cochesGenerados como un contador de la cantidad de coches generados

Definir clase Coche:
- tiempoLlegada como el tiempo en que el coche llega a la gasolinera
- tiempoRepostaje como el tiempo que el coche tarda en repostar
- tiempoPago como el tiempo que el coche tarda en realizar el pago

Definir función llegadaCoche():
- Generar un nuevo coche con tiempoLlegada aleatorio entre 0 y T minutos
- Añadir el coche a la colaCoches

Definir función repostaje(coche):
- Elegir un surtidor libre o con la menor cantidad de coches en cola
- Marcar el surtidor como ocupado
- Esperar tiempoRepostaje aleatorio entre 5 y 10 minutos
- Marcar el surtidor como libre

Definir función pago(coche):
- Esperar tiempoPago de 3 minutos

Inicio del programa:
- Generar 50 coches utilizando la función llegadaCoche()
- Mientras haya coches en la colaCoches o cochesGenerados < TOTAL_COCHES:
  - Si hay surtidores libres y coches en la colaCoches:
    - Sacar un coche de la colaCoches
    - Llamar a la función repostaje(coche) para que el coche reposte en un surtidor
  - Llamar a la función pago(coche) para que el coche realice el pago después del repostaje
  - Actualizar el tiempoTotal con el tiempo de espera del coche
  - Incrementar el contador de cochesGenerados
- Calcular el tiempo promedio de espera dividiendo el tiempoTotal entre el total de coches generados
- Mostrar el tiempo promedio de espera en la gasolinera
"""