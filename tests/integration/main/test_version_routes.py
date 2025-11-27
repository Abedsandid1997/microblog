"""
Test routes for routes for authorizing users, app/main/routes
"""
# pylint: disable=redefined-outer-name,unused-argument



def test_version_route(client, app_version_response):
    """
    Test that /version returns JSON with 'version' field.
    """
    response = client.get("/version")
    assert response.status_code == 200

    data = response.get_json()
    assert "version" in data
    assert data["version"] == "test-version"
