"""
Execute this file to run the server locally
"""

import configparser
import sys

import uvicorn
from fastapi import FastAPI

config = configparser.ConfigParser()
config.read("config.ini")

for key, value in config.items("pythonpath"):
    sys.path.append(value)

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

from fastapi.middleware.cors import CORSMiddleware
from modules.funds.app import router as funds_router
from modules.transactions.app import router as transactions_router
from modules.auth.app import router as auth_router

app = FastAPI()

origins = [
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitimos solo los orígenes especificados
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluye los routers de los módulos con prefijos específicos
app.include_router(funds_router)  # Rutas de fondos
app.include_router(transactions_router)  # Rutas de transacciones
app.include_router(auth_router)  # Rutas de transacciones
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
