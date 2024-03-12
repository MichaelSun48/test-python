import sentry_sdk

sentry_sdk.init(
    dsn="https://ae6f60ef51077bf31b2d47712f41ce59@sun-dev.ngrok.dev/10",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
)

division_by_zero = 1 / 0
