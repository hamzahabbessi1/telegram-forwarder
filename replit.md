# Telegram Message Forwarder Bot

## Overview
This is a Telegram bot that automatically forwards messages from one Telegram channel to another using the Telethon library. The bot runs continuously and listens for new messages in the source channel, then forwards them to the destination channel.

## Project Architecture
- **Language**: Python 3.11
- **Main Framework**: Telethon (Telegram client library)
- **Type**: Backend service/bot (no frontend)

## Recent Changes
- **October 15, 2025**: Initial Replit setup
  - Installed Python 3.11 and dependencies
  - Created .gitignore for Python project
  - Set up workflow to run the bot
  - Configured environment for Telegram API credentials

## Required Environment Variables
The bot requires the following secrets to be configured:
- `TELEGRAM_API_ID`: Your Telegram API ID (get from https://my.telegram.org)
- `TELEGRAM_API_HASH`: Your Telegram API hash
- `TELEGRAM_SOURCE_CHANNEL`: The channel username or ID to forward messages from
- `TELEGRAM_DEST_CHANNEL`: The channel username or ID to forward messages to

## Dependencies
- telethon==1.34.0
- asyncio

## How It Works
1. The bot connects to Telegram using your API credentials
2. It listens for new messages in the source channel
3. When a new message arrives, it forwards it to the destination channel
4. The bot maintains a session file (`forwarder_session.session`) to persist authentication

## Running the Bot
The bot runs continuously using the configured workflow. It will start automatically when the Replit project is started.
