from app import create_app

flask_app = create_app()

def test_home_page():
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200

def test_encode_page():
    with flask_app.test_client() as test_client:
        response = test_client.get('/encode')
        assert response.status_code == 200
