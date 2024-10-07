Lo ideal sería que hiciera un escaneo cada cierto tiempo y que asi estuviera siempre organizado

En segundo plano (Windows): start /B python /dir/scripts/organizar_descargas.py
Si se reinicia el PC se desactiva.


Se puede programar las tareas de windows.

Pasos:
Abre el Programador de Tareas:

Escribe "Programador de tareas" en la barra de búsqueda de Windows y ábrelo.
Crea una tarea básica:

Haz clic en "Crear tarea" en el panel derecho.
En la pestaña "General", ponle un nombre (por ejemplo, "Organizar Descargas").
Establece un desencadenador:

Ve a la pestaña "Desencadenadores" y haz clic en "Nuevo".
Establece la frecuencia con la que deseas que se ejecute el script (por ejemplo, cada hora).
Establece la acción:

Ve a la pestaña "Acciones" y haz clic en "Nuevo".
En "Acción", selecciona "Iniciar un programa".
En "Programa/script", escribe el camino a python.exe (por ejemplo, C:\Python39\python.exe).
En "Agregar argumentos (opcional)", añade el camino a tu script, por ejemplo: /dir/scripts/organizar_descargas.py


Y la opción ideal sería con un demonio (Linux) o servicio (Windows). En resumen, monitorear la carpeta de Descargas en busca de cambios.