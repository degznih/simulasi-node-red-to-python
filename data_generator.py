import random

def generate_dummy_data():
    return {
        "Pyranometer": round(random.uniform(600, 800), 2),
        "TotalEnergy": round(random.uniform(5000, 6000), 2),
        "Voltage": round(random.uniform(220, 230), 2),
        "Current": round(random.uniform(1, 2), 3),
        "ActivePower": round(random.uniform(300, 400), 1),
        "Frequency": round(random.uniform(49.9, 50.1), 2),
        "PowerFactor": round(random.uniform(0.85, 0.95), 2)
    }
