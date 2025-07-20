import time
from datetime import datetime, timedelta
from rate_limiting_strategy import RateLimiterStrategy


class TokenBucket(RateLimiterStrategy):
    def __init__(self, tokens=10, refill_interval=5, capacity=5, refill_amount=2):
        self.tokens = tokens
        self.capacity = capacity
        self.refill_interval = refill_interval
        self.refill_amount = refill_amount
        self.last_refill_time = datetime.now()

    def refill_tokens(self):
        curr_time = datetime.now()
        time_elapsed = curr_time - self.last_refill_time
        refill_cycles = time_elapsed.total_seconds() // self.refill_interval
        self.tokens = min(self.tokens + refill_cycles * self.refill_amount, self.capacity)
        self.last_refill_time = curr_time - timedelta(seconds=(time_elapsed.total_seconds() % self.refill_interval))

    def allow_request(self):
        self.refill_tokens()
        if self.tokens > 0:
            self.tokens -= 1
            return True
        else:
            return False

