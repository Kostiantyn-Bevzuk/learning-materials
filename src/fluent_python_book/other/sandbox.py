from datetime import datetime, timedelta
from operator import attrgetter


def get_time_period(now: datetime, interval: int):
    for attr in ["year", "month", "day", "hour"]:
        f = attrgetter(attr)
        time_period = list(set(f(now - timedelta(hours=i)) for i in range(interval)))
        yield time_period


# now = datetime.now()
# print("Current datetime:", now)
# time_periods = get_time_period(now, 3)

# for _ in range(4):
#     print(next(time_periods))


class A:

    @property
    def a(self):
        return 1
    
a = A()
print(a.a)