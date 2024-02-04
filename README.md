# scripts-puubx-config

A repository to hold python scripts to configure variables of ZED-F9P.

## Setup

```
pip3 install serial pyubx2 click
```

## Usage

Keys for configuration is defined as [UBX_CONFIG_DATABASE](https://github.com/semuconsulting/pyubx2/blob/b55d97c5c4f7f0d4547b24074efd4caead090e60/src/pyubx2/ubxtypes_configdb.py#L69) in [pyubx2](https://github.com/semuconsulting/pyubx2).

### Set

Command with name of key
```sh
./pyubx-cfg-set.py --port /dev/ttyACM0 --key CFG_UART1_BAUDRATE --value 9600
```

Command with hex number of key
```sh
./pyubx-cfg-set.py --port /dev/ttyACM0 --key 0x40520001 --value 9600
```

result
```
<UBX(CFG-VALSET, version=0, ram=1, bbr=0, flash=0, action=0, reserved0=0, CFG_UART1_BAUDRATE=9600)>
```

### Get

Command with name of key
```sh
./pyubx-cfg-get.py --port /dev/ttyACM0 --key CFG_UART1_BAUDRATE
```

Command with hex number of key
```sh
./pyubx-cfg-get.py --port /dev/ttyACM0 --key 0x40520001
```

result
```
<UBX(CFG-VALGET, version=1, layer=0, position=0, CFG_UART1_BAUDRATE=9600)>
```

## License

MIT
