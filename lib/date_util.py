import datetime


def get_current_date_str() -> str:
    return datetime.datetime.now().strftime('%Y%m%d')


def get_date_before(days) -> str:
    now = datetime.datetime.now()
    return (now - datetime.timedelta(days)).strftime('%Y%m%d')


if __name__ == '__main__':
    print(get_current_date_str())
    print(get_date_before(3))
