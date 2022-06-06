import os
import uvicorn
from api import *

if __name__ == "__main__":
    os.chdir("/code/")
    uvicorn.run("api:app", host="0.0.0.0", port=80, log_level="info")