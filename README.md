### Backend

📦backend
 ┣ 📂app
 ┃ ┣ 📂api          # Rutas, endpoints y controladores de FastAPI
 ┃ ┣ 📂core         # Configuración global, variables de entorno (.env), seguridad
 ┃ ┣ 📂models       # Modelos de datos (aquí estructuramos las tablas de PostgreSQL)
 ┃ ┣ 📂schemas      # Validaciones de Pydantic (los contratos de entrada y salida)
 ┃ ┣ 📂services     # La lógica de negocio pesada (aquí se conectará el Agente de IA)
 ┃ ┗ 📜main.py      # El interruptor principal que enciende el servidor
 ┣ 📜.python-version
 ┗ 📜pyproject.toml