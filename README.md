# 🔴 TikTok Live M3U8 Stream Converter

Aplikasi web dan API untuk mengonversi tautan siaran langsung TikTok (baik link pendek `vt.tiktok.com`, URL web, maupun `@username`) menjadi tautan video streaming langsung (**HLS `.m3u8`**).

Tautan `.m3u8` yang dihasilkan dapat langsung diputar di:
- **iPhone / iPad Safari** (pemutar video bawaan iOS dengan fitur Picture-in-Picture).
- **VLC Media Player**.
- **Browser Modern** (Chrome, Firefox, Edge, Safari via pemutar web bawaan).

---

## ✨ Fitur Utama

- ⚡ **Tanpa Login & Tanpa Aplikasi TikTok**: Ekstrak link streaming langsung dari CDN resmi TikTok.
- 📱 **Ramah Mobile**: Tampilan web bersih, responsif, dark mode, dan ringan.
- 🎥 **Pemutar Video Bawaan**: Langsung menonton live stream di halaman web.
- 🔗 **Mendukung Segala Format Link**:
  - `https://vt.tiktok.com/ZS9DNt5ndtpxn-bSGbT/`
  - `https://www.tiktok.com/@username/live`
  - `@username` atau sekadar `username`
- 🚀 **Siap Deploy ke Vercel**: Dilengkapi dengan serverless function Python tanpa dependensi pihak ketiga.

---

## 🌐 Cara Menjadikan Web Online via GitHub & Vercel (Gratis)

Repositori ini sudah dikonfigurasi untuk langsung di-deploy ke **Vercel** secara gratis:

1. Buka [Vercel](https://vercel.com) dan login menggunakan akun **GitHub** Anda.
2. Klik tombol **"Add New..."** > pilih **"Project"**.
3. Pilih repositori **`TTstream-generated`** dari daftar repositori Anda.
4. Klik tombol **"Deploy"** (tanpa perlu mengubah pengaturan apapun).
5. Dalam ~1 menit, website Anda sudah aktif dan online dengan domain seperti:
   `https://ttstream-generated.vercel.app`

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

Jika Anda ingin menggunakannya sebagai endpoint backend:

```http
GET /api/convert?url=<LINK_TIKTOK_ATAU_USERNAME>
```

**Contoh Response (Sedang Live):**
```json
{
  "status": "live",
  "username": "mekaniktuax",
  "title": "CARI 7x CHICKEN with 2 BOBI !!",
  "viewers": 1240,
  "room_id": "7691609887024892680",
  "m3u8_url": "https://pull-hls-l11-sg01.tiktokcdn.com/game/stream-2137794040762728552_hd.m3u8?expire=...",
  "flv_url": "https://pull-flv-l11-sg01.tiktokcdn.com/game/stream-2137794040762728552_hd.flv?expire=..."
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
