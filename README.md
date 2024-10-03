# btg-backend

# Python 3.12

## Requirements to Run the Project Locally

### Create a New Virtual Environment

1. Create a virtual environment:

   ```bash
   virtualenv venv
   ```

2. Activate the virtual environment:

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```bash
     source venv/bin/activate
     ```

3. Install the dependencies:
   ```bash
   pip install -r develop.txt
   ```

## Run the FastAPI Project

1. To run the FastAPI server:
   ```bash
   python main.py
   ```

## Run the FastAPI Project with AWS SAM (Recommended)

1. Download and install the AWS SAM CLI: [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

2. Build the project using a local template file:

   ```bash
   sam build --template-file template_local.yaml
   ```

3. Start the local API with debugging support:

   ```bash
   sam local start-api -d 5858
   ```

4. Or start the local API without debugging:
   ```bash
   sam local start-api
   ```
####  Validaciones
   - El usuario solo puede estar activo a un solo fondo.
   - 

### Dudas
   - ¿ Como el usuario agrega un monto a su cuenta ?
### Documentation

Estructura del Módulo Funds
Directorio y Archivos Involucrados:

\*\*\* modules/funds/

app.py # Rutas (endpoints).
services.py # Servicios (intermediario entre API y lógica de negocio).
controllers.py # Controladores (interacción directa con la lógica de dominio).
schemas.py # Esquemas (Pydantic models para requests/responses).

\*\*\* domain/funds/

entities.py # Entidades (Objetos de negocio).
repositories.py # Repositorio (Abstracción de la persistencia).
logic.py # Lógica de negocio (use cases).

Estructura del Módulo Transactions

\*\*\* modules/transactions/

app.py # Rutas (endpoints).
services.py # Servicios (intermediario entre API y lógica de negocio).
controllers.py # Controladores (interacción directa con la lógica de dominio).
schemas.py # Esquemas (Pydantic models para requests/responses).

\*\*\* domain/transactions/

entities.py # Entidades (Objetos de negocio).
repositories.py # Repositorio (Abstracción de la persistencia).
logic.py # Lógica de negocio (use cases).
