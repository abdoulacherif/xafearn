import os

BOT_TOKEN        = os.environ.get("BOT_TOKEN", "")
BOT_USERNAME     = "xafearn_bot"
SUPABASE_URL     = os.environ.get("SUPABASE_URL", "")
SUPABASE_KEY     = os.environ.get("SUPABASE_KEY", "")
WEBHOOK_URL      = os.environ.get("WEBHOOK_URL", "")
WEBHOOK_SECRET   = os.environ.get("WEBHOOK_SECRET", "xafearn_secure_2024")

CHANNELS = [
    os.environ.get("CHANNEL_1", "@channel1"),
    os.environ.get("CHANNEL_2", "@channel2"),
    os.environ.get("CHANNEL_3", "@channel3"),
]

RETRAIT_CHANNEL_ID = int(os.environ.get("RETRAIT_CHANNEL_ID", "0"))

_admin_env = os.environ.get("ADMIN_IDS", "")
ADMIN_IDS = [int(x.strip()) for x in _admin_env.split(",") if x.strip().isdigit()]