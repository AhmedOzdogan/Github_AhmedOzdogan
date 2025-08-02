from rest_framework.throttling import UserRateThrottle


class TenCallsPerMinute(UserRateThrottle):
    """
    Custom throttle class that allows 10 requests per minute for anonymous users.
    """
    scope = 'ten'