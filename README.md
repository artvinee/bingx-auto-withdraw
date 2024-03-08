output comes from a spot account

to customize the software, you need to open bingxwithdraw.py and find a dictionary with the following pairs:

"address": addresses are taken from addresses.txt

"amount": enter the number of tokens to be output, taking into account the bingx commissions 

"coin": write the ticker of the coin.

"network": enter the network. TRC20, BEP20, etc. (the network you need should be checked on the bingx output page)

"timestamp": to specify it, you need to run the code. It might work, and then it's fine. If, however, within 5 minutes did not begin to leave funds from your account to your wallets, then you should turn to the output from the console. The output line will contain the timestamp value. you should enter it as a value.

time.sleep(random.randint(30, 60)) instead of 30 and 60 specify your rest range between outputs in seconds.

If the code does not work, open a new issue

donate : 0x0005b9fa0D2932D5E879102919675692cF60C52a, CqC89ZhqzTxnkCPjJQYCXXTXbhw5fN1bK881daqWxcR1
