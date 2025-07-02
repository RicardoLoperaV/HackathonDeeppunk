# 🎤 Voces de Confianza: Agente Conversacional Ético para Adultos Mayores

Voces de Confianza es un agente de conversación en español diseñado para acompañar a los adultos mayores que se sienten solos. Como compañero digital, siempre está disponible para escuchar y dialogar con calidez, sin juzgar ni filtrar lo que importa. Aprovecha la potencia de Gemini y un enfoque centrado en la equidad y el respeto por la privacidad, adaptándose a su ritmo y a sus necesidades. Con este aliado, combatimos la soledad, preservamos historias valiosas y brindamos compañía genuina, gracias a un entrenamiento minucioso que garantiza respuestas empáticas y seguras.

## 🏗️ Arquitectura

- **Frontend**: HTML/CSS/JavaScript con Web Audio API
- **Backend**: Webhook n8n (https://totoratsu.app.n8n.cloud/webhook/viejito)
- **Despliegue**: Docker

## 🚀 Instalación y Configuración

### Prerrequisitos

1. **Software requerido**:
   - Docker
   - Navegador web moderno con soporte para Web Audio API

### Configuración

No se requiere configuración adicional. El demo se conecta directamente al webhook de n8n.

## 🐳 Despliegue con Docker

### Opción 1: Docker Compose (Recomendado)

```bash
# Levantar servicios
docker-compose up --build
```

**Acceso**:
- Frontend: http://localhost:3000
- Demo: http://localhost:3000/demo.html

### Opción 2: Contenedores individuales

```bash
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

## 🎤 Uso del Demo

1. Accede a http://localhost:3000/demo.html
2. Permite el acceso al micrófono cuando se solicite
3. Presiona el micrófono o el botón "Grabar" para comenzar
4. Habla tu mensaje
5. Presiona "Detener" para enviar el audio
6. El agente procesará tu mensaje y responderá con audio

### Webhook Endpoint

- `POST https://totoratsu.app.n8n.cloud/webhook/viejito`
- Content-Type: `audio/webm`
- Respuesta: Audio blob (audio/mpeg o audio/webm)

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
├── frontend/
│   ├── public/
│   │   ├── index.html       # Página principal
│   │   └── demo.html        # Demo del agente de voz
│   ├── src/
│   │   ├── App.js           # Componente principal React
│   │   ├── App.css
│   │   └── index.js
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

1. **Error de micrófono**:
   - Asegurar que el navegador tenga permisos de micrófono
   - Usar HTTPS en producción (requerido para Web Audio API)

2. **Error de CORS**:
   - El webhook de n8n debe tener CORS habilitado

3. **Error de conexión al webhook**:
   - Verificar que el backend esté corriendo en el puerto correcto
   - Revisar la variable `REACT_APP_API_URL`

3. **Problemas con el micrófono**:
   - Asegurar que el navegador tenga permisos de micrófono
   - Usar HTTPS en producción (requerido para Web Audio API)

### Logs útiles

```bash
# Ver logs de Docker Compose
docker-compose logs -f

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
- [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
- [MediaRecorder API](https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder)
- [n8n Webhooks](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/)
- [React Documentation](https://reactjs.org/docs/getting-started.html)
Sistema creado para conversar de manera natural con adultos mayores. Teniendo en cuenta la época que vivieron y las cosas que eran relevantes.
