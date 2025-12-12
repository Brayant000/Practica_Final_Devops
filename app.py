from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'message': '¡Hola Mundo DevOps!',
        'status': 'success',
        'version': '1.0.0'
    })

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'devops-practice-app'
    })

@app.route('/info')
def app_info():
    return jsonify({
        'app': 'DevOps Practice Final',
        'author': 'Estudiante DevOps',
        'environment': os.getenv('ENVIRONMENT', 'development')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)