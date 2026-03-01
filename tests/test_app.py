from fastapi.testclient import TestClient
import pytest

from src.app import app, activities


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the global activities dict before each test.

    We take a shallow copy of the initial state so that tests can modify it
    without affecting other tests. Because the data structure is nested,
    we reinstanciate a fresh dictionary identical to the original contents.
    """
    # store original data for restoration
    original = {
        name: {
            **details,
            "participants": list(details["participants"]),
        }
        for name, details in activities.items()
    }
    yield
    activities.clear()
    activities.update(original)


@pytest.fixture

def client():
    return TestClient(app)


class TestRootEndpoint:
    def test_redirects_to_static_index(self, client):
        response = client.get("/")
        assert response.status_code == 307 or response.status_code == 200
        # depending on TestClient behavior, follow_redirects could be used
        # ensure final url content contains the HTML
        assert "<html" in response.text.lower()


class TestActivitiesEndpoint:
    def test_get_activities(self, client):
        response = client.get("/activities")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert "Chess Club" in data
        assert "schedule" in data["Chess Club"]


class TestSignupEndpoint:
    def test_successful_signup(self, client):
        email = "newstudent@mergington.edu"
        activity = "Chess Club"
        response = client.post(f"/activities/{activity}/signup", params={"email": email})
        assert response.status_code == 200
        assert email in activities[activity]["participants"]
        assert response.json()["message"] == f"Signed up {email} for {activity}"

    def test_signup_nonexistent_activity(self, client):
        response = client.post(
            "/activities/Nonexistent/signup", params={"email": "x@x"}
        )
        assert response.status_code == 404
        assert response.json()["detail"] == "Activity not found"

    def test_signup_duplicate(self, client):
        email = activities["Chess Club"]["participants"][0]
        activity = "Chess Club"
        response = client.post(f"/activities/{activity}/signup", params={"email": email})
        assert response.status_code == 400
        assert "already signed up" in response.json()["detail"]


class TestUnsubscribeEndpoint:
    def test_successful_unsubscribe(self, client):
        activity = "Chess Club"
        email = activities[activity]["participants"][0]
        response = client.delete(f"/activities/{activity}/unsubscribe", params={"email": email})
        assert response.status_code == 200
        assert email not in activities[activity]["participants"]
        assert response.json()["message"] == f"Unsubscribed {email} from {activity}"

    def test_unsubscribe_nonexistent_activity(self, client):
        response = client.delete(
            "/activities/Nonexistent/unsubscribe", params={"email": "x@x"}
        )
        assert response.status_code == 404
        assert response.json()["detail"] == "Activity not found"

    def test_unsubscribe_not_signed_up(self, client):
        activity = "Chess Club"
        # choose an email that is not already registered
        email = "not@registered.edu"
        response = client.delete(f"/activities/{activity}/unsubscribe", params={"email": email})
        assert response.status_code == 400
        assert "not signed up" in response.json()["detail"]
