#!/usr/bin/env python
# encoding: utf-8
import json
import os
from enum import StrEnum
import aiohttp
import asyncio

from _decimal import Decimal
from aiohttp_socks import ProxyConnector
from dotenv import load_dotenv

from utils import get_time_now_iso_8601, calc_ok_access_sign

DOMAIN_NAME = "https://web3.okx.com"


class SwapMode(StrEnum):
    exactIn: str = "exactIn"
    exactOut: str = "exactOut"


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


# quote
async def get_aggregator_quote(api_key: str, secret_key: str, pass_phrase: str,
                               chain_idx: int, swap_mode: SwapMode, amount: int,
                               from_token_contract_addr: str, to_token_contract_addr: str, slippage: Decimal,
                               timeout: int) -> dict:
    # SwapMode: exactIn => amount: sell exact amount
    # SwapMode: exactOut => amount: buy exact amount
    request_path = "/api/v5/dex/aggregator/quote?chainIndex={}&swapMode={}&amount={}&fromTokenAddress={}&toTokenAddress={}&slippage={}".format(
        chain_idx, swap_mode.value, amount, from_token_contract_addr, to_token_contract_addr, slippage)
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


async def get_aggregator_swap(api_key: str, secret_key: str, pass_phrase: str,
                              chain_idx: int, swap_mode: SwapMode, amount: int,
                              from_token_contract_addr: str, to_token_contract_addr: str,
                              user_addr: str, slippage: Decimal,
                              timeout: int) -> dict:
    # SwapMode: exactIn => amount: sell exact amount
    # SwapMode: exactOut => amount: buy exact amount
    request_path = "/api/v5/dex/aggregator/swap?chainIndex={}&swapMode={}&amount={}&fromTokenAddress={}&toTokenAddress={}&userWalletAddress={}&slippage={}".format(
        chain_idx, swap_mode.value, amount, from_token_contract_addr, to_token_contract_addr, user_addr, slippage)
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


# history
async def get_aggregator_history(api_key: str, secret_key: str, pass_phrase: str,
                                 chain_idx: int, tx_hash: str, timeout: int) -> dict:
    request_path = "/api/v5/dex/aggregator/history?chainIndex={}&txHash={}".format(chain_idx, tx_hash)
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


async def get_gas_limit(api_key: str, secret_key: str, pass_phrase: str,
                        chain_idx: int, from_addr: str, to_addr: str,
                        value: int, input_data: str, timeout: int) -> dict:
    request_path = "/api/v5/dex/pre-transaction/gas-limit"
    ts_iso_8601 = get_time_now_iso_8601()

    body = {
        "chainIndex": chain_idx,
        "fromAddress": from_addr,
        "toAddress": to_addr,
        "txAmount": value,
        "extJson": {
            "inputData": input_data,
        }
    }

    ok_access_sign = calc_ok_access_sign(secret_key, ts_iso_8601, "POST", request_path, json.dumps(body))
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
        async with session.post(url, headers=headers, json=body, timeout=client_timeout) as response:
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

        r = await get_aggregator_quote(api_key, secret_key, pass_phrase, 1, SwapMode.exactIn,
                                       10000000000000000000,
                                       "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
                                       "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", Decimal("0.005"),
                                       timeout)
        print(r)

        r = await get_aggregator_swap(api_key, secret_key, pass_phrase, 1, SwapMode.exactIn,
                                      10000000000000000000,
                                      "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
                                      "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                                      "0x429752d5f5b595340381b158d80e846f9b20b6da",
                                      Decimal("0.005"),
                                      timeout)
        print(r)

        r = await get_aggregator_history(api_key, secret_key, pass_phrase, 784,
                                         "5GePcvqEakoUtArW8PHULDSQds95vcgeiTznvbnb8hCV", timeout)
        print(r)


    async def func2(api_key: str, secret_key: str, pass_phrase: str):
        timeout = 10
        fut1 = get_aggregator_supported_chain(api_key, secret_key, pass_phrase, 1, timeout)
        fut2 = get_aggregator_history(api_key, secret_key, pass_phrase, 784,
                                      "5GePcvqEakoUtArW8PHULDSQds95vcgeiTznvbnb8hCV", timeout)
        r1, r2 = await asyncio.gather(fut1, fut2)
        print(r1)
        print(r2)


    async def func3(api_key: str, secret_key: str, pass_phrase: str):
        timeout = 10
        r = await get_gas_limit(api_key, secret_key, pass_phrase, 1,
                                "0x429752d5f5b595340381b158d80e846f9b20b6da",
                                "0x55d398326f99059ff775485246999027b3197955", 0,
                                "095ea7b30000000000000000000000005c952063c7fc8610ffdb798152d69f0b9550762b00000000000000000000000000000000000000000000898a57ccc69947eb4300",
                                timeout)
        print(r)


    load_dotenv("../.env")
    apikey = str(os.getenv("API_KEY"))
    secretkey = str(os.getenv("API_SECRET"))
    passphrase = str(os.getenv("API_PASSPHRASE"))

    asyncio.run(func(apikey, secretkey, passphrase))
    # asyncio.run(func2(apikey, secretkey, passphrase))
    # asyncio.run(func3(apikey, secretkey, passphrase))
