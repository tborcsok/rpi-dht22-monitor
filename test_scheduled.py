
import time
from datetime import datetime
import board
import adafruit_dht
from tenacity import retry, stop_after_attempt, wait_fixed
from pathlib import Path
import logging

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D22)

root = Path(__file__).parent

@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
def read_write_data():
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        now = datetime.utcnow()
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        raise error
    except Exception as error:
        raise error

    try:
        with open(root/'data'/f'test_log_{now.date().isoformat()}.csv', 'a+') as f:
            f.write(f'{now.strftime("%Y-%m-%dT%H:%M:%S")},{temperature_c},{humidity}\n')
    except:
        pass

if __name__=='__main__':
    started = datetime.utcnow()

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler(root/'logs'/f'schedule_{started.date().isoformat()}.log'),
                                  logging.StreamHandler()])

    read_write_data()
    dhtDevice.exit()
    logging.info(f'Finished {datetime.utcnow() - started}')
