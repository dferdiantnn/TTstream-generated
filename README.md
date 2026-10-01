# 🔴 TikTok Live Generator Link - Kandang Monyet

> 🌐 **Website Resmi (Siap Pakai):** 👉 **[https://ttstream.vercel.app](https://ttstream.vercel.app)**  
> 🛡️ **100% Nonton Live Stream TikTok Bebas Tanpa Login Akun!**

Aplikasi web dan API untuk mengonversi tautan siaran langsung TikTok (baik link pendek `vt.tiktok.com`, URL web, maupun `@username`) menjadi tautan video streaming langsung (**HLS `.m3u8`**).

Tautan `.m3u8` yang dihasilkan dapat langsung diputar di:
- **iPhone / iPad Safari** (pemutar video bawaan iOS dengan fitur Picture-in-Picture).
- **VLC Media Player**.
- **Browser Modern** (Chrome, Firefox, Edge, Safari via pemutar web bawaan).

---

## ✨ Fitur Utama

- ⚡ **Tanpa Login & Tanpa Aplikasi TikTok**: Ekstrak link streaming langsung dari CDN resmi TikTok tanpa perlu login akun sama sekali.
- 📱 **Ramah Mobile & Dark Mode**: Tampilan web bernuansa *Neo-Brutalist Dark*, responsif, dan ringan (diadopsi dari desain kokopcoffee).
- 🎥 **Pemutar Video Bawaan**: Langsung menonton live stream di halaman web.
- 🔗 **Mendukung Segala Format Link**:
  - `https://vt.tiktok.com/ZS9DNt5ndtpxn-bSGbT/`
  - `https://www.tiktok.com/@username/live`
  - `@username` atau sekadar `username`
- 🚀 **Deployed on Vercel**: Dilengkapi dengan serverless function Python tanpa dependensi pihak ketiga.

---

## 🌐 Akses Website Online

Website sudah aktif dan dapat langsung digunakan melalui browser HP/PC Anda:
👉 **[https://ttstream.vercel.app](https://ttstream.vercel.app)**

---

## 💻 Cara Menjalankan Secara Lokal

Program ini hanya menggunakan pustaka bawaan standar Python, sehingga **tidak memerlukan `pip install` apa pun**.

### 1. Sebagai Web Server Lokal
Jalankan perintah berikut di terminal:
```bash
python3 app.py
```
Lalu buka browser Anda di:
👉 `http://localhost:5000`

### 2. Sebagai Alat CLI (Terminal)
Anda juga dapat langsung mengekstrak link melalui terminal:
```bash
python3 app.py "https://vt.tiktok.com/ZS9DNt5ndtpxn-bSGbT/"
```

---

## 🔌 Dokumentasi API

Endpoint backend yang dapat dipanggil secara langsung:

```http
GET https://ttstream.vercel.app/api/convert?url=<LINK_TIKTOK_ATAU_USERNAME>
```

**Contoh Response (Sedang Live):**
```json
{
  "status": "live",
  "username": "mekaniktuax",
  "title": "CARI 7x CHICKEN with 2 BOBI !!",
  "viewers": 1240,
  "room_id": "7691609887024892680",
  "m3u8_url": "https://pull-hls-q5-sg01.tiktokcdn.com/game/..._hd/index.m3u8?expire=...",
  "flv_url": "https://pull-q5-sg01.tiktokcdn.com/game/..._hd.flv?expire=..."
}
```

**Contoh Response (Offline):**
```json
{
  "status": "offline",
  "username": "mekaniktuax",
  "message": "Akun @mekaniktuax sedang tidak live."
}
```

---

## 👤 Author & Copyright

Crafted by [@dferdiantn](https://www.instagram.com/dferdiantn)
