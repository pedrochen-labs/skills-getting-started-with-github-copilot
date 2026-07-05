from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_from_activity():
    signup_response = client.post(
        "/activities/Chess Club/signup?email=test@mergington.edu"
    )
    assert signup_response.status_code == 200

    delete_response = client.delete(
        "/activities/Chess Club/participants/test@mergington.edu"
    )
    assert delete_response.status_code == 200

    activities_response = client.get("/activities")
    assert activities_response.status_code == 200

    activities = activities_response.json()
    assert "test@mergington.edu" not in activities["Chess Club"]["participants"]
