from jose import jwt

SECRET_KEY = "bd0a219ba836505fb46819edb1f8b59931cec12c33cb5fa5f151d9855ba2e327"
ALGORITHM = "HS256"


def encode_token(name: str, password: str):
    token_payload = {"sub": name,
                     "password": password}
    token = jwt.encode(token_payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except Exception as e:
        return {}
