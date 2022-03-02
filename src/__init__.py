from datetime import datetime
from adafruit_dht import DHT22
from tenacity import retry, stop_after_attempt, wait_fixed
from pathlib import Path
import logging

@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
def read_write_data(dhtDevice: DHT22, root_folder: Path, dev: bool = True):
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        now = datetime.utcnow()
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        logging.error(error.args[0], exc_info=True)
        raise error
    except Exception as error:
        raise error

    reading = f'{now.strftime("%Y-%m-%dT%H:%M:%S")},{temperature_c},{humidity}\n'

    if not dev:
        try:
            with open(root_folder/'data'/f'test_log_{now.date().isoformat()}.csv', 'a+') as f:
                f.write(reading)
        except:
            logging.error('Error during saving results to file', exc_info=True)
    else:
        print(reading)
