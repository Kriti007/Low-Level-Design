from rate_limiting_strategy import RateLimiterStrategy
from rate_limiter_types import  RateLimiters
from token_bucket import TokenBucket
from sliding_window_log import SlidingWindowLog
from fixed_window_counter import FixedWindowCounter


class RateLimiterFactory:
    @staticmethod
    def create(config: dict) -> RateLimiterStrategy:
        if config:
            rl_type = config["type"]
            if rl_type == RateLimiters.TOKEN_BUCKET:
                return TokenBucket(config["tokens"], config["refill_window"], config["capacity"], config["refill_amount"])
            if rl_type == RateLimiters.SLIDING_WINDOW_LOG:
                return SlidingWindowLog(config["window_size"], config["max_requests"])
            if rl_type == RateLimiters.FIXED_WINDOW:
                return FixedWindowCounter()
            else:
                raise ValueError("Invalid Rate Limiter Type")
        else:
            raise ValueError("No config provided")

