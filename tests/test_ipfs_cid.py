def test_module():
    from ipfs_cid.main import hello_world

    assert hello_world() == "Hello world"
