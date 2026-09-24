import random
from datetime import datetime, timedelta

# Configuration
NUM_LINES = 5000
OUTPUT_FILE = "access.log"

# Pool de données
IPS = [f"192.168.1.{i}" for i in range(1, 50)] + [
    f"10.0.0.{i}" for i in range(1, 30)
] + [
    "172.16.0.5", "172.16.0.12", "8.8.8.8", "1.1.1.1"
]

METHODS = ["GET", "POST", "PUT", "DELETE"]
METHOD_WEIGHTS = [0.75, 0.15, 0.07, 0.03]

URLS = [
    "/index.html",
    "/about.html",
    "/contact.html",
    "/api/v1/users",
    "/api/v1/products",
    "/api/v1/login",
    "/dashboard",
    "/static/css/style.css",
    "/static/js/app.js",
    "/images/logo.png"
]

STATUS_CODES = [200, 301, 304, 400, 401, 403, 404, 500, 503]
STATUS_WEIGHTS = [0.70, 0.05, 0.08, 0.03, 0.02, 0.02, 0.07, 0.02, 0.01]

def generate_logs():
    now = datetime.now()
    start_date = now - timedelta(days=30)
    
    timestamps = []
    for _ in range(NUM_LINES):
        random_seconds = random.randint(0, int((now - start_date).total_seconds()))
        timestamps.append(start_date + timedelta(seconds=random_seconds))
    
    timestamps.sort()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for dt in timestamps:
            ip = random.choice(IPS)
            date_str = dt.strftime("%d/%b/%Y:%H:%M:%S +0100")
            method = random.choices(METHODS, weights=METHOD_WEIGHTS)[0]
            url = random.choice(URLS)
            status = random.choices(STATUS_CODES, weights=STATUS_WEIGHTS)[0]
            bytes_sent = random.randint(200, 5000) if status == 200 else random.randint(0, 300)
            
            line = f'{ip} - - [{date_str}] "{method} {url} HTTP/1.1" {status} {bytes_sent}\n'
            f.write(line)

    print(f"Fichier '{OUTPUT_FILE}' généré avec succès ({NUM_LINES} lignes).")

if __name__ == "__main__":
    generate_logs()
