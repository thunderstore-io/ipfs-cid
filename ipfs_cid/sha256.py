import array
from hashlib import sha256
from typing import Iterable, Union

from ipfs_cid.cid import cid_sha256_wrap_digest

ENCODEABLE_TYPES = Union[bytes, bytearray, memoryview, array.array]


def cid_sha256_hash(data: ENCODEABLE_TYPES) -> str:
    sha = sha256(data)
    return cid_sha256_wrap_digest(sha.digest())


def cid_sha256_hash_chunked(data: Iterable[ENCODEABLE_TYPES]) -> str:
    sha = sha256()
    for chunk in data:
        sha.update(chunk)
    return cid_sha256_wrap_digest(sha.digest())
