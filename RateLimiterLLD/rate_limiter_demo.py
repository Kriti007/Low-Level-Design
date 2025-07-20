from sliding_window_log import SlidingWindowLog
from fixed_window_counter import FixedWindowCounter
from token_bucket import TokenBucket
from rate_limiting_strategy import RateLimiterStrategy
from rate_limiter_factory import RateLimiterFactory
from rate_limiter_types import RateLimiters

import time


class RateLimiterDemo:
    def __init__(self, rate_limiter: RateLimiterStrategy):
        self.rate_limiter = rate_limiter

    def allow_request(self):
        if isinstance(self.rate_limiter, TokenBucket):
            for i in range(15):
                if self.rate_limiter.allow_request():
                    print("processed")
                else:
                    print("rate limited")
                time.sleep(1)

        elif isinstance(self.rate_limiter, SlidingWindowLog):
            self.rate_limiter.allow_request(1)
            self.rate_limiter.allow_request(3)
            self.rate_limiter.allow_request(5)
            self.rate_limiter.allow_request(6)
            self.rate_limiter.allow_request(7)
            self.rate_limiter.allow_request(9)
            self.rate_limiter.allow_request(10)
            self.rate_limiter.allow_request(15)
            self.rate_limiter.allow_request(18)

        elif isinstance(self.rate_limiter, FixedWindowCounter):
            self.rate_limiter = FixedWindowCounter(5, 3)
            for i in range(10):
                if self.rate_limiter.allow_request():
                    print("Processed")
                else:
                    print("Rate Limited")
                time.sleep(1.0)


def main():
    # choose any one of these configs
    config = {"type": RateLimiters.TOKEN_BUCKET, "capacity": 5, "refill_amount": 2, "refill_window": 5, "tokens": 10}
    # config = {"type": RateLimiters.SLIDING_WINDOW_LOG, "window_size": 10, "max_requests": 5}
    # config = {"type": RateLimiters.FIXED_WINDOW, "window_size": 5, "max_requests": 3}
    rate_limiter = RateLimiterFactory.create(config)
    obj = RateLimiterDemo(rate_limiter)
    obj.allow_request()


if __name__ == "__main__":
    main()
