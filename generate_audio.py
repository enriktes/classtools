from gtts import gTTS
import os

PHRASES = [
    "Would you please repeat that?",
    "What is the meaning of that?",
    "How do you say that in English?",
    "How do you spell that?",
    "Would you please write that down?",
    "Would you please speak slower?",
    "May I please go to the bathroom?",
    "May I please take this call?",
    "May I please step outside?",
    "What is the phonetics of that?",
    "How do you pronounce that?",
    "Can you hear me clearly?",
    "Let's get started.",
    "Does anyone have any questions?",
    "That's all for today."
]

OUTPUT_DIR = "audio"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=" * 55)
print("  CLASS TOOLS PRO — Generador de audios Google TTS")
print("  100% GRATIS — Sin API key")
print("=" * 55)
print()

for i, phrase in enumerate(PHRASES, 1):
    filename = f"phrase_{i:02d}.mp3"
    filepath = os.path.join(OUTPUT_DIR, filename)

    if os.path.exists(filepath):
        print(f"⏭️  {filename} ya existe, saltando...")
        continue

    print(f"🔊 {i:02d}/15: {phrase}")

    try:
        tts = gTTS(text=phrase, lang='en', slow=False)
        tts.save(filepath)
        print(f"   ✅ Guardado: {filename}")
    except Exception as e:
        print(f"   ❌ Error: {e}")

print()
print("=" * 55)
print("  🎉 ¡Listo! Los audios están en la carpeta 'audio/'")
print("=" * 55)
print()
print("  Ahora sube esta carpeta completa a Netlify Drop:")
print("  → https://app.netlify.com/drop")
