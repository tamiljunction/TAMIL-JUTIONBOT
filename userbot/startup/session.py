from telethon import TelegramClient
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession

from ..config import Config


if Config.LEGEND_STRING:
    session = StringSession(str(Config.LEGEND_STRING))
else:
    session = "Legend"

try:
    Legend = TelegramClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"LEGEND_STRING - {e}")
    sys.exit()


if Config.SESSION_2:
    session2 = StringSession(str(Config.SESSION_2))
    L2 = TelegramClient(
        session=session2,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    L2 = None


if Config.SESSION_3:
    session3 = StringSession(str(Config.SESSION_3))
    L3 = TelegramClient(
        session=session3,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    L3 = None


if Config.SESSION_4:
    session4 = StringSession(str(Config.SESSION_4))
    L4 = TelegramClient(
        session=session4,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    L4 = None


if Config.SESSION_5:
    session5 = StringSession(str(Config.SESSION_5))
    L5 = TelegramClient(
        session=session5,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    L5 = None


LegendBot = TelegramClient(
    session="Legend-Bot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.BOT_TOKEN)
