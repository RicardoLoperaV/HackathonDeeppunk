# 🎤 Voces de Confianza: Agente Conversacional Ético para Adultos Mayores

Voces de Confianza es un agente de conversación en español diseñado para acompañar a los adultos mayores que se sienten solos. Como compañero digital, siempre está disponible para escuchar y dialogar con calidez, sin juzgar ni filtrar lo que importa. Aprovecha la potencia de Gemini y un enfoque centrado en la equidad y el respeto por la privacidad, adaptándose a su ritmo y a sus necesidades. Con este aliado, combatimos la soledad, preservamos historias valiosas y brindamos compañía genuina, gracias a un entrenamiento minucioso que garantiza respuestas empáticas y seguras.

## 🏗️ Arquitectura

- **Backend**: FastAPI con Python
- **Frontend**: React con Web Audio API
- **IA**: Google Gemini + Google Cloud Speech & Text-to-Speech
- **Despliegue**: Docker + Docker Compose

## 🚀 Instalación y Configuración

### Prerrequisitos

1. **Cuentas y APIs necesarias**:
   - [Google Cloud Platform](https://cloud.google.com/) con Speech-to-Text y Text-to-Speech habilitados
   - [Google AI Studio](https://makersuite.google.com/) para obtener API key de Gemini

2. **Software requerido**:
   - Docker y Docker Compose
   - Node.js 18+ (para desarrollo local)
   - Python 3.11+ (para desarrollo local)

### Configuración de Credenciales

1. **Google Cloud**:
   ```bash
   # Crear service account y descargar JSON key
   # Guardar como 'service-account-key.json' en el directorio raíz
   ```

2. **Variables de entorno**:
   ```bash
   # Copiar archivos de ejemplo
   cp backend/.env.example backend/.env
   cp frontend/.env.example frontend/.env
   
   # Editar backend/.env
   GEMINI_API_KEY=tu_api_key_de_gemini
   GOOGLE_APPLICATION_CREDENTIALS=./service-account-key.json
   
   # Editar frontend/.env
   REACT_APP_API_URL=http://localhost:8000
   ```

## 🐳 Despliegue con Docker

### Opción 1: Docker Compose (Recomendado)

```bash
# Configurar variables de entorno
export GEMINI_API_KEY="tu_api_key"
export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/service-account-key.json"

# Levantar servicios
docker-compose up --build
```

**Acceso**:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Documentación API: http://localhost:8000/docs

### Opción 2: Contenedores individuales

```bash
# Backend
cd backend
docker build -t agente-voz-backend .
docker run -p 8000:8000 \
  -e GEMINI_API_KEY="tu_api_key" \
  -v $(pwd)/../service-account-key.json:/app/credentials.json \
  agente-voz-backend

# Frontend
cd frontend
docker build -t agente-voz-frontend .
docker run -p 3000:80 agente-voz-frontend
```

## 💻 Desarrollo Local

### Backend

```bash
cd backend

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend

# Instalar dependencias
npm install

# Ejecutar en modo desarrollo
npm start
```

## 📡 API Endpoints

### REST API

- `GET /` - Health check
- `POST /api/chat` - Enviar mensaje de texto y recibir respuesta con audio

### WebSocket

- `WS /api/stream` - Streaming de audio para transcripción en tiempo real

### Ejemplo de uso

```javascript
// Enviar mensaje de texto
const response = await fetch('http://localhost:8000/api/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ message: 'Hola, ¿cómo estás?' })
});

const data = await response.json();
console.log(data.response); // Respuesta en texto
// data.audio_base64 contiene el audio en base64
```

## 🧪 Testing

```bash
# Backend
cd backend
pip install pytest
pytest

# Frontend
cd frontend
npm test
```

## 🔧 Estructura del Proyecto

```
.
├── backend/
│   ├── app/
│   │   └── main.py          # FastAPI app principal
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── App.js           # Componente principal React
│   │   ├── App.css
│   │   └── index.js
│   ├── public/
│   │   └── index.html
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── package.json
│   └── .env.example
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions CI/CD
├── docker-compose.yml
└── README.md
```

## 🚨 Solución de Problemas

### Errores comunes

1. **Error de autenticación de Google Cloud**:
   - Verificar que el archivo JSON de credenciales existe
   - Confirmar que las APIs están habilitadas en GCP

2. **Error de CORS en el frontend**:
   - Verificar que el backend esté corriendo en el puerto correcto
   - Revisar la variable `REACT_APP_API_URL`

3. **Problemas con el micrófono**:
   - Asegurar que el navegador tenga permisos de micrófono
   - Usar HTTPS en producción (requerido para Web Audio API)

### Logs útiles

```bash
# Ver logs de Docker Compose
docker-compose logs -f

# Logs específicos del backend
docker-compose logs backend

# Logs específicos del frontend
docker-compose logs frontend
```

## 🤝 Contribución

1. Fork el proyecto
2. Crear rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 🔗 Enlaces Útiles

- [Documentación de FastAPI](https://fastapi.tiangolo.com/)
- [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text)
- [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech)
- [Google Generative AI](https://ai.google.dev/)
- [React Documentation](https://reactjs.org/docs/getting-started.html)
Sistema creado para conversar de manera natural con adultos mayores. Teniendo en cuenta la época que vivieron y las cosas que eran relevantes.
