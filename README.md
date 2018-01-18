# sbanken-cli
A Python 3 command line client for checking your account balance at [Sbanken](https://sbanken.no/).

## Advice
As this is accessing your bank account, you shuld __always read the code before running it__. If you don't understand it, __do not run it!__

## Usage
```bash
❯ ./sbanken-cli.py 
Brukskonto:	2460.17
Regning:	0.0
```

## Installation
If you don't already have it installed, install Python 3 and pip3

```bash
pip3 install -r requirements.txt
mv config.json.example config.json
nano config.json # Add API credentials from Sbanken developer portal and your User ID (PN)
chmod +x sbanken-cli.py
```
