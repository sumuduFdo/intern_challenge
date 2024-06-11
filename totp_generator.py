import hmac
import hashlib
import time

from typing import Any

def truncate(hmac_sha: str, digits: int = 10) -> str:
    offset = hmac_sha[-1] & 0XF
    code = (
        (hmac_sha[offset] & 0x7F) << 24
        | (hmac_sha[offset + 1] & 0xFF) << 16
        | (hmac_sha[offset + 2] & 0xFF) << 8
        | (hmac_sha[offset + 3] & 0xFF)
    )
    str_code = str(code).zfill(digits)
    return str_code[-digits:]


""" Generate HMAC OTP for a given seret"""
def generate_hotp(k: int, c: int, digest: Any = hashlib.sha1, digits: int = 10) -> str:
    if c < 0:
        raise ValueError("Time code must be a positive integer")
    
    # byte value conversion of secret key and counter value
    k_bytes = bytes(k, "utf-8")
    c_bytes = c.to_bytes(8)

    
    hmac_sha = hmac.new(k_bytes, c_bytes, digestmod=digest).digest()
    return truncate(hmac_sha, digits)

def generate_totp(k: int, time_ref: int = 0, time_step: int = 30, digest: Any = hashlib.sha1, digits: int = 10) -> str:

    """ 
    calculate time based counter value for TOTP implementation 
    where counter value is derived from time reference and a time step value
    respectively 0 and 30 in the specified case
    """
    c = int((int(time.time()) - time_ref) / time_step)
    totp = generate_hotp(k, c, digest=hashlib.sha512, digits=10)
    return totp