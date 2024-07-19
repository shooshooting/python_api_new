from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_get_data():
    response = client.get("/api/data")
    assert response.status_code == 200
    assert response.json() == [
        {
            "member_id": "001",
            "name": "Alice Chen",
            "email": "alice.chen@example.com",
            "phone": "0912345678",
            "address": "123 Main St, Taipei City, Taiwan",
            "join_date": "2023-05-15"
        },
        {
            "member_id": "002",
            "name": "Bob Lin",
            "email": "bob.lin@example.com",
            "phone": "0923456789",
            "address": "456 Oak St, Kaohsiung City, Taiwan",
            "join_date": "2023-06-20"
        },
        {
            "member_id": "003",
            "name": "Cathy Wang",
            "email": "cathy.wang@example.com",
            "phone": "0934567890",
            "address": "789 Pine St, Tainan City, Taiwan",
            "join_date": "2023-07-10"
        },
        {
            "member_id": "004",
            "name": "David Lee",
            "email": "david.lee@example.com",
            "phone": "0945678901",
            "address": "101 Maple St, Taichung City, Taiwan",
            "join_date": "2023-08-05"
        }
    ]


