# Tópicos-para-el-Despliegue-de-Aplicaciones

### Instrucciones para ejecutar los archivos de pyhton correctamente

1. Abrir una nueva terminal de python en la parte superior donde dice **Terminal**, luego en **New Terminal**.
<img width="273" alt="Image" src="https://github.com/user-attachments/assets/1d7f1e0a-bd99-4a1a-8f2a-14ca7657947d" />

2. En seguida lo llevará al directoria de donde se esta ejecutando, sin embargo los codigo de python no esta guardados es este directorio, por lo que tendremos que navegar usando:
```
cd PythonVersion/
```
Y de esta forma llegamos al directorio de PythonVersion/.

<img width="384" alt="Image" src="https://github.com/user-attachments/assets/8d438611-ee57-40a8-ba59-c1cb1a2232f7" />

3. Después selecionamos la opción de **Split Terminal** para copiar las instrucciones ejecutadas, ya que una servirá para el servidor y el otro para el cliente, justo como aparece en las imagenes:

<img width="307" alt="Image" src="https://github.com/user-attachments/assets/95268cf1-0d4b-4f28-8693-8e4eed0879d6" />

<img width="914" alt="Image" src="https://github.com/user-attachments/assets/f91da4f3-5eb8-49e8-9b65-671025a74355" />

4. Luego tendremos que escribir el siguiente comando para ejecutar los archivos de python:
```
#En la pestaña del servidor
python3 Chat_Servidor_Interfaz.py #(esto en el caso de usar Mac, de lo contrario omita el número 3)
#En la pestaña del cliente
python3 Chat_Cliente_Interfaz.py #(esto en el caso de usar Mac, de lo contrario omita el número 3)
```

5. Por último presionamos **enter** en las dos pestañas para correr los códigos, y automaticamente se mostrarán las interfaces del servidor y del cliente, justo como se muestra en las imagenes:

<img width="280" alt="Image" src="https://github.com/user-attachments/assets/ffebd02e-449e-4f02-b967-52bb1144379a" />

<img width="403" alt="Image" src="https://github.com/user-attachments/assets/fc28571d-1964-46f2-9cad-b360a87edd5e" />

Y esto seria todo, ya se podria enviar mensajes y conectar a varios clientes (recordando que solo tiene un limite de 5 clientes conectados simultáneamente).
