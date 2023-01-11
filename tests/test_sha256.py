from hashlib import sha256
from io import BytesIO
from typing import Callable, Iterable

import pytest

from ipfs_cid import cid_sha256_hash, cid_sha256_hash_chunked, cid_sha256_unwrap_digest
from tests.data import TEST_SETS


@pytest.mark.parametrize(("data_generator", "expected"), TEST_SETS)
def test_cid_sha256_hash(data_generator: Callable[[], bytes], expected: str) -> None:
    data = data_generator()
    expected_digest = sha256(data).digest()
    cid = cid_sha256_hash(data)
    assert cid == expected
    assert cid_sha256_unwrap_digest(cid) == expected_digest


@pytest.mark.parametrize(("data_generator", "expected"), TEST_SETS)
def test_cid_sha256_hash_chunked(
    data_generator: Callable[[], bytes],
    expected: str,
) -> None:
    def as_chunks(stream: BytesIO, chunk_size: int) -> Iterable[bytes]:
        while len((chunk := stream.read(chunk_size))) > 0:
            yield chunk

    data = data_generator()
    expected_digest = sha256(data).digest()
    buffer = BytesIO(data)
    cid = cid_sha256_hash_chunked(as_chunks(buffer, 100))
    assert cid == expected
    assert cid_sha256_unwrap_digest(cid) == expected_digest
