import pytest
import json
from certnode_api import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_api_logic_validation():
    payload = {"text": "If it rains, the ground gets wet."}
    response = client.post("/validate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "validation_passed" in data
