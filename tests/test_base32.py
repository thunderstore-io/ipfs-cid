import pytest

from ipfs_cid.encode import Base32Multibase


# Sourced from https://github.com/multiformats/multibase/tree/master/tests
@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (b"yes mani !", "bpfsxgidnmfxgsibb"),
        (b"hello world", "bnbswy3dpeB3W64TMMQ"),
        (b"\x00yes mani !", "bab4wk4zanvqw42jaee"),
        (b"\x00\x00yes mani !", "baaahszltebwwc3tjeaqq"),
    ],
)
def test_base32_encode_decode(data: bytes, expected: str):
    encoded = Base32Multibase.encode(data)
    assert encoded == expected.lower()
    assert Base32Multibase.decode(encoded) == data
    assert Base32Multibase.decode(expected) == data


def test_base32_decode_invalid():
    with pytest.raises(AttributeError, match="Invalid Multibase32 string:"):
        Base32Multibase.decode("amogus")
