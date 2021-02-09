import os, sys
import yaml
import time
import re
import socket
import logging

# Setup logging
logging.basicConfig(filename="ip_log.csv", level=logging.INFO, format='%(asctime)s, %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')



if __name__ == "__main__":
    with open('config.yaml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    hostname = config['hostname']
    cycle = config['cycle']
    ip_addr = socket.gethostbyname(hostname)

    try:
        while True:
            logging.info(f"IPv4: {ip_addr}")
            time.sleep(cycle)

    except Exception as e:
        print(str(e))