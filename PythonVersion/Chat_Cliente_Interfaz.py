import socket
import threading
import tkinter as tk
from tkinter import simpledialog

#Clase del cliente
class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 12345)) #Socket de conexión para el cliente
        
        self.nombre_usuario = self.pedir_nombre()
        self.send_message(f"{self.nombre_usuario} se ha unido al chat")

        self.gui = self.create_gui()

        threading.Thread(target=self.receive_messages, daemon=True).start()

    def pedir_nombre(self):
        ventana_nombre = tk.Tk()
        ventana_nombre.withdraw()
        nombre = simpledialog.askstring("Nombre", "Ingrese su nombre: ")
        return nombre if nombre else "Usuario anonimo"

    def create_gui(self):
        window = tk.Tk()
        window.title(f"Chat de {self.nombre_usuario}")
        window.geometry("400x350")

        etiqueta_usuario = tk.Label(window, text=f"Bienvenido, {self.nombre_usuario}", font=("Arial", 12, "bold"))
        etiqueta_usuario.pack(pady=5)

        self.text_display = tk.Text(window, width=50, height=10, state=tk.DISABLED)
        self.text_display.pack(padx=10, pady=10)

        self.message_entry = tk.Entry(window, width=40)
        self.message_entry.pack(padx=10, pady=10)

        send_button = tk.Button(window, text="Enviar", command=self.send_message_from_entry)
        send_button.pack(padx=10, pady=10)

        return window

    def send_message(self, message):
        if message:
            try:
                self.client_socket.send(message.encode('utf-8'))
            except:
                print("Error al enviar mensaje.")
    
    def send_message_from_entry(self):
        message = self.message_entry.get()
        if message:
            self.send_message(f"{self.nombre_usuario}: {message}")
            self.message_entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.text_display.config(state=tk.NORMAL)
                    self.text_display.insert(tk.END, f"{message}\n")
                    self.text_display.config(state=tk.DISABLED)
                    self.text_display.yview(tk.END)
            except:
                print("Error al recibir mensajes.")
                break
    
    def run(self):
        self.gui.mainloop()

#Ejecución del cliente
if __name__ == "__main__":
    client = Client()
    client.run()