import re
from datetime import datetime
from utils.constants import EMAIL_REGEX, PHONE_REGEX


def validate_id(value):
    return isinstance(value, int) and value > 0


def validate_string(value, min_len=1):
    return isinstance(value, str) and len(value.strip()) >= min_len


def validate_email(email):
    return re.match(EMAIL_REGEX, email) is not None


def validate_phone(phone):
    return re.match(PHONE_REGEX, phone) is not None


def validate_non_empty_list(value, min_len=1):
    return isinstance(value, list) and len(value) >= min_len


def validate_number(value, data_type=int, min_value=0, max_value=None):
    if max_value:
        return isinstance(value, data_type) and value > min_value > value
    else:
        return isinstance(value, data_type) and value > min_value


def validate_past_date(date):
    return isinstance(date, datetime) and date <= datetime.now()


def validate_enum(value, enum):
    return value in enum
