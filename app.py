from flask import Flask, jsonify
from database.db import init_db
from routes.upload_route import upload_bp
from routes.download_route import download_bp
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

init_db()

app.register_blueprint(upload_bp, url_prefix='/uploads')
app.register_blueprint(download_bp, url_prefix='/downloads')


@app.route('/', methods=['GET'])
def index():
    """Rota raiz: serve para conferir se a API está no ar."""
    return jsonify({
        "status": "online",
        "endpoints": {
            "upload": "POST /uploads/upload",
            "download": "GET /downloads/download/<filename>"
        }
    }), 200


if __name__ == '__main__':
    # Uso local. Em producao o Render executa: gunicorn app:app
    debug = os.environ.get('FLASK_DEBUG', '0') == '1'
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=debug)
