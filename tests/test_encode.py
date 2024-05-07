from app import create_app
from app.encode import encode

flask_app = create_app()

def test_encode_ABCD():
    encoded_message = encode("ABCD", 2)
    assert encoded_message == "CDEF"

def test_encode_TESTE():
    encoded_message = encode("TESTE", 2)
    assert encoded_message == "VGUVG"

def test_encode_XYZ():
    encoded_message = encode("XYZ", 2)
    assert encoded_message == "ZAB"

def test_encode_ABCD_negative():
    encoded_message = encode("XYZ", -2)
    assert encoded_message == "ZAB"
