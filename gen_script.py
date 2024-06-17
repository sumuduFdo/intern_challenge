"""
This is a script that is written with direct reference to PyOTP implementation
without any modifications to the functions or their implemntations
"""
import datetime
import hashlib
import calendar
import time
import hmac
import base64

from typing import Any


def timecode(for_time: datetime.datetime, time_step: int) -> int:
    if for_time.tzinfo:
        return int(calendar.timegm(for_time.utctimetuple()) / time_step)
    else:
        return int(time.mktime(for_time.timetuple()) / time_step)


def pad_secret(k: str) -> bytes:
    secret = k
    padding = len(secret) % 8
    if padding != 0:
        secret += "=" * (8-padding)
    return base64.b32decode(secret, casefold=True)


def int_to_bytestr(i: int, padding: int = 8) -> bytes:
    """
    Turns an integer to the OATH specified bytestring, 
    which is fed to the HMAC along with the secret
    """
    result = bytearray()
    while i != 0:
        result.append(i & 0xFF)
        i >>= 8
    return bytes(bytearray(reversed(result))).rjust(padding, b"\0")


def generate_otp(k: str, time_code: int, digest: Any = hashlib.sha512, digits: int = 10):
    if time_code < 0:
        raise ValueError("Time code must be positive integer")

    hmac_sha = hmac.new(pad_secret(k), int_to_bytestr(
        time_code), digestmod=digest)
    hmac_sha_hash = bytearray(hmac_sha.digest())
    offset = hmac_sha_hash[-1] & 0XF
    code = (
        (hmac_sha_hash[offset] & 0x7F) << 24
        | (hmac_sha_hash[offset + 1] & 0xFF) << 16
        | (hmac_sha_hash[offset + 2] & 0xFF) << 8
        | (hmac_sha_hash[offset + 3] & 0xFF)
    )
    str_code = str(10_000_000_000 + (code % 10**digits))
    return str_code[-digits : ]

def generate_totp(k: str, time_step: int = 30, digest: Any = hashlib.sha512, digits: int = 10):
    c = timecode(datetime.datetime.now(), time_step)
    totp = generate_otp(k, c, hashlib.sha512, 10)
    return totp
