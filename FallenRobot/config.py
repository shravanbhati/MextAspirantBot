class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 20573861
    API_HASH = "9ed32e4aa14ee55496b2c1f6bd9124da"

    CASH_API_KEY = "X8ZYRPSU4VLXJH6E"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://xxvshcsd:iRYvEgOlla1CuwcAp2WqFpHakyW9lOtH@arjuna.db.elephantsql.com/xxvshcsd"  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://shravanbhati0098:pKMBB!kvzrfy3G3@cluster0.am91sgd.mongodb.net"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "MikeyBotSupport"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6845925574:AAGIBG97uaiPMx0p94kGdmeBa4JoN6SdnkY"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "http://api.timezonedb.com/v2.1/get-time-zone"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5022405777  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
