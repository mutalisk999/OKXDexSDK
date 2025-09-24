#!/usr/bin/env python
# encoding: utf-8
import asyncio
import base64
import datetime
import hmac
from typing import Optional

from web3 import AsyncWeb3


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


async def check_allowance(_node_url: str, _token_addr: str, _owner_addr: str, _spender_addr: str) -> Optional[int]:
    token_abi = [
        {
            "constant": True,
            "inputs": [
                {"name": "_owner", "type": "address"},
                {"name": "_spender", "type": "address"}
            ],
            "name": "allowance",
            "outputs": [{"name": "", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        }
    ]

    w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(_node_url))
    connected = await w3.is_connected()
    if not connected:
        return None

    contract = w3.eth.contract(
        address=AsyncWeb3.to_checksum_address(_token_addr),
        abi=token_abi
    )

    _owner_addr = AsyncWeb3.to_checksum_address(_owner_addr)
    _spender_addr = AsyncWeb3.to_checksum_address(_spender_addr)

    res = await contract.functions.allowance(_owner_addr, _spender_addr).call()
    return res


async def estimate_gas(_node_url: str, _token_addr: str, _caller_addr: str, _value: int, _data: bytes) -> Optional[int]:
    w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(_node_url))
    connected = await w3.is_connected()
    if not connected:
        return None

    gas_limit = await w3.eth.estimate_gas({
        'from': AsyncWeb3.to_checksum_address(_caller_addr),
        'to': AsyncWeb3.to_checksum_address(_token_addr),
        'value': w3.to_wei(_value, 'wei'),
        'data': _data,
    })

    return gas_limit


if __name__ == "__main__":
    url = "https://public-bsc.nownodes.io"
    # token_addr = "0x55d398326f99059ff775485246999027b3197955"
    # owner_addr = "0x429752d5f5b595340381b158d80e846f9b20b6da"
    # spender_addr = "0x2c34a2fb1d0b4f55de51e1d0bdefaddce6b7cdd6"

    token_addr = "0xb1b5d6ae7cb737357766e924d11793f0dc4d4444"
    owner_addr = "0x429752d5f5b595340381b158d80e846f9b20b6da"
    spender_addr = "0x5c952063c7fc8610ffdb798152d69f0b9550762b"


    async def func1(_url, _token_addr, _owner_addr, _spender_addr):
        r = await check_allowance(_url, _token_addr, _owner_addr, _spender_addr)
        return r


    async def func2(_url, _token_addr, _owner_addr):
        data = "095ea7b30000000000000000000000005c952063c7fc8610ffdb798152d69f0b9550762b00000000000000000000000000000000000000000000898a57ccc69947eb4300"
        r = await estimate_gas(_url, _token_addr, _owner_addr, 0, bytes.fromhex(data))
        return r


    async def func():
        fut1 = func1(url, token_addr, owner_addr, spender_addr)
        fut2 = func2(url, token_addr, owner_addr)

        r1, r2 = await asyncio.gather(fut1, fut2)
        print(r1)
        print(r2)


    asyncio.run(func())
