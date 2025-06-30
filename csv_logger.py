import csv
from datetime import datetime

def log_to_csv(data, filename="sensor_log.csv"):
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        row = [datetime.now()] + list(data.values())
        writer.writerow(row)
