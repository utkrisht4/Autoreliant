import logging

logging.basicConfig(
    filename="reports/test_failures.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_failure(message):
    logging.error(message)