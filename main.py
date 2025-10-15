import os
import asyncio
from telethon import TelegramClient, events

# Load your environment variables
try:
    api_id_str = os.environ.get("TELEGRAM_API_ID")
    if not api_id_str:
        raise ValueError("TELEGRAM_API_ID is not set")
    api_id = int(api_id_str)
except ValueError as e:
    print(f"❌ Error: TELEGRAM_API_ID must be a numeric value (e.g., 12345678)")
    print(f"   Current value appears to be: {api_id_str[:20] if api_id_str else 'None'}...")
    print(f"   Please check that TELEGRAM_API_ID and TELEGRAM_API_HASH are not swapped")
    print(f"   Get your API credentials from https://my.telegram.org")
    raise

api_hash = os.environ.get("TELEGRAM_API_HASH")
source_channel = os.environ.get("TELEGRAM_SOURCE_CHANNEL")
dest_channel = os.environ.get("TELEGRAM_DEST_CHANNEL")

if not api_hash:
    raise ValueError("TELEGRAM_API_HASH is not set")
if not source_channel:
    raise ValueError("TELEGRAM_SOURCE_CHANNEL is not set")
if not dest_channel:
    raise ValueError("TELEGRAM_DEST_CHANNEL is not set")

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
