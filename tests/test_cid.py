from hashlib import sha256
from typing import Callable

import pytest

from ipfs_cid import cid_sha256_unwrap_digest, cid_sha256_wrap_digest
from tests.data import TEST_SETS


def test_cid_sha256_wrap_digest_invalid_length():
    with pytest.raises(AttributeError, match="Invalid digest length"):
        cid_sha256_wrap_digest(b"\x00" * 40)


@pytest.mark.parametrize(
    "cid",
    [
        "bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi",
        "bafybeibnqmhw7bhvyalczhxzcgdhwk2lm3pgi4n2ctmpqgbnzyz6hpkkji",
        "bafkreif2why4bwbiadz3gfjoik2ywzmumcnmebmec4evy4spctrxxd3m5ysa",
    ],
)
def test_cid_sha256_unwrap_digest_unsupported_format(cid: str):
    with pytest.raises(AttributeError, match="Unsupported CID format"):
        cid_sha256_unwrap_digest(cid)


# Comparison targets were generated with Kubo CLI
@pytest.mark.parametrize(("data_generator", "expected"), TEST_SETS)
def test_cid_sha256_wrap_unwrap_digest(
    data_generator: Callable[[], bytes],
    expected: str,
):
    digest = sha256(data_generator()).digest()
    wrapped = cid_sha256_wrap_digest(digest)
    assert wrapped == expected
    unwrapped = cid_sha256_unwrap_digest(wrapped)
    assert unwrapped == digest
