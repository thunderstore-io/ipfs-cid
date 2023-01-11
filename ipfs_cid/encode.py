from base64 import b32decode, b32encode
from hashlib import sha256


class Base32Multibase:
    PREFIX = "b"

    @staticmethod
    def encode(data: bytes) -> str:
        b32 = b32encode(data).decode()
        return Base32Multibase.PREFIX + b32.lower().replace("=", "")

    @staticmethod
    def decode(data: str) -> bytes:
        if data[0] != Base32Multibase.PREFIX:
            raise AttributeError(f"Invalid Multibase32 string: {data}")
        data = data[1:]
        padding = (8 - (len(data) % 8)) % 8
        return b32decode(data.upper() + (padding * "="))


MULTICODEC_CIDV1 = b"\x01"
MULTICODEC_RAW_BINARY = b"\x55"
MULTICODEC_SHA_2_256 = b"\x12"
MULTICODEC_SHA_2_256_LENGTH = b"\x20"


def encode_cid_v1(data: bytes) -> str:
    sha = sha256()
    sha.update(data)
    digest = sha.digest()

    digestlen = len(digest).to_bytes(1, "big")
    if digestlen != MULTICODEC_SHA_2_256_LENGTH:  # pragma: no cover
        raise RuntimeError("Invalid digest length")
    multihash = b"" + MULTICODEC_SHA_2_256 + digestlen + digest
    encoded = b"" + MULTICODEC_CIDV1 + MULTICODEC_RAW_BINARY + multihash
    return Base32Multibase.encode(encoded)
