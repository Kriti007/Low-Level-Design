from collections import deque
from rate_limiting_strategy import RateLimiterStrategy

# handles the burst conditions well unlike token bucket


class SlidingWindowLog(RateLimiterStrategy):
    def __init__(self, window_size=10, max_requests=5):
        self.window_size = window_size
        self.queue = deque()
        self.max_requests = max_requests

    def allow_request(self, current_time):
        diff = current_time - self.window_size
        while self.queue and self.queue[0] <= diff:
            self.queue.popleft()
        if len(self.queue) < self.max_requests:
            self.queue.append(current_time)
            print(f"{current_time} - Processed")
            return True
        else:
            print(f"{current_time} - Rate Limited")
            return False

