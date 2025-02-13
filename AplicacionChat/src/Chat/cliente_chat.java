package Chat;

import java.io.*;
import java.net.*;

public class cliente_chat {

    public static void main(String[] args) {
        String host = "127.0.0.1";
        int puerto = 12345;
        
        try{
            //Conectar al servidor
            Socket socket = new Socket(host, puerto);
            
            // Crear objetos para leer y escribir datos
            BufferedReader entrada = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter salida = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader teclado = new BufferedReader(new InputStreamReader(System.in));
            
            // Leer y mostrar el mensaje del servidor
            String mensajeServidor = entrada.readLine();
            System.out.println(mensajeServidor);
            
            // Intercambiamos mensajes 
            String mensajeCliente = "";
            while (true){
                // Leer mensaje del usuario
                System.out.println("Tu: ");
                mensajeCliente = teclado.readLine();
                
                // Enviar mensaje al servidor
                salida.println(mensajeCliente);
                
                // Si el cliente escribe "exit", se cerrará la conexión
                if (mensajeCliente.equalsIgnoreCase("exit")){
                    break;
                }
                
                // Recibir y mostrar mensaje del servidor
                String mensajeServidorRecibido = entrada.readLine();
                System.out.println("Servidor: "+mensajeServidorRecibido);
            }
            
            entrada.close();
            salida.close();
            teclado.close();
            socket.close();
            
        } catch (IOException ex){
            ex.printStackTrace();
        }
    }
    
}
