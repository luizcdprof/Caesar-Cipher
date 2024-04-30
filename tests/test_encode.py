from app import create_app
from app.encode import encode_function

flask_app = create_app()

def test_encode_function():
    encoded_message = encode_function("ABCD", 2)
    assert encoded_message == "CDEF"
