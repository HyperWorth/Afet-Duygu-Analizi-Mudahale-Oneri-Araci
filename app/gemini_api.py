import os
from dotenv import load_dotenv
from google import generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_emotion(text: str):
    prompt = f"""
Bir afet sonrası halktan gelen bir cümle aşağıdadır:

"{text}"

Lütfen bu cümleyi analiz et ve aşağıdaki formatta yanıt ver:

Duygu: (örneğin: korku, panik, öfke, umutsuzluk, umut, güven)
Skor: (0 ile 100 arasında sayısal bir değer, örn: 78)
Öneri: (Bu duyguya yönelik yapılması gereken müdahale veya eylem)

Sadece Türkçe cevap ver. Liste ve açıklama istemiyorum. Formatı bozmadan yaz.
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Hata oluştu: {str(e)}"
