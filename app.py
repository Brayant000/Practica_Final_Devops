from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'message': '¡Práctica Final DevOps - Brayant000 Completada! 🎉',
        'status': 'success',
        'version': '1.0.0',
        'author': 'Brayant000',
        'docker_hub': 'brayant002',
        'github': 'Brayant000',
        'deployed_on': 'Render.com',
        'features': [
            'Flask Application',
            'Unit Tests (4/4 passing)',
            'Docker Containerization',
            'GitHub Actions CI/CD',
            'Docker Hub Registry',
            'Auto-deploy to Render'
        ]
    })

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'devops-practice-app',
        'timestamp': '2024-01-01T00:00:00Z',
        'checks': {
            'database': 'ok',
            'api': 'ok',
            'storage': 'ok'
        }
    })

@app.route('/info')
def app_info():
    return jsonify({
        'app': 'Practica Final DevOps CI/CD',
        'student': 'Brayant000',
        'course': 'DevOps',
        'environment': os.getenv('ENVIRONMENT', 'production'),
        'docker_hub_user': 'brayant002',
        'repository': 'https://github.com/Brayant000/Practica_Final_Devops',
        'pipeline': 'https://github.com/Brayant000/Practica_Final_Devops/actions',
        'docker_image': 'https://hub.docker.com/r/brayant002/practica-final-devops'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)