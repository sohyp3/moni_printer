from binance.client import Client
from binance.enums import *
import schedule 

import re 

import api

# binance shit
client = Client(api.binance_api_key,api.binance_api_secret)

class yosh():
    # currently self.buy/self.sell/self.rep/self.price_checker is disabled
    # __init__ -> checker -> how_many -> oco_buy

    # starts here 1. -> self.checker()
    def __init__(self,hehe,datee):
        self.text = hehe
        self.checker(self.text)
    
    
    # 2. -> self.how_many() 
    def checker(self,text):

        # the way i get the currency name is by getting the words with all CAPS 
        # [Forwarded from Crypto VIP Paid signal™] so we gotta remove that VIP
        text = text.replace("VIP", "")
        # searching for all caps
        matches = re.findall(r"([A-Z]+\s?[A-Z]+[^a-z0-9\W])",text)
        
        self.cur_price = 0
        try:
            # get the currency price
            self.cur_price = float(client.get_avg_price(symbol=f"{matches[0]}BTC")['price'])
            self.cur_name = matches[0]
            self.how_many(self.cur_name)
        except:
            print("invalid currency name. ")


    # This function determine how much it should buy
    # i tell him with how much usd i want to work with
    # 3. -> self.buy()
    def how_many(self,cur):

        self.btc_price = float(client.get_avg_price(symbol=f"BTCUSDT")['price'])
        self.usdt_limit = 190
        self.btc_limit = float(self.usdt_limit / self.btc_price)
        self.cur_amount = int(self.btc_limit/self.cur_price) 
        self.cur_amount = self.cur_amount - int (self.cur_amount*0.01)
        print(self.cur_amount)
        # self.buy()
        # self.rep()
        self.oco_buy()
        
    # buy market than imidietly add a oco order but oco not working
    def oco_buy(self):
        # 3% sell profit / 1% stop lose
        self.sell_limit = self.cur_price + (self.cur_price * 0.03)   
        self.sell_stop = self.cur_price - (self.cur_price * 0.01)     

        order = client.create_order(
            symbol=f'{self.cur_name}BTC',
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=self.cur_amount)
            
        # it gets all orders 
        orders = client.get_all_orders(symbol=f'{self.cur_name}BTC')
        # get the market order price
        for item in orders:
            x = float(item['cummulativeQuoteQty'])/float(item['executedQty'])        
        
        self.cur_price = x 

        print(f"bought {self.cur_amount} of {self.cur_name} at " "%.8f" % self.cur_price)
        # ==============
        # making OCO not working.. 
                        
        # y = str("%.8f" % self.sell_stop)
        # z = str("%.8f" % self.sell_limit)
        # order = client.create_oco_order(
        #     symbol=f'{self.cur_name}BTC',
        #     side=SIDE_SELL,
        #     stopLimitTimeInForce=TIME_IN_FORCE_GTC,
        #     quantity=self.cur_amount,
        #     stopPrice=self.sell_stop,
        #     price=self.sell_limit)
        # print('don')   


    # buy market
    # 4. -> self.rep()
    def buy(self):

        order = client.create_order(
            symbol=f'{self.cur_name}BTC',
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=self.cur_amount)
        
        print(f"bought {self.cur_amount} of {self.cur_name} at " "%.8f" % self.cur_price)
        self.rep()


    # rep will run every 5 seconds look at the price 
    # 5. -> self.price_check()
    def rep(self):
        schedule.every(5).seconds.do(self.price_check)            
        self.x = 0
        while self.x == 0:
            schedule.run_pending()
    
    
    # check if it reached the goal 
    # 6. -> self.sell()
    def price_check(self):
        self.sell_limit = self.cur_price + (self.cur_price * 0.03)        
        self.cur_price_new = float(client.get_avg_price(symbol=f"{self.cur_name}BTC")['price'])
        print('\n========\n')
        print(f"sell limit = " "%.8f" % self.sell_limit)
        print(f"buy price = " "%.8f" % self.cur_price)
        print(f"current price = " "%.8f" % self.cur_price_new)
        print('\n========\n')
        
        if self.cur_price_new >= self.sell_limit:
            print("hoi")
            self.sell()
            self.x = 1


    # sell market
    # 7. ends here    
    def sell(self):
        order = client.create_order(
            symbol=f'{self.cur_name}BTC',
            side=SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=self.cur_amount)   
        self.pr = f"sold {self.cur_amount} of {self.cur_name} at " "%.8f" % self.cur_price_new
        print(self.pr)