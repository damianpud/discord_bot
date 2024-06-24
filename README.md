# Discord RSI Bot

This bot fetches spot K-line data for the SOL/USDT pair from Bybit, calculates the RSI, and sends notifications to a Discord channel when the RSI value exceeds 70 or drops below 30.

## Setup

1. Clone the repository:
    ```
    git clone https://github.com/damianpud/discord_bot.git
    ```

2. Create a `.env` file and add your Discord bot token and channel ID:
    ```
    DISCORD_BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN
    CHANNEL_ID=YOUR_CHANNEL_ID
    ```

3. Build the Docker image:
    ```
    docker build -t discord-bot .
    ```

4. Run the Docker container:
    ```
    docker run --env-file .env discord-bot
    ```

## Usage

The bot will automatically start fetching data and sending notifications when the RSI value is above 70 or below 30.