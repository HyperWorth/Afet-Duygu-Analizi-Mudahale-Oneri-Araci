````markdown
# 🌪️ Afet Duygu Analizi ve Müdahale Öneri Aracı

Bu proje, afet sonrası vatandaşların yazılı ifadelerini analiz ederek **duygusal durumu belirlemeyi** ve bu duyguya uygun **müdahale önerileri sunmayı** amaçlayan bir yapay zeka destekli araçtır.

Yapay zekâ, kullanıcının girdiği her cümleyi analiz eder:
- 🧠 Duygusal durumu tespit eder (panik, öfke, umut, vb.)
- 🎯 0–100 arasında bir duygu skoru verir
- 💡 Duruma özel bir müdahale/aksiyon önerisi sunar

---

## 🔧 Kullanılan Teknolojiler

| Katman        | Teknoloji            |
|---------------|----------------------|
| Backend       | Python (Flask)       |
| AI Model      | Google Gemini (gemini-2.5-flash) |
| Arayüz        | HTML, CSS, JavaScript |
| UI/UX         | Flexbox kart yapısı + dinamik renk sistemi |
| Güvenlik      | `.env` ile API anahtarı yönetimi |

---

## 💡 Özellikler

- ✅ Serbest metin girişi (çok satırlı)
- ✅ Her satır için duygu analizi + öneri üretimi
- ✅ Skora göre renkli kartlarla gösterim (kırmızı, sarı, yeşil)
- ✅ Kullanıcı deneyimini geliştiren loading animasyonu
- ✅ Responsive, sade ve modern arayüz

---

## 🖥️ Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/HyperWorth/afet_duygu_ai.git
cd afet_duygu_ai
````

2. Ortamı oluşturun ve bağımlılıkları yükleyin:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. `.env` dosyası oluşturun ve Gemini API anahtarınızı girin:

```
GEMINI_API_KEY=your_gemini_api_key
```

4. Uygulamayı çalıştırın:

```bash
flask run
```

5. Tarayıcıda açın: [http://127.0.0.1:5000](http://127.0.0.1:5000)


## 📁 Proje Yapısı

```
├── app/
│   ├── routes.py
│   ├── gemini_api.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
├── run.py
├── .env (gizli)
├── requirements.txt
├── README.md
```

---

## 📄 Lisans

MIT Lisansı – Detaylar için `LICENSE` dosyasına bakabilirsiniz.

---

## 👤 Geliştirici

* Ad: HyperWorth
* GitHub: [github.com/HyperWorth](https://github.com/HyperWorth)

---

## ✍️ Örnek Girdi

```text
Çadır hâlâ gelmedi, insanlar soğukta bekliyor.
Biraz umut var, sonunda sağlık ekipleri geldi.
Herkes yardım için bağırıyor ama kimse ilgilenmiyor.
```

---

## 🎯 Beklenen Çıktı (örnek)

```text
Duygu: Umutsuzluk
Skor: 92
Öneri: Acil çadır ve battaniye desteği verilmeli, halk bilgilendirilmeli.
```

---

## 📦 Geliştirilebilecek Özellikler

* [ ] JSON/CSV dışa aktarım
* [ ] Harita üzerinde duygu yoğunluğu görselleştirme
* [ ] PDF rapor çıktısı
* [ ] Gerçek zamanlı sosyal medya entegrasyonu (X / Reddit)

````

---

Bu dosyayı ister GitHub arayüzünden “Create new file” ile ekleyebilir, ister terminalden:

```bash
touch README.md
````

→ içine yapıştırıp:

```bash
git add README.md
git commit -m "📝 Proje tanımı eklendi"
git push origin main
```
komutlarıyla yükleyebilirsin.
