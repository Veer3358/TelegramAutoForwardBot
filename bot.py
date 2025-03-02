from telethon import TelegramClient, events
import os

# API Details (Railway Environment Variables se fetch karenge)
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

# Channels
source_channel = os.getenv("SOURCE_CHANNEL")  # Source Channel
destination_channel = os.getenv("DESTINATION_CHANNEL")  # Destination Channel

# Start Client
client = TelegramClient("bot_session", api_id, api_hash).start(bot_token=bot_token)

# Forwarding Messages
@client.on(events.NewMessage(chats=source_channel))
async def forward_message(event):
    await client.send_message(destination_channel, event.message)

print("Bot is running 24/7...")
client.run_until_disconnected()
