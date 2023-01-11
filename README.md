# ipfs-cid

[![pypi](https://img.shields.io/pypi/v/ipfs-cid)](https://pypi.org/project/ipfs-cid/)
[![test](https://github.com/thunderstore-io/ipfs-cid/workflows/Test/badge.svg)](https://github.com/thunderstore-io/ipfs-cid/actions)
[![codecov](https://codecov.io/gh/thunderstore-io/ipfs-cid/branch/master/graph/badge.svg?token=6lS3pEHvIw)](https://codecov.io/gh/thunderstore-io/ipfs-cid)

A library for building IPFS CID v1 compatible content identifiers using fixed
encoding parameters.

## Usage

```python
from ipfs_cid import encode_cid_v1

data = b"Hello world"
result = encode_cid_v1(data)
# result is now "bafkreide5semuafsnds3ugrvm6fbwuyw2ijpj43gwjdxemstjkfozi37hq"
```

## Encoding Format

[The CID spec](https://github.com/multiformats/cid) supports multiple different
encodings and hashing algorithms.

The resulting CID string is composed of the following components:

```
{multibase prefix} + multibase_encoded({cid version} + {content type} + {multihash})
```

This library always uses the following encoding parameters:

| multibase | CID version | Content Type | Multihash |
| --------- | ----------- | ------------ | --------- |
| base32    | cidv1       | raw          | sha2-256  |

More details about the formats below:

### Multibase

| encoding | code | description                           |
| -------- | ---- | ------------------------------------- |
| base32   | b    | rfc4648 case-insensitive - no padding |

### Multicodec

| name     | code | description                  |
| -------- | ---- | ---------------------------- |
| cidv1    | 0x01 | CID v1                       |
| sha2-256 | 0x12 | sha2-256 with 256 bit digest |
| raw      | 0x55 | raw binary                   |
