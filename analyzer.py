from binance.client import Client
from binance.enums import *

import re 

import api


client = Client(api.binance_api_key,api.binance_api_secret)

class yosh():
    def __init__(self,hehe):
        self.text = hehe
        self.checker(self.text)

    def checker(self,text):
        
        text = text.replace("VIP", "")

        matches = re.findall(r"([A-Z]+\s?[A-Z]+[^a-z0-9\W])",text)

        # print(matches[0])
        
        self.cur_price = 0
        try:
            self.cur_price = float(client.get_avg_price(symbol=f"{matches[0]}BTC")['price'])
            self.cur_name = matches[0]
            self.how_many(self.cur_name)
        except:
            print("invalid currency name. ")


        # print("%.8f" % self.cur_price)
        # print(matches[0])

    def how_many(self,cur):
        self.btc_price = float(client.get_avg_price(symbol=f"BTCUSDT")['price'])
        self.usdt_limit = 100 
        self.btc_limit = float(self.usdt_limit / self.btc_price)
        self.cur_amount = int(self.btc_limit/self.cur_price) 
        self.cur_amount = self.cur_amount - int (self.cur_amount*0.01)
        print(self.cur_amount)

        # self.buy()

    def buy(self):
        order = client.create_order(
            symbol=f'{self.cur_name}BTC',
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=self.cur_amount)

        print(f"bought {self.cur_amount} of {self.cur_name} at " "%.8f" % self.cur_price)


        
