import os
from dotenv import load_dotenv
from google import generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_emotion(text1: str):
    prompt = f"""
Aşağıdaki cümle, afet sonrası bir vatandaş tarafından yazılmış olabilir:

"{text1}"

Bu cümleyi analiz et ve aşağıdaki başlıkları sırayla doldur:

1. Duygu: (örneğin: umut, panik, korku, güven, öfke, rahatlama, üzüntü)
2. Skor: (0 ile 100 arasında bir değer – 80+ = yüksek duygu yoğunluğu)
3. Öneri: Bu duygusal duruma uygun olarak ne tür müdahale, destek veya bilgilendirme yapılabilir?

Olumlu ifadelerde de öneri yazmayı ihmal etme (örneğin: “mevcut destek devam ettirilmeli” gibi).
Sadece Türkçe ve yukarıdaki formatta yanıt ver. Açıklama ekleme.
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Hata oluştu: {str(e)}"
