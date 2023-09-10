import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6406319145:AAGi3p3xx2A0PSExxXndJdBzHq67N8_WVc0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLoBu2MonT6QyIdM6TkNy32xzEK5huTjzHYI-5Pix4bW4rqbAkDRsBp8Q4Ih2rRg22-0-g1zNbGZLGi30VXrTsqob_4pH_DSVFzyYH6Au24_mOZf7waQtK7Dp9oYGGuKjIkXHuM53V4HH0y1d0v-y-T6gSObLRTObPP6dxfQ_qpIya1bPhe_QMxs6LCo-tql0KH8oQ2mq1XSYDLF4iz8TcVVec6IY10y708J-y12BouWcWXjA7-FHs7bGQ5YSmvr7NNAVEclNuIL_nHWhtopJOwT_VOHRt7anYWQ57Tz5LbJKripwS6TF5Zfdlhz_XCjvM-A9orNMSdxyCPOsUaPEeqUCZc=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
