from typing import Callable

import pytest

from ipfs_cid import encode_cid_v1


# Comparison targets were generated with Kubo CLI
@pytest.mark.parametrize(
    ("data_generator", "expected"),
    [
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
    ],
)
def test_encode_cid_v1(data_generator: Callable[[], bytes], expected: str):
    data = data_generator()
    assert encode_cid_v1(data) == expected
