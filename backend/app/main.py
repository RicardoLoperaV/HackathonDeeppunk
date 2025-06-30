from fastapi import FastAPI, WebSocket, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import json
import base64
from dotenv import load_dotenv
import google.generativeai as genai
from google.cloud import speech, texttospeech

load_dotenv()

app = FastAPI(title="Agente Voz-a-Voz", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configurar Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Clientes de Google Cloud
speech_client = speech.SpeechClient()
tts_client = texttospeech.TextToSpeechClient()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    audio_base64: str

@app.get("/")
async def root():
    return {"message": "Agente Voz-a-Voz API"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        # Generar respuesta con Gemini
        response = model.generate_content(f"Responde en español de manera conversacional: {request.message}")
        text_response = response.text
        
        # Convertir texto a audio
        synthesis_input = texttospeech.SynthesisInput(text=text_response)
        voice = texttospeech.VoiceSelectionParams(
            language_code="es-ES",
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        
        tts_response = tts_client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        
        audio_base64 = base64.b64encode(tts_response.audio_content).decode()
        
        return ChatResponse(response=text_response, audio_base64=audio_base64)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.websocket("/api/stream")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.WEBM_OPUS,
        sample_rate_hertz=48000,
        language_code="es-ES",
    )
    
    streaming_config = speech.StreamingRecognitionConfig(
        config=config,
        interim_results=True,
    )
    
    try:
        while True:
            data = await websocket.receive_bytes()
            
            # Procesar audio con Speech-to-Text
            audio_generator = [speech.StreamingRecognizeRequest(audio_content=data)]
            requests = (speech.StreamingRecognizeRequest(audio_content=chunk) 
                       for chunk in audio_generator)
            
            responses = speech_client.streaming_recognize(streaming_config, requests)
            
            for response in responses:
                for result in response.results:
                    if result.is_final:
                        transcript = result.alternatives[0].transcript
                        await websocket.send_json({"transcript": transcript})
                        
    except Exception as e:
        await websocket.send_json({"error": str(e)})
        await websocket.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)