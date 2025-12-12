import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world_endpoint(client):
    """Test para el endpoint principal"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == '¡Hola Mundo DevOps!'
    assert data['status'] == 'success'

def test_health_endpoint(client):
    """Test para el endpoint de health check"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_info_endpoint(client):
    """Test para el endpoint de información"""
    response = client.get('/info')
    assert response.status_code == 200
    data = response.get_json()
    assert 'app' in data
    assert 'environment' in data

def test_not_found_endpoint(client):
    """Test para endpoint no existente"""
    response = client.get('/nonexistent')
    assert response.status_code == 404