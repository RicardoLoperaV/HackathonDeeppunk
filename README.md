# 🎤 Voces de Compañía - Agente Voz-a-Voz

## Integrantes:

- **Nixon Daniel Lizcano Santana**
- **Joan Sebastian Salazar Montoya**
- **Ricardo Esteban Lopera Vasco**

Voces de Confianza es un agente de conversación en español diseñado para acompañar a los adultos mayores que se sienten solos. Como compañero digital, siempre está disponible para escuchar y dialogar con calidez, sin juzgar ni filtrar lo que importa. Aprovecha la potencia de Gemini y un enfoque centrado en la equidad y el respeto por la privacidad, adaptándose a su ritmo y a sus necesidades. Con este aliado, combatimos la soledad, preservamos historias valiosas y brindamos compañía genuina, gracias a un entrenamiento minucioso que garantiza respuestas empáticas y seguras.

## 🏗️ Arquitectura

- **Frontend**: React + HTML estático con Web Audio API
- **Backend**: Webhook n8n (https://totoratsu.app.n8n.cloud/webhook/viejito)
- **Demo**: Página HTML independiente para grabación y reproducción de audio
- **Despliegue**: Docker

## 🚀 Desarrollo Local

```bash
# Clonar repositorio
git clone <repository-url>
cd HackathonDeeppunk/frontend

# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm start
```

**Acceso**:
- Página principal: http://localhost:3000
- Demo de voz: http://localhost:3000/demo.html

## 🐳 Despliegue con Docker

```bash
# Construir y ejecutar
docker-compose up --build
```

## 🎤 Uso del Demo

1. **Acceder al demo**: Clic en botón "Demo" o navegar a `/demo.html`
2. **Permisos**: Permitir acceso al micrófono cuando se solicite
3. **Grabar**: Presionar el micrófono o botón "Grabar"
4. **Hablar**: Decir tu mensaje en español
5. **Enviar**: Presionar "Detener" para procesar
6. **Escuchar**: El agente responderá con audio automáticamente

### Integración Webhook

- **Endpoint**: `https://totoratsu.app.n8n.cloud/webhook/viejito`
- **Método**: POST con FormData
- **Campo**: `data` (archivo audio/webm)
- **Respuesta**: JSON con `audio_base64` o audio directo

## 🔧 Estructura del Proyecto

```
.
├── frontend/
│   ├── public/
│   │   ├── index.html       # Landing page principal
│   │   ├── demo.html        # Demo interactivo de voz
│   │   ├── etica_page.html  # Página de ética
│   │   └── video1.mp4, video2.mp4, video3.mp4
│   ├── src/
│   │   ├── App.js           # Componente React (no usado en demo)
│   │   ├── App.css
│   │   ├── index.js         # Punto de entrada React
│   │   └── setupProxy.js    # Configuración de rutas
│   ├── package.json
│   └── Dockerfile
├── etica/
│   └── etica.md            # Documentación ética
├── .github/workflows/
├── docker-compose.yml
└── README.md
```

## 🚨 Solución de Problemas

### Errores comunes

1. **Error de micrófono**:
   - Permitir acceso al micrófono en el navegador
   - Usar HTTPS en producción (requerido para Web Audio API)

2. **Error "Unexpected end of JSON input"**:
   - El webhook puede estar devolviendo respuesta vacía
   - Verificar logs de consola para debugging

3. **Error de conexión al webhook**:
   - Verificar conectividad a internet
   - El webhook n8n debe estar activo y configurado

### Debugging

```bash
# Logs del servidor de desarrollo
npm start

# Logs de Docker
docker-compose logs -f

# Consola del navegador (F12)
# - Response status y headers
# - Contenido de respuesta del webhook
# - Errores de audio y grabación
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

- [Create React App](https://create-react-app.dev/)
- [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
- [MediaRecorder API](https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder)
- [FormData API](https://developer.mozilla.org/en-US/docs/Web/API/FormData)
- [n8n Webhooks](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/)

## 👥 Equipo

Proyecto desarrollado para el Hackathon DeepPunk - Universidad Nacional de Colombia

**Misión**: Aumentar la calidad de vida de los adultos mayores a través de tecnología conversacional accesible.