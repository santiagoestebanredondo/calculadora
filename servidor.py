import socket

def calcular(operador, num1, num2):
    """Realiza la operación solicitada por el cliente"""
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operador == '+':
            return num1 + num2
        elif operador == '-':
            return num1 - num2
        elif operador == '*':
            return num1 * num2
        elif operador == '/':
            if num2 == 0:
                return "Error: división por cero"
            return num1 / num2
        else:
            return "Operador no válido"
    except ValueError:
        return "Error: datos no válidos"


def iniciar_servidor(host='0.0.0.0', port=5000):
    """Inicializa el servidor TCP"""
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, port))
    servidor.listen(5)

    print(f"🖥️ Servidor TCP escuchando en {host}:{port}")

    while True:
        conexion, direccion = servidor.accept()
        print(f"📡 Conexión establecida desde {direccion}")

        # Recibir los datos del cliente
        data = conexion.recv(1024).decode('utf-8')
        if not data:
            conexion.close()
            continue

        print(f"🔹 Datos recibidos: {data}")

        # Espera formato: "num1 operador num2"
        partes = data.split()
        if len(partes) == 3:
            num1, operador, num2 = partes
            resultado = calcular(operador, num1, num2)
        else:
            resultado = "Error en el formato. Use: número operador número"

        # Enviar el resultado al cliente
        conexion.send(str(resultado).encode('utf-8'))
        print(f"✅ Resultado enviado: {resultado}")

        # Cerrar la conexión
        conexion.close()
        print("🔻 Conexión cerrada.\n")


if __name__ == "__main__":
    iniciar_servidor()
