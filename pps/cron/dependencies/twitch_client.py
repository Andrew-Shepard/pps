# Directly runs off of cli commands, could be refactored to directly use twitch api instead of this library
from asyncio import subprocess
from env import STREAMER

def grab_latest_vod_text():
    subprocess.run([f"tcd --channel {STREAMER} --first=1"])
    
