import discord
import requests
import pandas as pd
import ta
import asyncio
import os

# Discord bot token
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Channel ID where the bot will send messages
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def fetch_klines():
        url = "https://api.bybit.com/v5/market/kline"
        params = {
            'symbol': 'SOLUSDT',
            'interval': '60',
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data['result']['list']

    @staticmethod
    def calculate_rsi(data):
        df = pd.DataFrame(data)
        df[4] = df[4].astype(float)
        rsi_i = ta.momentum.RSIIndicator(df[4], window=14)
        return rsi_i.rsi().iloc[-1]

    async def setup_hook(self) -> None:
        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def my_background_task(self):
        await self.wait_until_ready()
        channel = self.get_channel(CHANNEL_ID)
        alert = False
        while not self.is_closed():
            klines = self.fetch_klines()
            rsi = self.calculate_rsi(klines)
            if rsi > 70 and not alert:
                alert = True
                await channel.send(f"RSI is above 70: {rsi}")
            elif rsi < 30 and not alert:
                alert = True
                await channel.send(f"RSI is below 30: {rsi}")
            elif 30 <= rsi <= 70:
                alert = False
            await asyncio.sleep(1)


intents = discord.Intents.default()
client = MyClient(intents=intents)

client.run(TOKEN)
