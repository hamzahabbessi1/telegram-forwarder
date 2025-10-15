import os
import asyncio
from telethon import TelegramClient, events

# Load your environment variables
api_id = int(os.environ.get("TELEGRAM_API_ID"))
api_hash = os.environ.get("TELEGRAM_API_HASH")
source_channel = os.environ.get("TELEGRAM_SOURCE_CHANNEL")
dest_channel = os.environ.get("TELEGRAM_DEST_CHANNEL")

client = TelegramClient("forwarder_session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    try:
        await client.send_message(dest_channel, event.message)
        print(f"✅ Forwarded message: {event.message.text}")
    except Exception as e:
        print(f"❌ Error forwarding message: {e}")

async def main():
    await client.start()
    print("🚀 Bot started and is forwarding messages...")
    await client.run_until_disconnected()

asyncio.run(main())
