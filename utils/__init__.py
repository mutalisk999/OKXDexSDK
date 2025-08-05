#!/usr/bin/env python
# encoding: utf-8
import base64
import datetime
import hmac


# ISO-8601 format timestamp
def get_time_now_iso_8601() -> str:
    ts_iso_8601 = datetime.datetime.utcnow().isoformat(timespec='milliseconds') + "Z"
    return ts_iso_8601


# calc HMAC256 signature
def calc_ok_access_sign(secret_key: str, utc_ts_iso_8601: str, method: str,
                        request_path: str, body: str = "") -> str:
    if method.upper() == "GET":
        body = ""

    prehash_string = "".join([utc_ts_iso_8601, method, request_path, body])
    signature = hmac.new(secret_key.encode(), prehash_string.encode(), 'sha256').digest()
    ok_access_sign = base64.b64encode(signature).decode()
    return ok_access_sign
