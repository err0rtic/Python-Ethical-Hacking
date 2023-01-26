import speedtest
import platform
import re
import uuid
import psutil
from socket import *


def pc_info():
    result = f"{'*'*10} Information host {'*'*10}\n"
    result += f'Platform: {platform.system()}\n'
    result += f'Platform-release: {platform.release()}\n'
    result += f'Platform-version: {platform.version()}\n'
    result += f'Architecture: {platform.machine()}\n'
    result += f'Hostname: {gethostname()}\n'
    result += f'IP-address: {gethostbyname(gethostname())}\n'
    result += f'MAC-address: {":".join(re.findall("..", "%012x" % uuid.getnode()))}\n'
    result += f'Download speed: {speedtest.Speedtest().download()/1024/1024:.2f} Mbit/s\n'
    result += f'Upload speed: {speedtest.Speedtest().upload()/1024/1024:.2f} Mbit/s\n'
    result += f'Processor: {platform.processor()}\n'
    result += f'Ram: {round(psutil.virtual_memory().total / (1024.0 **3))} GB\n'
    return result


if __name__ == '__main__':
    print(pc_info())