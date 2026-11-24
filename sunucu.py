# Kesir Çarkı - yerel sunucu
# Bu klasörü boş bir portta yayınlar ve oyunu tarayıcıda açar.
# Başka bir projenin sunucusu açık olsa bile ona karışmaz: dolu portu atlar.
import http.server, os, socket, sys, threading, webbrowser

KLASOR = os.path.dirname(os.path.abspath(__file__))
os.chdir(KLASOR)
ILK_PORT = 8771          # bu projeye ayrılan port (doluysa sıradaki boş port)


class Isleyici(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                      '.wasm': 'application/wasm', '.js': 'text/javascript', '.data': 'application/octet-stream'}

    def __init__(self, *a, **k):
        super().__init__(*a, directory=KLASOR, **k)

    def end_headers(self):
        # tarayıcı başka projenin eski sayfasını önbellekten getirmesin
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def log_message(self, *a):
        pass


class Sunucu(http.server.ThreadingHTTPServer):
    allow_reuse_address = False   # Windows'ta dolu porta ikinci kez bağlanmayı engeller

    def server_bind(self):
        if hasattr(socket, 'SO_EXCLUSIVEADDRUSE'):
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
        super().server_bind()


def port_dolu(p):
    with socket.socket() as s:
        s.settimeout(0.3)
        return s.connect_ex(('127.0.0.1', p)) == 0


sunucu = None
for port in range(ILK_PORT, ILK_PORT + 40):
    if port_dolu(port):
        continue
    try:
        sunucu = Sunucu(('127.0.0.1', port), Isleyici)
        break
    except OSError:
        continue

if not sunucu:
    print('  Boş port bulunamadı. Açık olan diğer oyun pencerelerini kapatıp tekrar deneyin.')
    sys.exit(1)

adres = 'http://127.0.0.1:%d/index.html' % port
print('  KESIR CARKI calisiyor:', adres)
print('  Oyun bitene kadar bu pencereyi KAPATMAYIN.')
threading.Timer(1.0, lambda: webbrowser.open(adres)).start()
try:
    sunucu.serve_forever()
except KeyboardInterrupt:
    pass
