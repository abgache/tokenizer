from datetime import datetime
def time_log_module():
    return f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"