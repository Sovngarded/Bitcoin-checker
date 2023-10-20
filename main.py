import os

import requests
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv

load_dotenv()

BITCOIN_WALLET_ADDRESS = os.getenv('BITCOIN_WALLET_ADDRESS')


def check_bitcoin_balance(wallet_address):
    url = f"https://blockstream.info/api/address/{wallet_address}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        balance = data["chain_stats"]["funded_txo_sum"] / 100000000
        print(f"Balance =  {wallet_address}: {balance} BTC")


scheduler = BackgroundScheduler()
scheduler.add_job(check_bitcoin_balance, 'interval', seconds=1, args=[BITCOIN_WALLET_ADDRESS])
scheduler.start()

try:
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
