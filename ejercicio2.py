from fastapi import FastAPI
from typing import Optional
from fastapi.responses import HTMLResponse

app = FastAPI()
	
@app.get("/integrantes/{item_id}")
async def leer_integrante(item_id: int, matricula: int, nombre: str, carrera: str, edad: Optional[int] = None):
	respuesta = f"""
	<html>
    <head>
        <title>{nombre}</title>
    </head>
    <body>
        <h3>Mis Datos Personales</h3>
        <ul>
            <li>Matricula: {matricula}</li>
            <li>Nombre: {nombre}</li>
            <li>Carrera: {carrera}</li>
            <li>Edad: {edad}</li>
        </ul>
    </body>
	</html>
	"""
	return HTMLResponse(content=respuesta, status_code=200)