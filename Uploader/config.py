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
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5751126237:AAGZH7TnC1thjiuMvvR7-0YbLpXbNZwaZs4")
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
