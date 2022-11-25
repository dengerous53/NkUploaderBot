import os



import asyncio
from collections import defaultdict
import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

class Config:
    ACTIVE_DOWNLOADS = []
    API_ID = int(os.environ.get("API_ID", "10412514"))
    API_HASH = os.environ.get("API_HASH", "4d55a7064ad72adcfa8944f505453a8c")
    AUTH_USERS =  [int(i) for i in os.environ.get("AUTH_USERS", "5467777513").split(" ")]
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5751126237:AAF62IPKfPEAmi8gXlvb55fDCC-I4L4OFMQ")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Haashim:Haashim@mfile0.t9hxg.mongodb.net/?retryWrites=true&w=majority")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    UPDATE_CHANNEL = int(os.environ.get("UPDATE_CHANNEL", "-1001860535753"))
    PROCESS_MAX_TIMEOUT = 3600
    RESTART_TIME = []
    TG_MAX_FILE_SIZE = 3980000000
    TIME_GAP1 = {}
    TIME_GAP2 = {}
    timegap_message = {}
    
    TRACE_CHANNEL = os.environ.get("DB_CHANNEL_ID", "-1001860535753")
    last_edit = defaultdict(lambda: 0)
    SESSION_STRING = os.environ.get(
        "SESSION_STRING",
        "AQBrpOgAA3CMAB3i5__N6FXYIqpvtl9djrQ1pDu0BpubbmMRtnZpcouaIGVYdLRezA_0Jka2DZfgze47b6WiKx02B0K_gFov5ae-PUK_C-351c9e462DRDnfJhpY0BEFaeUQlQFSRCLkFGdO5Ub4SoMT4YsMFKgCXK8h91fvLCQU1cenN1IZTyRhopzxbYRn3WutyVrh2QlgV8D2GMX8Fm6Nzt3HO2_PCx1tuZFB98u3KSNpyObkXcrgEHE9MR5clD3Vqr7rLZE0Dy5FMVBmnWVNf_HK-cggxsjVbxRXwY8QND309LnmVpdsc865XEZ5N77r0EAXBLo6B4BxWDqO6GnJj6qhzgAAAAB1aFXoAA",
    )

    # QUEUE
    SESSION_NAME = os.environ.get("SESSION_NAME", "Ovuploader")
    WORKERS = 5
    QUEUE_MAXSIZE = 20
    normal_queue = asyncio.Queue(maxsize=QUEUE_MAXSIZE)
    queue = asyncio.Queue(maxsize=QUEUE_MAXSIZE)
    normal_tasks = []
    tasks = []
    user = []
    Library = ['aria2', 'aiohttp']
    Extension = ['mp4', 'webm', 'mkv', 'all']
    FORCE_SUB = os.environ.get("FORCE_SUB", "Nkbots") 
    PORT = os.environ.get("PORT", "8080")

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Update channel for Force Subscribe
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001215708095")
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 4194304000
    TG_MAX_FILE_SIZE = 4194304000
    FREE_USER_MAX_FILE_SIZE = 4194304000

    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprcess
    PROCESS_MAX_TIMEOUT = 300
    # watermark file
    DEF_WATER_MARK_FILE = ""
   
  
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001860535753"))
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", "5467777513"))
    # Update channel for Force Subscribe
    
    TG_MIN_FILE_SIZE = 2097152000
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "NkUploaderBot")
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "5467777513").split()))
    PRO_USERS.append(OWNER_ID)
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
    BYPASS = os.environ.get("BYPASS", "")
    ADL_BOT_RQ = {}
    
