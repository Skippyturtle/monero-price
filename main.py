#final
import discord
import requests
import json
import matplotlib.pyplot as plt
import time

while True:
    #api request
    url = 'https://min-api.cryptocompare.com/data/v2/histohour?fsym=XMR&tsym=EUR&limit=24'
    response = requests.get(url)
    data = json.loads(response.text)
    
    #display data
    monero_prices = []
    for item in data['Data']['Data']:
        monero_prices.append(item['close'])
    
    #plot graph
    plt.style.use('dark_background')
    plt.plot(monero_prices, color='orange')
    plt.title("Monero price in the last 24 hours", color='orange')
    plt.xlabel('Hours', color='orange')
    plt.ylabel('Price in EUR', color='orange')
    plt.savefig('Monero Price Graph.png', facecolor='#36393e')
    
    #send to discord webhook
    from discord_webhook import DiscordWebhook
    
    #get current price
    url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=XMR&tsyms=EUR'
    response = requests.get(url)
    data = json.loads(response.text)
    
    monero_price = data['XMR']['EUR']
    
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1069319344380719104/4ZxYrJruHifSvIfyHor6dKkp_pFXI7WNBfVvT5s4lXNlwAgyI--GWd7EBEKxDcGa274p')
    embed = discord.Embed(title='Monero Price', description=f'The current price of Monero is {monero_price} EUR', color=242424)
    embed.set_thumbnail(url="attachment://Monero Price Graph.png")
    webhook.add_embed(embed.to_dict())
    webhook.add_file(file=open('Monero Price Graph.png', 'rb'), filename='Monero Price Graph.png')
    webhook.execute()
    
    time.sleep(3600)
