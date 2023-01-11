# ipfs-cid

[![pypi](https://img.shields.io/pypi/v/ipfs-cid)](https://pypi.org/project/ipfs-cid/)
[![test](https://github.com/thunderstore-io/ipfs-cid/workflows/Test/badge.svg)](https://github.com/thunderstore-io/ipfs-cid/actions)
[![codecov](https://codecov.io/gh/thunderstore-io/ipfs-cid/branch/master/graph/badge.svg?token=6lS3pEHvIw)](https://codecov.io/gh/thunderstore-io/ipfs-cid)
[![python-versions](https://img.shields.io/pypi/pyversions/ipfs-cid.svg)](https://pypi.org/project/ipfs-cid/)

A library for building IPFS CID v1 compatible content identifiers using fixed
encoding parameters.

## Usage

### Get CID from bytes

All at once

```python
from ipfs_cid import cid_sha256_hash

data = b"Hello world"
result = cid_sha256_hash(data)
assert result == "bafkreide5semuafsnds3ugrvm6fbwuyw2ijpj43gwjdxemstjkfozi37hq"
```

In chunks with a generator

```python
from typing import Iterable
from io import BytesIO
from ipfs_cid import cid_sha256_hash_chunked

def as_chunks(stream: BytesIO, chunk_size: int) -> Iterable[bytes]:
    while len((chunk := stream.read(chunk_size))) > 0:
        yield chunk

buffer = BytesIO(b"Hello world")
result = cid_sha256_hash_chunked(as_chunks(buffer, 4))
assert result == "bafkreide5semuafsnds3ugrvm6fbwuyw2ijpj43gwjdxemstjkfozi37hq"
```

### Wrap an existing SHA 256 checksum as a CID

**WARNING:** This will lead to an invalid CID if an invalid digest is provided.
This is not possible to validate against without the original data.

```python
from hashlib import sha256
from ipfs_cid import cid_sha256_wrap_digest

data = b"Hello world"
digest = sha256(data).digest()
result = cid_sha256_wrap_digest(digest)
assert result == "bafkreide5semuafsnds3ugrvm6fbwuyw2ijpj43gwjdxemstjkfozi37hq"
```

### Unwrap a compatible CID to a sha256 digest

**NOTE:** The `cid_sha256_unwrap_digest` function will throw an `AttributeError`
if the input CID is not using the same encoding parameters.

```python
from hashlib import sha256
from ipfs_cid import cid_sha256_unwrap_digest

data = b"Hello world"
digest = sha256(data).digest()

cid = "bafkreide5semuafsnds3ugrvm6fbwuyw2ijpj43gwjdxemstjkfozi37hq"
result = cid_sha256_unwrap_digest(cid)
assert result == digest
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
