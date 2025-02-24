import socket
import threading
import tkinter as tk
from tkinter import messagebox

#Clase del servidor
class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 12345))  #Dirección y puerto del servidor
        self.server_socket.listen(5)  #El servidor solamente puede aceptar 5 clientes a la vez
        self.clients = []  #Lista para guardar los sockets de los clientes
        self.gui = self.create_gui()

    def create_gui(self):
        window = tk.Tk()
        window.title("Servidor")
        window.geometry("400x300")

        self.client_listbox = tk.Listbox(window, width=50, height=10)
        self.client_listbox.pack(padx=10, pady=10)

        self.text_display = tk.Text(window, width=50, height=10)
        self.text_display.pack(padx=10, pady=10)
        
        self.text_display.insert(tk.END, "Esperando conexiones...\n")
        
        threading.Thread(target=self.accept_clients, daemon=True).start()
        return window

    def accept_clients(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            self.clients.append(client_socket)
            self.client_listbox.insert(tk.END, f"Cliente {client_address}")
            threading.Thread(target=self.handle_client, args=(client_socket, client_address), daemon=True).start()

    def handle_client(self, client_socket, client_address):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    self.broadcast_message(message, client_address)
                else:
                    break
            except:
                break

        self.clients.remove(client_socket)
        self.client_listbox.delete(self.client_listbox.get(0, tk.END).index(f"Cliente {client_address}"))
        client_socket.close()

    def broadcast_message(self, message, client_address):
        self.text_display.insert(tk.END, f"Mensaje de {client_address}: {message}\n")
        self.text_display.yview(tk.END)
        for client in self.clients:
            try:
                client.send(f"{client_address}: {message}".encode('utf-8'))
            except:
                pass

    def run(self):
        self.gui.mainloop()

#Ejecución del servidor
if __name__ == "__main__":
    server = Server()
    server.run()
