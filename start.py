import random
from agents import Agent
from tools import plot
from time import sleep
from abygame import quit


endowed_agents = [Agent(goods=1, money=0.0, utility=random.gauss(5, 2), i=i, name='endowed') 
                  for i in range(500)]
have_nots_agents = [Agent(goods=0, money=20.0, utility=random.gauss(10, 2), i=i, name='have not') 
                    for i in range(500)]

all_agents = endowed_agents + have_nots_agents

history_of_traded_quantity = []
history_of_prices = []

for time in range(300):
    print(time)
    trades_this_round = 0
    prices_this_round = 0
    for i in range(150):
        seller = random.choice(all_agents)
        buyer = random.choice(all_agents)

        offer_price = seller.makes_an_offer()
        if offer_price is not None:
            traded_quantity = buyer.accepts_or_rejects_offer(offer_price)
            seller.delivers(traded_quantity, offer_price)

            if traded_quantity > 0:
                trades_this_round += 1
                prices_this_round += offer_price

    seller.update()
    buyer.update()
    sleep(0.02)
  

    history_of_traded_quantity.append(trades_this_round)
    if trades_this_round > 0:
        history_of_prices.append(prices_this_round / trades_this_round)
    else:
        history_of_prices.append(None)

plot(history_of_traded_quantity, history_of_prices)
input()

quit()