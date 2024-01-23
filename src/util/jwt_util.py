from jose import jwt

SECRET_KEY = "ja-ja_binks"
ALGORITHM = "HS256"


def encode_token(name: str, password: str):
    token_payload = {"name": name,
                     "password": password}
    token = jwt.encode(token_payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def decode_token(token: str):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithm=ALGORITHM)
        return decoded_token
    except Exception as e:
        return {}
