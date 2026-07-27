═══════════════════════════════════════════════════════════════
  CLASS TOOLS PRO — Android / Acode Edition
  Club de Conversación Teshiba
═══════════════════════════════════════════════════════════════

📦 ARCHIVOS INCLUIDOS
─────────────────────
  index.html              → La app PWA
  manifest.json           → Configuración PWA
  sw.js                   → Funciona offline
  icon-192.png / icon-512.png
  generate_audio.py       → Script Python (para Acode + Pydroid/Termux)
  generate_audio.html     → Generador en navegador (SIN instalar nada)
  audio/                  → Carpeta vacía (aquí van los MP3)

═══════════════════════════════════════════════════════════════

🚀 OPCIÓN A: Generar audios desde el NAVEGADOR (MÁS FÁCIL)
─────────────────────────────────────────────────────────

NO necesitas instalar Python. Solo Chrome o Firefox en Android.

1. Abre generate_audio.html en Chrome/Firefox
2. Toca "Empezar"
3. Los 15 audios se descargarán uno por uno
4. Mueve los MP3 descargados a la carpeta audio/
5. Sube todo a Netlify Drop: https://app.netlify.com/drop

═══════════════════════════════════════════════════════════════

🐍 OPCIÓN B: Generar audios con Python en Android (Acode)
─────────────────────────────────────────────────────────

Requiere instalar Pydroid 3 o Termux.

PASO 1: Instalar Pydroid 3
  → Play Store → busca "Pydroid 3" → instalar

PASO 2: Instalar requests
  → Abre Pydroid 3
  → En la terminal escribe: pip install requests
  → Espera a que termine

PASO 3: Abrir generate_audio.py en Acode
  → Abre Acode
  → Abre el archivo generate_audio.py
  → Revisa que la API Key esté correcta

PASO 4: Ejecutar en Pydroid 3
  → En Pydroid 3, toca el ícono de carpeta amarilla
  → Busca y abre generate_audio.py
  → Toca el botón amarillo de PLAY (▶)
  → Espera ~2 minutos

PASO 5: Verificar
  → Se crearán 15 archivos en la carpeta audio/
  → phrase_01.mp3, phrase_02.mp3, ..., phrase_15.mp3

═══════════════════════════════════════════════════════════════

☁️ PASO 6: SUBIR A INTERNET (Netlify Drop)
───────────────────────────────────────────

1. Ve a: https://app.netlify.com/drop
2. Arrastra TODA esta carpeta (con los MP3 ya generados)
3. Te dará un link en 10 segundos

═══════════════════════════════════════════════════════════════

📲 PASO 7: INSTALAR EN EL TELÉFONO
───────────────────────────────────

Android (Chrome):
  → Abre el link en Chrome
  → Menú ⋮ → "Agregar a pantalla de inicio"

iPhone (Safari):
  → Abre el link en Safari
  → Compartir → "Agregar a pantalla de inicio"

═══════════════════════════════════════════════════════════════
