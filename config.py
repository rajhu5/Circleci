## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCPOD2gQoFVcRJ0Q3QNS36-zzu1nLMwKBqXvu2-iAE5mMLypfcBccWCQr8FIhxKcRqydw5t0M0rkzm88k3xPWZeuRcb8X-kYJPvESRBQocg4rr_PouyCYO_MyYi4tC8BKlvcpnLyRnsi-Wc0t4cbwBBud39rZFPfEsXXDabRdt034QC8IMU9I8IhS3BM_0OXdsp-xUDJaRRuQfEcscURZMXG-z_Y0an7HzvCMiqrjBROmqJfJXu8RZc4mfyLVvogTrbvi1B3hgQTPxm48O_T3Jgq0NUblD368jOBgQQT3m6fPBu7GN7iVNAvZ0N777isCdYwYteZt-52FeedyZPyOMAAAAAAYRq1wgA")
BOT_TOKEN = getenv("BOT_TOKEN", "6570587888:AAGtvjvPgrxjIma7UJ91kRoUGKPlBl46OSY")
BOT_NAME = getenv("BOT_NAME", "Fhh")
API_ID = int(getenv("API_ID", "28645948"))
API_HASH = getenv("API_HASH", "0d1cca3a9f4f4beb7ae8508f05ec4fcd")
OWNER_NAME = getenv("OWNER_NAME", "𝐜𝐡𝐚𝐫𝐦𝐢𝐧𝐠")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Drama_boy2")
ALIVE_NAME = getenv("ALIVE_NAME", "𝐜𝐡𝐚𝐫𝐦𝐢𝐧𝐠")
BOT_USERNAME = getenv("BOT_USERNAME", "filter_file_robot")
OWNER_ID = getenv("OWNER_ID", "64256820350")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Drama_boy2")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TheSupportChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheUpdatesChannel")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6425682035").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
