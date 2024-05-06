import pytest
from app import app, db, Product

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_products(client):
    response = client.get('/products')
    assert response.status_code == 200

def test_get_product(client):
    response = client.get('/products/1')
    assert response.status_code == 200

def test_add_product(client):
    response = client.post('/products', json={"title": "New Product", "price": 99.99})
    assert response.status_code == 201

def test_update_product(client):
    response = client.put('/products/1', json={"title": "Updated Product"})
    assert response.status_code == 200

def test_delete_product(client):
    response = client.delete('/products/1')
    assert response.status_code == 200
