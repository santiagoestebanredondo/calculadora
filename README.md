Servidor
el archivo servidor.py crea un socket TCP y se asocia a una dirreccion y puerto
el cual por defecto es el 50000, se mantiene mientras este ejecutandoce las conexiones
de los clientes.Cuando un cliente se conceta realiza lo siguiente:
-recibe los datos enviados (dos numeros y un operador).
-Realiza la operacion matematica correspondiente.
-envia el resultado de vuelta al cliente.
por ultimo cierra la conexion con ese cliente y queda disponible para nuevas solicitudes.

Cliente
lo primero que hace es solicitarle al usuario la ip del servidor luego pide los 
2 numeros y el operador para poder realizar la operacion, se conceta al servidor 
a traves de TCP usando la ip del servidor y el puerto. envia los datos al servidor,
espera la respuesta con el resultado, muestra el resultado en pantalla y finaliza 
la conexion.
