"""Integration tests for endpoints"""

def test_example_endpoint(client):
    """Test our example API endpoint"""
    response = client.get('/example_endpoint')
    assert response.status_code == 200

    import json
    response_data = json.loads(response.data.decode('utf8'))
    assert "name" in response_data[0]
    assert "value" in response_data[0]
    assert isinstance(response_data[0]['name'], str)
    assert isinstance(response_data[0]['value'], str)