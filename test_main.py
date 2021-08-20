from fastapi.testclient import TestClient
from main import user_info
from qldb.querying import *
from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/api/user_info")
    assert response.status_code == 200
    assert response.json() == {"Name": Person_Name,"Credit":Credit_Number,"Curr_Available":Current_Available_Amount}