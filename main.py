import tkinter as tk
import logging
from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex import BitmexClient
import config

from interface.root_component import Root

logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler("info.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':


    # HERE INSERT YOUR API KEYS
    binance = BinanceFuturesClient("61f9472a2e2b9027ea5fa69045a83b62adc2706d23ff9b89c0550bbe5d9c55e5", "a8afaf411b4410aa0942af1a289989826595f5f21abbf9975b2fea67078de6c2", True)
    bitmex = BitmexClient("bT1DPuWY35kcmX7Zp_p8MRQl", "9mH13sOVtW_QUs2Kms247r9wLmQDjAZ_ls3J1sdIxO0pZmzD", True)

    root = Root(binance, bitmex)
    root.mainloop() 