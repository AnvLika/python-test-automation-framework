from src.api_client import ApiClient

api = ApiClient()

def test_get_users_list():
    """Test GET /users"""
    response = api.get("users")
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data, list)
    assert len(json_data) > 0

def test_create_user():
    """Test POST /users"""
    payload = {"name": "Alla", "job": "QA Automation"}
    response = api.post("users", data=payload)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["name"] == "Alla"