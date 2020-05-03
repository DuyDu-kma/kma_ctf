from KMActf.utils.crypto import hash_password as hp
from KMActf.utils.crypto import sha256 as sha
from KMActf.utils.crypto import verify_password as vp


def hash_password(p):
    print(
        "This function will be deprecated in a future release. Please update to KMActf.utils.crypto.hash_password"
    )
    return hp(p)


def check_password(p, hash):
    print(
        "This function will be deprecated in a future release. Please update to KMActf.utils.crypto.verify_password"
    )
    return vp(p, hash)


def sha256(p):
    print(
        "This function will be deprecated in a future release. Please update to KMActf.utils.crypto.sha256"
    )
    return sha(p)
