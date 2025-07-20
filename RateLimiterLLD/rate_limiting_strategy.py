from abc import ABC, abstractmethod


class RateLimiterStrategy(ABC):
    @abstractmethod
    def allow_request(self, user_id: str) -> bool:
        pass