from passlib.hash import pbkdf2_sha256


def encode_password(password):
    hashed_password = pbkdf2_sha256.hash(password)
    return hashed_password


def decode_password(password, hashed_password):
    response = pbkdf2_sha256.verify(password, hashed_password)
    return response