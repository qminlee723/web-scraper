import csv
import os
from datetime import datetime

def get_today_filename(prefix, ext="csv", folder="../data"):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{prefix}_{today}.{ext}"
    return os.path.join(folder, filename)

def save_to_csv(filename, data, mode="a"):
    with open(filename, mode, newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(data)
