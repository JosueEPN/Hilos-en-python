from concurrent.futures import thread
import threading
import time
# funcion que se ejecutara en segundo plano


def Hilo2(id):
    print("Hola Soy el hilo 2, se empezo esta tarea 2, en 10 segundo acabo mi ejecucion\n")
    time.sleep(10)


if _name_ == '_main_':
    # se especifica que codigo se ejecuta en segundo plano, en este caso el HILO 2
    thread = threading.Thread(target=Hilo2, args=("2"))
    print("Hola soy el Hilo principal. En dos segundo empieza a ejecutarse el Hilo 2")
    time.sleep(2)
    thread.start()  # Inicia la ejecucion del codigo en segundo plano,
    thread.join()  # Espera que finalice la ejecucion en segundo plano para continuar la ejecucion en el plano principal, si se retira se ejecuta los dos hilos a las par

    print("Finalizo la ejecucion del Hilo 2")
