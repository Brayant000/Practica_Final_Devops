from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)

# HTML Template para la página principal
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Práctica Final DevOps</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 20px;
            padding: 50px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            text-align: center;
            max-width: 600px;
            width: 100%;
        }
        .avatar {
            width: 120px;
            height: 120px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 50%;
            margin: 0 auto 30px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 50px;
            color: white;
        }
        h1 {
            color: #333;
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        .matricula {
            color: #667eea;
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 20px;
        }
        .practica {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 30px;
            border-radius: 50px;
            font-size: 1.2rem;
            font-weight: bold;
            display: inline-block;
            margin-bottom: 30px;
        }
        .features {
            text-align: left;
            background: #f8f9fa;
            padding: 25px;
            border-radius: 15px;
            margin-top: 20px;
        }
        .features h3 {
            color: #667eea;
            margin-bottom: 15px;
            text-align: center;
        }
        .features ul {
            list-style: none;
        }
        .features li {
            padding: 8px 0;
            color: #555;
            border-bottom: 1px solid #eee;
        }
        .features li:last-child {
            border-bottom: none;
        }
        .features li::before {
            content: "✅ ";
        }
        .status {
            margin-top: 20px;
            padding: 10px 20px;
            background: #d4edda;
            color: #155724;
            border-radius: 10px;
            font-weight: 600;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="avatar">👨‍💻</div>
        <h1>JoseRaulPayanSoler</h1>
        <p class="matricula">Matrícula: 20231034</p>
        <div class="practica">🚀 Práctica Final DevOps</div>
        
        <div class="features">
            <h3>CI/CD Pipeline Implementado</h3>
            <ul>
                <li>Aplicación Flask</li>
                <li>Pruebas Unitarias (pytest)</li>
                <li>Contenedor Docker</li>
                <li>GitHub Actions CI/CD</li>
                <li>Docker Hub Registry</li>
                <li>Deploy en Render</li>
            </ul>
        </div>
        
        <div class="status">✨ Aplicación funcionando correctamente</div>
    </div>
</body>
</html>
'''

@app.route('/')
def hello_world():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api')
def api_info():
    """Endpoint JSON para verificación programática"""
    return jsonify({
        'message': '¡Práctica Final DevOps - JoseRaulPayanSoler Completada! 🎉',
        'status': 'success',
        'version': '1.0.0',
        'author': 'JoseRaulPayanSoler',
        'matricula': '20231034',
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
        'student': 'JoseRaulPayanSoler',
        'matricula': '20231034',
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
        'student': 'JoseRaulPayanSoler',
        'matricula': '20231034',
        'course': 'DevOps',
        'environment': os.getenv('ENVIRONMENT', 'production')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)