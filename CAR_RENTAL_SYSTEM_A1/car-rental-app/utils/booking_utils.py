import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def calculate_price(car_rate: float, start_date: str, end_date: str) -> float:
    try:
        date_format = "%Y-%m-%d"
        start = datetime.strptime(start_date, date_format)
        end = datetime.strptime(end_date, date_format)
        delta = end - start
        days = delta.days + 1

        if days <= 0:
            logger.warning(f"Invalid date range: start={start_date}, end={end_date}")
            return 0.0

        price = car_rate * days
        logger.debug(f"Calculated price: {price} for {days} days at rate {car_rate}")
        return price

    except ValueError as e:
        logger.error(f"Date parsing error: {e}")
        return 0.0
