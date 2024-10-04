"""Additional Notes

- Fixtures: For handling test dependencies, state, and reusable functionality
- Marks: For categorizing tests and limiting access to external resources
- Parametrization: For reducing duplicated code between tests
- Durations: For identifying your slowest tests
- Plugins: For integrating with other frameworks and testing tools


"""

from flask.testing import FlaskClient, FlaskCliRunner
from werkzeug.test import TestResponse

base_url = "https://reqres.in"


def test_get_request(client: FlaskClient) -> None:
    response: TestResponse = client.get(f"{base_url}/api/users")
    assert response.status_code == 200


def test_post_request(client: FlaskClient) -> None:
    response: TestResponse = client.post(
        f"{base_url}/api/users",
        data={
            "name": "Louis-Ferdinand Celine",
            "job": "French Novelist",
        },
    )
    assert response.status_code == 201
