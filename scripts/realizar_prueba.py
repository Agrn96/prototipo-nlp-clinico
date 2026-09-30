"""Local interactive demo. Run with python realizar_prueba.py."""
import json
import os
import traceback
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from time import perf_counter
from nlp_pipeline import cargar_nlp

ROOT = Path(__file__).resolve().parent
LABELS = {'SINTOMA', 'DIAGNOSTICO', 'TRATAMIENTO', 'PROCEDIMIENTO'}

def main():
    os.chdir(ROOT)
    print('Cargando modelo y patrones...', flush=True)
    nlp = cargar_nlp()
    class Handler(BaseHTTPRequestHandler):
        def respond(self, status, payload, content_type='application/json; charset=utf-8'):
            body = payload if isinstance(payload, bytes) else json.dumps(payload, ensure_ascii=False).encode('utf-8')
            self.send_response(status)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        def do_GET(self):
            if self.path in ('/', '/index.html'):
                self.respond(200, (ROOT / 'demo.html').read_bytes(), 'text/html; charset=utf-8')
            else:
                self.respond(404, {'error': 'Página no encontrada'})
        def do_POST(self):
            if self.path != '/api/anotar':
                self.respond(404, {'error': 'Ruta no encontrada'})
                return
            try:
                length = int(self.headers.get('Content-Length', '0'))
                if not 0 < length <= 100000:
                    raise ValueError()
                data = json.loads(self.rfile.read(length))
                text = data.get('texto') if isinstance(data, dict) else None
                if not isinstance(text, str) or not text.strip() or len(text) > 5000:
                    raise ValueError()
            except (ValueError, UnicodeDecodeError):
                self.respond(400, {'error': 'Escribe una nota de entre 1 y 5000 caracteres.'})
                return
            try:
                start = perf_counter()
                doc = nlp(text)
                entities = [{'texto': e.text, 'etiqueta': e.label_, 'inicio': e.start_char, 'fin': e.end_char} for e in doc.ents if e.label_ in LABELS]
                result = {'texto': text, 'entidades': entities, 'tiempo_ms': round((perf_counter() - start) * 1000, 1)}
                (ROOT / 'outputs').mkdir(exist_ok=True)
                (ROOT / 'outputs' / 'resultado_prueba.json').write_text(json.dumps(entities, ensure_ascii=False, indent=2), encoding='utf-8')
                self.respond(200, result)
            except Exception:
                traceback.print_exc()
                self.respond(500, {'error': 'No se pudo procesar la nota. Revisa la terminal.'})
    server = HTTPServer(('127.0.0.1', 5000), Handler)
    print('Demo lista: http://localhost:5000 — Ctrl+C para detener', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()

if __name__ == '__main__':
    main()
