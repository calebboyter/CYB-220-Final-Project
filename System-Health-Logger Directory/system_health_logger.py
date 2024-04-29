import psutil
import datetime

def get_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    timestamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    return f"{timestamp} - CPU: {cpu_usage}%, Memory: {memory}%, Disk: {disk_usage}%"

def log_system_health():
    health_info = get_system_health()
    with open("system_health_log.txt", "a") as file:
        file.write(health_info + "\n")

if __name__ == "__main__":
    log_system_health()
