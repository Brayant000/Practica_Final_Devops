import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world_endpoint(client):
    """Test para el endpoint principal - página HTML"""
    response = client.get('/')
    assert response.status_code == 200
    # Verificar que es HTML y contiene la información del estudiante
    html_content = response.data.decode('utf-8')
    assert 'JoseRaulPayanSoler' in html_content
    assert '20231034' in html_content
    assert 'Práctica Final DevOps' in html_content

def test_api_endpoint(client):
    """Test para el endpoint API JSON"""
    response = client.get('/api')
    assert response.status_code == 200
    data = response.get_json()
    assert 'JoseRaulPayanSoler' in data['message']
    assert data['status'] == 'success'
    assert data['matricula'] == '20231034'
    assert 'features' in data
    assert len(data['features']) == 6

def test_health_endpoint(client):
    """Test para el endpoint de health check"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['student'] == 'JoseRaulPayanSoler'
    assert data['matricula'] == '20231034'
    assert 'checks' in data

def test_info_endpoint(client):
    """Test para el endpoint de información"""
    response = client.get('/info')
    assert response.status_code == 200
    data = response.get_json()
    assert data['student'] == 'JoseRaulPayanSoler'
    assert data['matricula'] == '20231034'

def test_not_found_endpoint(client):
    """Test para endpoint no existente"""
    response = client.get('/nonexistent')
    assert response.status_code == 404