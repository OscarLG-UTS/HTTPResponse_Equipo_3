from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

lista_integrantes = [{'item_id': 1, 'matricula': 918765432, 'nombre':'Juan', 'APaterno':'Hernandez', 'AMaterno':'Gomez', 'correo':'juanHGomez@gmail.com', 'telefono': 9191853124, 'carrera':'IRIyC', 'edad':21, 'sexo':'H', 'LugarNacimiento':'Tuxtla Gutierrez'}, 
                     {'item_id': 2, 'matricula': 918765433, 'nombre':'Pedro', 'APaterno':'Guzman', 'AMaterno':'Salazar', 'correo':'GSPedrito@gmail.com', 'telefono': 9191376483, 'carrera':'IRIyC', 'edad':21, 'sexo':'H', 'LugarNacimiento':'Ocosingo'}, 
                     {'item_id': 3, 'matricula': 918765434, 'nombre':'Maria', 'APaterno':'Torres', 'AMaterno':'Sanchez', 'correo':'MariaTorres2000@gmail.com', 'telefono': 6675822176, 'carrera':'IRIyC', 'edad':20, 'sexo':'M', 'LugarNacimiento':'Chilon'}, 
                     {'item_id': 4, 'matricula': 918765435, 'nombre':'Carla','APaterno':'Arcia', 'AMaterno':'Lopez', 'correo':'CarlaArciaL23@gmail.com', 'telefono': 9832728937, 'carrera':'IRIyC', 'edad':20, 'sexo':'M', 'LugarNacimiento':'Tuxtla Gutierrez'},
                     {'item_id': 5, 'matricula': 91810027, 'nombre':'Jorge Antonio', 'APaterno':'Rodriguez', 'AMaterno':'De la Torre', 'correo':'mecosde@gmail.com', 'telefono': 9612284428, 'carrera':'IRIyC', 'edad':21, 'sexo':'H', 'LugarNacimiento':'Venustiano Carranza'},
                     {'item_id': 6, 'matricula': 91810372, 'nombre':'Josue Jonathan', 'APaterno':'Perez', 'AMaterno':'Gonzalez', 'correo':'josuepereztic@laselva.edu.mx', 'telefono': 9191109773 , 'carrera':'IRIyC', 'edad':23, 'sexo':'H', 'LugarNacimiento':'Yajalon'},
                     {'item_id': 7, 'matricula': 91810232, 'nombre':'Jose Daniel', 'APaterno':'Cruz', 'AMaterno':'Luna', 'correo':'sprayerjose@gamil.com', 'telefono': 9191233278, 'carrera':'IRIyC', 'edad':20, 'sexo':'H', 'LugarNacimiento':'Ocosingo'},
                     {'item_id': 8, 'matricula': 91810143, 'nombre':'Oscar', 'APaterno':'Lopez', 'AMaterno':'Gomez', 'correo':'oscarlopezgomez701@gmail.com', 'telefono': 9191331534, 'carrera':'IRIyC', 'edad':20, 'sexo':'H', 'LugarNacimiento':'Ocosingo'},
                     {'item_id': 9, 'matricula': 91810892, 'nombre':'Alfredo', 'APaterno':'Felix', 'AMaterno':'Gallardo', 'correo':'felixAl23@gmail.com', 'telefono': 6672437766, 'carrera':'IRIyC', 'edad':23, 'sexo':'H', 'LugarNacimiento':'Comitan'},
                     {'item_id': 10, 'matricula': 91811545, 'nombre':'Andrea', 'APaterno':'Beltran', 'AMaterno':'Leyva', 'correo':'AndreaBeltran2000@gmail.com', 'telefono': 9611435431, 'carrera':'IRIyC', 'edad':20, 'sexo':'M', 'LugarNacimiento':'Tuxtla Gutierrez'}]

@app.get("/integrantes")
async def leer_integrante(item_id: int):
    for diccionario in lista_integrantes:
        if diccionario.get('item_id') == item_id:
            respuesta = f"""
                <html>
                <head>
                    <title>{diccionario.get('nombre')}</title>
                </head>
                <body>
                    <h3>Sitio Personal</h3>
                    <ul>
                        <li>Matricula: {diccionario.get('matricula')}</li>
                        <li>Nombre: {diccionario.get('nombre')}</li>
                        <li>Apellido Paterno: {diccionario.get('APaterno')}</li>
                        <li>Apellido Materno: {diccionario.get('AMaterno')}</li>
                        <li>Correo: {diccionario.get('correo')}</li>
                        <li>Telefono: {diccionario.get('telefono')}</li>
                        <li>Carrera: {diccionario.get('carrera')}</li>
                        <li>Edad: {diccionario.get('edad')}</li>
                        <li>Sexo: {diccionario.get('sexo')}</li>
                        <li>Lugar de Nacimiento: {diccionario.get('LugarNacimiento')}</li>
                    </ul>
                </body>
                </html>
            """
            return HTMLResponse(content=respuesta, status_code=200)
    return "No se encontró el registro"
