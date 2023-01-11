from io import BytesIO
from typing import Callable, Iterable

import pytest

from ipfs_cid import cid_sha256_hash, cid_sha256_hash_chunked

# Comparison targets were generated with Kubo CLI
TEST_SETS = [
    (
        lambda: b"\x00" * 200000,
        "bafkreicmxpm34df2nbmdk5k7qj3vq4c5wwsbhrkjjq2cmlgslfdkoptvqi",
    ),
    (
        lambda: b"\x00" * 500000,
        "bafkreidlw2xpv2ve4girfzlgwrt4imaumorqwcqvxhecjcqa5wonrzmunm",
    ),
    (
        lambda: b"".join((x % 256).to_bytes(1, "big") for x in range(200000)),
        "bafkreighu7ltw2gscebl67lntprhwqigjf7pzaizejf6x66snm3vkqn544",
    ),
    (
        lambda: b"".join((x % 256).to_bytes(1, "big") for x in range(500000)),
        "bafkreia7ldhwiil4nra2ymrkz66tyq2zzdwlypgeqvunj6d7sqd6gpmko4",
    ),
]


@pytest.mark.parametrize(("data_generator", "expected"), TEST_SETS)
def test_cid_sha256_hash(data_generator: Callable[[], bytes], expected: str) -> None:
    data = data_generator()
    assert cid_sha256_hash(data) == expected


@pytest.mark.parametrize(("data_generator", "expected"), TEST_SETS)
def test_cid_sha256_hash_chunked(
    data_generator: Callable[[], bytes],
    expected: str,
) -> None:
    def as_chunks(stream: BytesIO, chunk_size: int) -> Iterable[bytes]:
        while len((chunk := stream.read(chunk_size))) > 0:
            yield chunk

    buffer = BytesIO(data_generator())
    assert cid_sha256_hash_chunked(as_chunks(buffer, 100)) == expected
