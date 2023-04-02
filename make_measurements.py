from datetime import datetime
import board
import adafruit_dht
from pathlib import Path
import logging

from src import read_write_data


root = Path(__file__).parent

if __name__=='__main__':
    started = datetime.utcnow()

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler(root/'logs'/f'schedule_{started.date().isoformat()}.log'),
                                  logging.StreamHandler()])


    dhtDevice = adafruit_dht.DHT22(board.D22)

    try:
        read_write_data(dhtDevice=dhtDevice, root_folder=root, dev=False)
    except:
        raise
    finally:
        dhtDevice.exit()
        logging.info(f'Finished {datetime.utcnow() - started}')
