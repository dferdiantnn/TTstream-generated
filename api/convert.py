import json
import re
import ssl
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler

def extract_tiktok_live(input_target):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    url = input_target.strip()
    if url.startswith('http://') or url.startswith('https://'):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
                url = resp.geturl()
        except Exception as e:
            pass

    match = re.search(r'@([a-zA-Z0-9_.-]+)', url)
    if match:
        username = match.group(1)
    else:
        username = url.replace('https://', '').replace('http://', '').replace('www.tiktok.com/', '').replace('@', '').split('/')[0].split('?')[0].strip()

    if not username:
        return {'status': 'error', 'message': 'Username tidak valid atau tidak ditemukan.'}

    profile_url = f'https://www.tiktok.com/@{username}'
    try:
        req = urllib.request.Request(profile_url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return {'status': 'error', 'message': f'Gagal mengakses profil TikTok: {str(e)}'}

    room_id = None
    m_script = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__"[^>]*>(.*?)</script>', html)
    if m_script:
        try:
            data = json.loads(m_script.group(1))
            scope = data.get('__DEFAULT_SCOPE__', {})
            user_info = scope.get('webapp.user-detail', {}).get('userInfo', {})
            room_id = user_info.get('user', {}).get('roomId')
        except Exception:
            pass

    if not room_id:
        m_id = re.search(r'"roomId":"(\d+)"', html)
        if m_id:
            room_id = m_id.group(1)

    if not room_id or str(room_id) == '0':
        return {'status': 'offline', 'username': username, 'message': f'Akun @{username} sedang tidak live.'}

    api_url = f'https://webcast.tiktok.com/webcast/room/info/?aid=1988&room_id={room_id}'
    try:
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            d = res.get('data', {})
    except Exception as e:
        return {'status': 'error', 'message': f'Gagal mengambil data webcast: {str(e)}'}

    if d.get('status') != 2:
        return {'status': 'ended', 'username': username, 'message': f'Siaran live @{username} telah berakhir.'}

    stream_url = d.get('stream_url', {})
    hls_url = stream_url.get('hls_pull_url')
    flv_url = stream_url.get('rtmp_pull_url') or (stream_url.get('flv_pull_url') or {}).get('HD1')

    return {
        'status': 'live',
        'username': username,
        'title': d.get('title', 'TikTok LIVE'),
        'viewers': d.get('user_count', 0),
        'room_id': str(room_id),
        'm3u8_url': hls_url,
        'flv_url': flv_url
    }

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        target_url = params.get('url', [''])[0]

        if not target_url:
            response_data = {'status': 'error', 'message': 'Parameter ?url= wajib diisi.'}
            status_code = 400
        else:
            try:
                response_data = extract_tiktok_live(target_url)
                status_code = 200
            except Exception as e:
                response_data = {'status': 'error', 'message': str(e)}
                status_code = 500

        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
