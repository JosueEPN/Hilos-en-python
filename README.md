# Hilos-en-python
### Josue Singaña
Se importan las librerias para poder realizar la ejecucion de los hilos
![image](https://user-images.githubusercontent.com/65979995/178618772-e57eb702-a190-4bc9-b6cf-207d12531f6d.png)

Se crea la instancia del segundo Hilo que se va a ejecutar en segundo plano
![image](https://user-images.githubusercontent.com/65979995/178618713-9f82f9c3-0dfb-4226-bc4d-38b9c6132522.png)

En nuestro Hilo principal creamos la intancia para que se ejecute la seccion anterior en segundo plano
![image](https://user-images.githubusercontent.com/65979995/178619102-a3f9fade-f4c4-4a4e-98b3-b98ec19cd964.png)

Se especifica cuando va iniciar y terminar la ejecucion del hilo 2, en este caso la linea de codigo  "thread.start" iniciara la ejecucion en segundo plano y el comando "thread.join()" esperara a que finalice el Hilo 2 si se quita los hilos se ejecutan a la par
![image](https://user-images.githubusercontent.com/65979995/178619691-13d95e8e-06b7-47b4-a762-c387d849be81.png)
