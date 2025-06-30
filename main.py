from data_generator import generate_dummy_data
from mqtt_publisher import publish_data
from csv_logger import log_to_csv
import time

while True:
    try:
        data = generate_dummy_data()
        print("Generated:", data)
        publish_data(data)
        log_to_csv(data)
        time.sleep(5)
    except Exception as e:
        print("Error:", e)
