# Spaceship-Game-MX-5-2023
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
    <h1>README</h1>

<p>Este repositorio contiene un juego implementado utilizando la biblioteca Pygame. El juego es un shooter espacial donde el jugador controla una nave espacial e intenta destruir enemigos y asteroides mientras evita las balas de los enemigos.</p>

<h2>Instalación</h2>

<p>Para ejecutar el juego, necesitas tener Python instalado en tu sistema. Puedes descargar Python desde el sitio web oficial: <a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a></p>

<p>Además, necesitas instalar la biblioteca Pygame. Puedes instalar Pygame usando pip, el gestor de paquetes de Python. Abre una terminal o símbolo del sistema y ejecuta el siguiente comando:</p>

<pre><code>pip install pygame</code></pre>

<h2>Uso</h2>

<p>Para iniciar el juego, ejecuta el siguiente comando en una terminal o símbolo del sistema:</p>

<pre><code>python game.py</code></pre>

<p>Una vez que el juego esté en ejecución, verás un menú con tres opciones: "Start Game" (Iniciar juego), "Statistics" (Estadísticas) y "Exit" (Salir). Puedes navegar por el menú usando las teclas de flecha (arriba y abajo) y seleccionar una opción presionando la tecla Enter.</p>

<p>Si seleccionas "Start Game", el juego comenzará y podrás controlar la nave espacial usando las teclas de flecha. Presiona la barra espaciadora para disparar balas y destruir enemigos y asteroides. El objetivo es sobrevivir el mayor tiempo posible y obtener una puntuación alta.</p>

<p>Durante el juego, tu puntuación actual se mostrará en la parte superior de la pantalla. Si tu nave espacial es destruida, el juego terminará y tu puntuación se mostrará en la pantalla de fin de juego. El juego también llevará un registro del número de veces que hayas muerto.</p>

<p>Si seleccionas "Statistics" en el menú, el juego mostrará tus estadísticas actuales, incluyendo el número de muertes y tu puntuación más alta. Las estadísticas se cargan desde un archivo JSON llamado "statistics.json" ubicado en el mismo directorio que el script del juego.</p>

<h2>Enemigos</h2>

<p>Burguer: Es un enemigo con aspecto de Hamburguesa que cae a una velocidad alta y cuando llega a la parte mas baja dispara hacia arriba, este enemigo tiene una bala personalizada.</p>
<p>Ship: Es un enemigo que tiene un movimiento en zigzag.</p>
<p>GoAllOver: Es un enemigo que hace un recorrido en toda la pantalla a una alta velocidad.</p>
<p>Ovni: Es un enemigo que aparece arriba de la pantalla y hace un movimiento en espiral que va aumentando de tamano mientras mas tiempo esta vivo.</p>

<h2>Obstaculos</h2>

<p>Asteroid: Es una roca de buen tamano que cae en diagonal y el jugador no puede destruirla, solo le queda esquivarla.</p>

</body>
</html>
