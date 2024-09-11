import pytest
import requests

BASE_URL = "https://qa-internship.avito.com/api/1"

# Тесты для создания объявления
def test_create_item_success():
    url = f"{BASE_URL}/item"
    data = {
        "name": "Телефон",
        "price": 85566,
        "sellerId": 3452,
        "statistics": {
            "contacts": 32,
            "like": 35,
            "viewCount": 14
        }
    }
    response = requests.post(url, json=data)
    assert response.status_code == 201  # Ожидается 201 Created
    response_data = response.json()
    assert 'id' in response_data  # Проверьте, что возвращается ID нового объявления

def test_create_item_missing_fields():
    url = f"{BASE_URL}/item"
    data = {
        "name": "Телефон"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400  # Ожидается 400 Bad Request
    response_data = response.json()
    assert 'code' in response_data
    assert response_data['code'] == 400
    assert 'message' in response_data
    assert response_data['message'] == 'Required fields are missing'

# Тесты для получения объявления по идентификатору
def test_get_item_success():
    item_id = "7a8fe969-2a57-468e-82c9-1982d22023c5"  # Убедитесь, что этот ID существует в вашей системе
    url = f"{BASE_URL}/item/{item_id}"
    response = requests.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, dict)  # Ожидается один объект
    assert 'name' in response_data

def test_get_item_not_found():
    item_id = "invalid-id"
    url = f"{BASE_URL}/item/{item_id}"
    response = requests.get(url)
    assert response.status_code == 404
    response_data = response.json()
    assert 'message' in response_data  # Проверка, что возвращается сообщение об ошибке
    assert response_data['message'] == 'Item not found'

# Тесты для получения всех объявлений по идентификатору продавца
def test_get_items_by_seller_success():
    seller_id = 3452  # Убедитесь, что у этого продавца есть объявления
    url = f"{BASE_URL}/{seller_id}/item"
    response = requests.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)

def test_get_items_by_seller_not_found():
    seller_id = 999999  # Убедитесь, что у этого продавца нет объявлений
    url = f"{BASE_URL}/{seller_id}/item"
    response = requests.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)
    # Проверьте, что список не содержит объявлений или проверяйте его содержимое по-другому
    assert len(response_data) == 0  # Убедитесь, что список пуст, если это ожидаемо

