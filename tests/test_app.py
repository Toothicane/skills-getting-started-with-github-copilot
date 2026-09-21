from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email():
    response = client.delete("/activities/Chess Club/unregister?email=daniel@mergington.edu")

    assert response.status_code == 200
    assert response.json()["message"] == "Unregistered daniel@mergington.edu from Chess Club"

    updated = client.get("/activities").json()
    assert "daniel@mergington.edu" not in updated["Chess Club"]["participants"]


def test_unregister_missing_participant_returns_404():
    response = client.delete("/activities/Chess Club/unregister?email=missing@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in activity"
