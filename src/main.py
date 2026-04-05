from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

# Aquí definimos la ruta principal
@app.route('/')
def home():
    # Solo dejamos los proyectos de software
    proyectos = [
        {
            'titulo': 'Sistema Control Embebido',
            'desc': 'Simulador de ciclos lógicos para hardware (Interfaz de Lavadora) desarrollado íntegramente en Python. Utiliza una arquitectura de estados para gestionar tiempos, procesos de lavado, enjuague y centrifugado en tiempo real, ofreciendo una respuesta visual inmediata al usuario.',
            'tech': 'Python, Tkinter , Lógica de Estados',
            'repo': 'https://github.com/Emi659/Sistema-embebido-lavadora'
        },
        {
            'titulo': 'E-commerce ',
            'desc': 'Desarrollo de una aplicación web con arquitectura cliente-servidor. Implementa un backend robusto en Python para el procesamiento de peticiones, una conexión a base de datos utilizando el gestor MariaDB con su software HeidiSQL y una interfaz moderna responsiva. Enfocado en la eficiencia de carga y la experiencia de usuario final.',
            'tech': 'Python, Flask, HTML5, CSS3, JavaScript, MariaDB',
            'repo': 'https://github.com/Emi659/E-commerce'
        },
        {
            'titulo': 'Juego de Laberinto',
            'desc': 'Juego interactivo de laberinto desarrollado en C++ con enemigos que persiguen al jugador. Incluye 3 niveles de dificultad progresiva, recolección de llaves para avanzar y gráficos dinámicos. El objetivo es escapar del laberinto evitando a los enemigos y recogiendo la llave de salida.',
            'tech': 'C++, Algoritmos de Búsqueda, Gráficos 2D',
            'repo': 'https://github.com/Emi659/Videojuego-Laberinto-consola-'
        }
    ]
    return render_template('index.html', proyectos=proyectos)

if __name__ == '__main__':
    app.run(debug=True)
