# Comparison targets were generated with Kubo CLI
TEST_SETS = [
    (
        lambda: b"Hello world",
        "bafkreide5semuafsnds3ugrvm6fbwuyw2ijpj43gwjdxemstjkfozi37hq",
    ),
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
