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
    assert 'Práctica Final DevOps - Brayant000' in data['message']
    assert data['status'] == 'success'
    assert 'features' in data
    assert len(data['features']) == 6

def test_health_endpoint(client):
    """Test para el endpoint de health check"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'checks' in data

def test_info_endpoint(client):
    """Test para el endpoint de información"""
    response = client.get('/info')
    assert response.status_code == 200
    data = response.get_json()
    assert data['student'] == 'Brayant000'
    assert data['docker_hub_user'] == 'brayant002'
    assert 'github.com/Brayant000' in data['repository']

def test_not_found_endpoint(client):
    """Test para endpoint no existente"""
    response = client.get('/nonexistent')
    assert response.status_code == 404