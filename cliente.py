import socket

def cliente_calculadora(host='127.0.0.1', port=5000):
    """Cliente TCP que se conecta al servidor y envía una operación"""
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect((host, port))
        print(f"🔗 Conectado al servidor {host}:{port}")

        # Solicitar datos al usuario
        num1 = input("Ingrese el primer número: ")
        operador = input("Ingrese la operación (+, -, *, /): ")
        num2 = input("Ingrese el segundo número: ")

        mensaje = f"{num1} {operador} {num2}"
        cliente.send(mensaje.encode('utf-8'))

        # Recibir resultado
        resultado = cliente.recv(1024).decode('utf-8')
        print(f"🧮 Resultado recibido del servidor: {resultado}")

    except ConnectionRefusedError:
        print("❌ No se pudo conectar al servidor. Verifique la IP y el puerto.")
    finally:
        cliente.close()
        print("🔻 Conexión cerrada.")


if __name__ == "__main__":
    host = input("Ingrese la IP del servidor: ") or "127.0.0.1"
    cliente_calculadora(host)
