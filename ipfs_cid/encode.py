import array
from hashlib import sha256
from typing import Iterable, Union

from ipfs_cid.base32 import Base32Multibase

MULTICODEC_CIDV1 = b"\x01"
MULTICODEC_RAW_BINARY = b"\x55"
MULTICODEC_SHA_2_256 = b"\x12"
MULTICODEC_SHA_2_256_LENGTH = b"\x20"

ENCODEABLE_TYPES = Union[bytes, bytearray, memoryview, array.array]


def cid_sha256_wrap_digest(digest: bytes):
    digestlen = len(digest).to_bytes(1, "big")
    if digestlen != MULTICODEC_SHA_2_256_LENGTH:  # pragma: no cover
        raise RuntimeError("Invalid digest length")
    multihash = b"" + MULTICODEC_SHA_2_256 + digestlen + digest
    encoded = b"" + MULTICODEC_CIDV1 + MULTICODEC_RAW_BINARY + multihash
    return Base32Multibase.encode(encoded)


def cid_sha256_hash(data: ENCODEABLE_TYPES) -> str:
    sha = sha256(data)
    return cid_sha256_wrap_digest(sha.digest())


def cid_sha256_hash_chunked(data: Iterable[ENCODEABLE_TYPES]) -> str:
    sha = sha256()
    for chunk in data:
        sha.update(chunk)
    return cid_sha256_wrap_digest(sha.digest())
