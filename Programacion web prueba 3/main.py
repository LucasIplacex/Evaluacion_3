from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None
    nota1 = None
    nota2 = None
    nota3 = None
    asistencia = None

    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            if not (10 <= nota1 <= 70) or not (10 <= nota2 <= 70) or not (10 <= nota3 <= 70):
                return render_template('ejercicio1.html', error="Las notas deben estar entre 10 y 70", nota1=int(nota1), nota2=int(nota2), nota3=int(nota3), asistencia=int(asistencia))

            if not (0 <= asistencia <= 100):
                return render_template('ejercicio1.html', error="La asistencia debe estar entre 0 y 100", nota1=int(nota1), nota2=int(nota2), nota3=int(nota3), asistencia=int(asistencia))

            promedio = (nota1 + nota2 + nota3) / 3

            if promedio >= 40 and asistencia >= 75:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"

        except ValueError:
            return render_template('ejercicio1.html', error="Por favor ingresa solo numeros", nota1=int(nota1) if nota1 else "", nota2=int(nota2) if nota2 else "",
            nota3=int(nota3) if nota3 else "", asistencia=int(asistencia) if asistencia else "")

    return render_template('ejercicio1.html', promedio=promedio, estado=estado, nota1=int(nota1) if nota1 else "", nota2=int(nota2) if nota2 else "",
    nota3=int(nota3) if nota3 else "", asistencia=int(asistencia) if asistencia else "")

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form.get('nombre1')
        nombre2 = request.form.get('nombre2')
        nombre3 = request.form.get('nombre3')

        if not nombre1 or not nombre2 or not nombre3:
            error = "Por favor, ingrese los tres nombres."
            return render_template('ejercicio2.html', error=error,nombre1=nombre1, nombre2=nombre2, nombre3=nombre3)

        nombres = [nombre1, nombre2, nombre3]
        mas_largo = max(nombres, key=len)
        longitud = len(mas_largo)

        return render_template('ejercicio2.html', mas_largo=mas_largo, longitud=longitud, nombre1=nombre1, nombre2=nombre2, nombre3=nombre3)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run()