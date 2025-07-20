from datetime import datetime, timedelta
from rate_limiting_strategy import RateLimiterStrategy


class FixedWindowCounter(RateLimiterStrategy):
    def __init__(self, window_size=5, max_requests=3):
        self.window_size = window_size
        self.max_requests = max_requests
        self.counter = 0
        self.start_time = datetime.now()

    def update_window(self):
        current_time = datetime.now()
        time_elapsed = current_time - self.start_time
        if time_elapsed.total_seconds() < self.window_size:
            return
        self.counter = 0
        self.start_time = current_time - timedelta(seconds=(time_elapsed.total_seconds() % self.window_size))

    def allow_request(self) -> bool:
        self.update_window()
        if self.counter < self.max_requests:
            self.counter += 1
            return True
        else:
            return False







