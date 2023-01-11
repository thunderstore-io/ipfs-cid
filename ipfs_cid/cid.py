from ipfs_cid.base32 import Base32Multibase

MULTICODEC_CIDV1 = b"\x01"
MULTICODEC_RAW_BINARY = b"\x55"
MULTICODEC_SHA_2_256 = b"\x12"
MULTICODEC_SHA_2_256_LENGTH = b"\x20"

CID_PREFIX = b"".join(
    [
        MULTICODEC_CIDV1,
        MULTICODEC_RAW_BINARY,
        MULTICODEC_SHA_2_256,
        MULTICODEC_SHA_2_256_LENGTH,
    ],
)


def cid_sha256_wrap_digest(digest: bytes) -> str:
    digestlen = len(digest).to_bytes(1, "big")
    if digestlen != MULTICODEC_SHA_2_256_LENGTH:
        raise AttributeError("Invalid digest length")
    return Base32Multibase.encode(CID_PREFIX + digest)


def cid_sha256_unwrap_digest(cid: str) -> bytes:
    decoded = Base32Multibase.decode(cid)
    if decoded[: len(CID_PREFIX)] != CID_PREFIX:
        raise AttributeError("Unsupported CID format")
    digest = decoded[len(CID_PREFIX) :]
    if len(digest).to_bytes(1, "big") != MULTICODEC_SHA_2_256_LENGTH:
        raise AttributeError("Unsupported CID format")
    return digest
