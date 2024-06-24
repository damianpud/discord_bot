FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app
RUN pip install discord.py requests pandas ta

# Run the bot
CMD ["python", "discord_bot.py"]