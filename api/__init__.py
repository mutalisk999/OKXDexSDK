#!/usr/bin/env python
# encoding: utf-8

import os

import aiohttp
import asyncio
from aiohttp_socks import ProxyConnector
from dotenv import load_dotenv

from utils import get_time_now_iso_8601, calc_ok_access_sign

DOMAIN_NAME = "https://web3.okx.com"


# chain
async def get_aggregator_supported_chain(api_key: str, secret_key: str, pass_phrase: str,
                                         chain_idx: int, timeout: int) -> dict:
    request_path = "/api/v5/dex/aggregator/supported/chain?chainIndex={}".format(chain_idx)
    ts_iso_8601 = get_time_now_iso_8601()
    ok_access_sign = calc_ok_access_sign(secret_key, ts_iso_8601, "GET", request_path)
    headers = {
        "OK-ACCESS-KEY": api_key,
        "OK-ACCESS-SIGN": ok_access_sign,
        "OK-ACCESS-PASSPHRASE": pass_phrase,
        "OK-ACCESS-TIMESTAMP": ts_iso_8601,
    }
    url = "".join([DOMAIN_NAME, request_path])

    connector = None
    proxy_url = os.getenv("CLIENT_PROXY")

    if proxy_url is not None and proxy_url != "":
        connector = ProxyConnector.from_url(proxy_url)

    client_timeout = aiohttp.ClientTimeout(total=timeout)

    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url, headers=headers, timeout=client_timeout) as response:
            return await response.json()


# all-tokens
async def get_aggregator_all_tokens(api_key: str, secret_key: str, pass_phrase: str,
                                    chain_idx: int, timeout: int) -> dict:
    request_path = "/api/v5/dex/aggregator/all-tokens?chainIndex={}".format(chain_idx)
    ts_iso_8601 = get_time_now_iso_8601()
    ok_access_sign = calc_ok_access_sign(secret_key, ts_iso_8601, "GET", request_path)
    headers = {
        "OK-ACCESS-KEY": api_key,
        "OK-ACCESS-SIGN": ok_access_sign,
        "OK-ACCESS-PASSPHRASE": pass_phrase,
        "OK-ACCESS-TIMESTAMP": ts_iso_8601,
    }
    url = "".join([DOMAIN_NAME, request_path])

    connector = None
    proxy_url = os.getenv("CLIENT_PROXY")

    if proxy_url is not None and proxy_url != "":
        connector = ProxyConnector.from_url(proxy_url)

    client_timeout = aiohttp.ClientTimeout(total=timeout)

    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url, headers=headers, timeout=client_timeout) as response:
            return await response.json()


# get-liquidity
async def get_aggregator_liquidity(api_key: str, secret_key: str, pass_phrase: str,
                                   chain_idx: int, timeout: int) -> dict:
    request_path = "/api/v5/dex/aggregator/get-liquidity?chainIndex={}".format(chain_idx)
    ts_iso_8601 = get_time_now_iso_8601()
    ok_access_sign = calc_ok_access_sign(secret_key, ts_iso_8601, "GET", request_path)
    headers = {
        "OK-ACCESS-KEY": api_key,
        "OK-ACCESS-SIGN": ok_access_sign,
        "OK-ACCESS-PASSPHRASE": pass_phrase,
        "OK-ACCESS-TIMESTAMP": ts_iso_8601,
    }
    url = "".join([DOMAIN_NAME, request_path])

    connector = None
    proxy_url = os.getenv("CLIENT_PROXY")

    if proxy_url is not None and proxy_url != "":
        connector = ProxyConnector.from_url(proxy_url)

    client_timeout = aiohttp.ClientTimeout(total=timeout)

    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url, headers=headers, timeout=client_timeout) as response:
            return await response.json()


# approve-transaction
async def get_approve_transaction(api_key: str, secret_key: str, pass_phrase: str,
                                  chain_idx: int, token_contract_addr: str,
                                  approve_amount: str, timeout: int) -> dict:
    request_path = "/api/v5/dex/aggregator/approve-transaction?chainIndex={}&tokenContractAddress={}&approveAmount={}".format(
        chain_idx, token_contract_addr, approve_amount)
    ts_iso_8601 = get_time_now_iso_8601()
    ok_access_sign = calc_ok_access_sign(secret_key, ts_iso_8601, "GET", request_path)
    headers = {
        "OK-ACCESS-KEY": api_key,
        "OK-ACCESS-SIGN": ok_access_sign,
        "OK-ACCESS-PASSPHRASE": pass_phrase,
        "OK-ACCESS-TIMESTAMP": ts_iso_8601,
    }
    url = "".join([DOMAIN_NAME, request_path])

    connector = None
    proxy_url = os.getenv("CLIENT_PROXY")

    if proxy_url is not None and proxy_url != "":
        connector = ProxyConnector.from_url(proxy_url)

    client_timeout = aiohttp.ClientTimeout(total=timeout)

    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url, headers=headers, timeout=client_timeout) as response:
            return await response.json()


if __name__ == "__main__":
    async def func(api_key: str, secret_key: str, pass_phrase: str):
        timeout = 10
        r = await get_aggregator_supported_chain(api_key, secret_key, pass_phrase, 1, timeout)
        print(r)

        r = await get_aggregator_all_tokens(api_key, secret_key, pass_phrase, 1, timeout)
        print(r)

        r = await get_aggregator_liquidity(api_key, secret_key, pass_phrase, 1, timeout)
        print(r)

        r = await get_approve_transaction(
            api_key, secret_key, pass_phrase, 1,
            "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", "100000", timeout)
        print(r)


    load_dotenv("../.env")
    apikey = str(os.getenv("API_KEY"))
    secretkey = str(os.getenv("API_SECRET"))
    passphrase = str(os.getenv("API_PASSPHRASE"))

    asyncio.run(func(apikey, secretkey, passphrase))
