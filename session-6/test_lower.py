def lowercase(data):
    return data.lower()


def test_lowercase():
    """Very Very Very Very Very long long long long name name name name"""
    assert lowercase("TEAM KAIZEND") == "team kaizend"


def test_lowercase2():
    assert lowercase("Team Kaizend") == "team kaizend"
