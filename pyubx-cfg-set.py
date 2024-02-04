#!/usr/bin/python3

import click
from serial import Serial
from pyubx2 import UBXMessage, UBXReader, ubxhelpers
import pyubx2.exceptions as ube

# ./pyubx-cfg-set.py --port /dev/ttyACM0 --key CFG_UART1_BAUDRATE --value 9600

# def is_valid_cfg_key_or_name(keyOrName: int | str) -> bool:
#     try:
#         if type(keyOrName) == str:
#             key = ubxhelpers.cfgname2key(keyOrName)
#         else:
#             name = ubxhelpers.cfgkey2name(keyOrName)
#     except ube.UBXMessageError as err:
#         print(err)
#         return False
#     return True

@click.command("cli", no_args_is_help=True)
@click.option("--port", required=True, help="Serial port of ublox device")
@click.option("--key", required=True, help="Key to write", type=str)
@click.option("--value", required=True, help="Value to write", type=int)
@click.option("--layer", default=1, help="1: Volatile RAM, 2: Battery backed RAM (BBR), 4: External flash")
@click.option("--baudrate", default=38400, help="Communication speed")
def config_set(port, key, value, layer, baudrate):
    transaction = 0
    # cfgData = [("CFG_UART1_BAUDRATE", 9600), (0x40530001, 115200)]
    # cfgData = [("CFG_UART1_BAUDRATE", 9600)]
    # if not is_valid_cfg_key_or_name(key):
    #     return
    if type(key) is str and key.startswith("0x"):
        key = int(key, 0)
    cfgData = [(key, value)]
    # print(cfgData)
    msg = UBXMessage.config_set(layer, transaction, cfgData)
    print(msg)
    serialOut = Serial(port, baudrate, timeout=5)
    serialOut.write(msg.serialize())

if __name__ == '__main__':
    config_set()
