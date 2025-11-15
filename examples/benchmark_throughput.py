"""Simple throughput benchmark for DynamicRateLimiter.

This is NOT a strict micro-benchmark, but a rough way to see how the
limiter behaves under load. It does NOT hit any real external API;
it just simulates requests in-process.
"""

import time

from api_ratelimiter import DynamicRateLimiter


def run_benchmark(num_requests: int = 200) -> None:
    limiter = DynamicRateLimiter(
        initial_rate=5.0,
        min_rate=0.5,
        max_rate=20.0,
        increase_step=0.5,
        decrease_factor=0.5,
    )

    start = time.perf_counter()

    for i in range(num_requests):
        limiter.acquire()
        # Simulate success for most, with occasional backoff signal
        if i % 50 == 0 and i > 0:
            limiter.on_429(retry_after=0.5)
        else:
            limiter.on_success()

    duration = time.perf_counter() - start
    snap = limiter.snapshot()

    print(f"Executed {num_requests} simulated requests in {duration:.2f}s")
    print(f"Approx throughput: {num_requests / duration:.2f} req/s")
    print("Final limiter snapshot:", snap)


if __name__ == "__main__":
    run_benchmark()
