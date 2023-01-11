from base64 import b32decode, b32encode


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
