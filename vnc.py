import asyncvnc
import time, os
from dotenv import load_dotenv

from setup_logger import logging

load_dotenv()

async def start_ros2():
    async with asyncvnc.connect(os.getenv('VNC_HOST'), port=5901, password=os.getenv('VNC_PASSWD')) as client:
        logging.info(f"{client}")
        client.keyboard.press('Ctrl', 'Alt', 't')
        time.sleep(1)
        client.keyboard.write('cd ade-home/2021/')
        client.keyboard.press('Return')
        time.sleep(.2)
        client.keyboard.write('ade start')
        client.keyboard.press('Return')
        time.sleep(2)
        client.keyboard.write('ade enter')
        client.keyboard.press('Return')
        time.sleep(2)
        client.keyboard.write('cd 2021')
        client.keyboard.press('Return')
        time.sleep(.1)
        client.keyboard.write('source install/setup.zsh')
        client.keyboard.press('Return')
        time.sleep(1.5)
        client.keyboard.write('ros2 launch teamspatzenhirn_launch freedrive_11_combined_perception.launch.py')
        client.keyboard.press('Return')