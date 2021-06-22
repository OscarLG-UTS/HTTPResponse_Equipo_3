from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title = "FastAPI con Jinja2")

app.mount("/rutarecursos", StaticFiles(directory="recursos"), name="mirecurso")

miPlantilla = Jinja2Templates(directory="plantillas")

@app.get("/integrantes/", response_class=HTMLResponse)
async def leer_integrante(request: Request, matricula: int, nombre: str, carrera: str, edad: int):
    return miPlantilla.TemplateResponse("integrantes.html",{"request":request, "matri": matricula,
                                                            "nom":nombre, "carr": carrera, "edad":edad })
