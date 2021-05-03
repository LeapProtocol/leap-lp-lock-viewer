import json
import datetime
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))

contract_address = Web3.toChecksumAddress("0x153aaf397d37a20Efa9dc46e4cBa42583cB0007A")
leap_json = json.load(open("./Leap.json"))
leap = w3.eth.contract(abi=leap_json["abi"], address=contract_address)

amounts, deadlines = leap.functions.getLockedLpTokens().call()

for (amount, deadline) in zip(amounts, deadlines):
    amount = amount * 1e-18
    deadline = datetime.datetime.fromtimestamp(deadline)
    deadline =  deadline.strftime('%Y-%m-%d %H:%M:%S')

    print("LP Token Amount: {}\t Release Time: {}".format(amount, deadline))