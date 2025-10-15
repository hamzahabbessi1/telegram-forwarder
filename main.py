# ===============================================================
# Telegram Channel Forwarder (Telethon)
# Forwards all new posts from one channel you can read
# to another channel where you’re admin.
# ===============================================================

import asyncio
from telethon import TelegramClient, events

# --- EDIT THESE FOUR VALUES -----------------------------------
api_id = 28004175                     # <<< your own api_id (integer, no quotes)
api_hash = "b22a2efdab5d7381f0fea38155b62d75"   # <<< your api_hash in quotes
session_name = "forwarder_session"    # local session filename

SOURCE = "https://t.me/+gpS_OS3bhGw1N2M0"   # <<< your source channel invite link
DEST = "@XAUUSD_VIP"                         # <<< your destination channel username
# ----------------------------------------------------------------

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE))
async def forward_new_message(event):
    """Forward every new post from SOURCE to DEST"""
    try:
        await client.forward_messages(DEST, event.message, from_chat=event.chat_id)
        print(f"✅ Forwarded message {event.id}")
    except Exception as e:
        print("❌ Forward error:", e)

async def main():
    await client.start()
    me = await client.get_me()
    print(f"Logged in as {me.first_name or me.username}")
    print(f"Listening on {SOURCE} → forwarding to {DEST}")
    await client.run_until_disconnected()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopped manually.")
