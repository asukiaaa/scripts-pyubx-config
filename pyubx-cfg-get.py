#!/usr/bin/python3

import click
import threading
from serial import Serial
from pyubx2 import UBXMessage, UBXReader

@click.command("cli", no_args_is_help=True)
@click.option("--port", required=True, help="Serial port of ublox device")
@click.option("--key", required=True, help="Key to write", type=str)
@click.option("--layer", default=0, help="0: Volatile RAM, 1: Battery backed RAM (BBR), 2: External flash")
@click.option("--baudrate", default=38400, help="Communication speed")
def config_get(port, key, layer, baudrate):
    transaction = 0
    protfilter = 2 # 2: UBX
    if type(key) is str and key.startswith("0x"):
        key = int(key, 0)
    keys = [key]
    msg = UBXMessage.config_poll(layer, transaction, keys)
    serial = Serial(port, baudrate, timeout=5)
    ubr = UBXReader(serial, protfilter=protfilter)
    def run_read():
        # global parsed_data
        (raw_data, parsed_data) = ubr.read()
        print(parsed_data)
        # (raw_data, parsed_data) = ubr.read()
        # print(parsed_data)
    t1 = threading.Thread(target=run_read)
    t1.start()
    # keys = ["CFG_UART1_BAUDRATE", 0x40530001]
    # keys = ["CFG_TMODE_MODE"]
    # print(msg)
    serial.write(msg.serialize())

if __name__ == '__main__':
    config_get()
