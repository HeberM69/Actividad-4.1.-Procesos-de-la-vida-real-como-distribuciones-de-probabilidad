# Actividad-4.1.-Procesos-de-la-vida-real-como-distribuciones-de-probabilidad

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## ¿Cómo correr el código?

### Verificar que python y pip estén instalados
<br>python --version
<br>pip --version

### Crear entorno
python -m venv env<br>
source env/bin/activate  # En macOS/Linux<br>
env\Scripts\activate     # En Windows

### Instalar dependencias
pip install numpy matplotlib fitter

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Análisis de la Duración de Canciones en una Playlist de Spotify

### 1. Selección del proceso o fenómeno
Para este análisis, se ha seleccionado la duración de canciones en una playlist de Spotify con 10 canciones. Esto es un fenómeno común en el día a día y puede ayudar a entender la distribución de las duraciones en una colección de música.

### 2. Atributo medido
El atributo analizado es la duración de cada canción en segundos.

### 3. Observaciones y recolección de datos
Se tomó una muestra de 10 canciones de una playlist de Spotify y se registraron sus duraciones en segundos.

<img width="521" alt="Captura de pantalla 2025-04-01 a la(s) 11 11 19" src="https://github.com/user-attachments/assets/106cee8f-ac7c-4071-abc8-0570e4b07f03" />


### 4. Histograma de frecuencias
Se generó un histograma para visualizar la distribución de las duraciones de las canciones.

#### Resultado del histograma
¿Se parece a alguna distribución conocida?
A simple vista de la gráfica, la distribución muestra una concentración de valores alrededor de la media, pero también presenta una dispersión notable hacia los extremos. Esto no es típico de una distribución normal, que tiende a ser más simétrica, por lo que podría estar más cerca de una distribución log-normal o gamma, que pueden mostrar colas más largas y un comportamiento asimétrico.

<img width="517" alt="Captura de pantalla 2025-04-01 a la(s) 11 11 54" src="https://github.com/user-attachments/assets/f5f141d5-2f48-409a-a9ed-192dcc804e1d" />


### 5. Ajuste de distribución con Fitter
Para confirmar la mejor distribución que ajusta a los datos, se utilizó la librería Fitter en Python. Se compararon varias distribuciones comunes:
<br>Normal
<br>Exponencial
<br>Log-normal
<br>Gamma

### 6. Parámetros de la distribución óptima
Tras ejecutar Fitter, la mejor distribución encontrada fue log-normal con los siguientes parámetros:
<br>s (Forma): 10.172
<br>loc (Localización): 191.0
<br>scale (Escala): 29.586

### 7. Reflexión y conclusiones
#### ¿Cuáles son los parámetros de la distribución?
Se identificó que la distribución log-normal es la más adecuada para modelar el comportamiento de los datos, proporcionando información sobre cómo se distribuyen las observaciones en relación con la media y cómo se dispersan.

#### ¿Cómo podría utilizarse este modelo?
Este modelo podría ser útil para predecir la duración de procesos o eventos, como el tiempo que tarda un cliente en hacer una compra en línea, o el tiempo de espera en un restaurante. También podría aplicarse en la optimización de tiempos en procesos industriales o en la planificación de proyectos.

#### ¿Se pueden usar distribuciones de probabilidad para identificar similitudes entre varios procesos?
Sí, por ejemplo, podríamos comparar el tiempo de espera en diferentes tiendas o la duración de los viajes en distintas rutas para ver si siguen patrones similares. También se podría utilizar para analizar el tiempo que tardan en completarse tareas dentro de un proceso de fabricación o incluso comparar la distribución de tiempos de respuesta en diferentes sistemas informáticos.
