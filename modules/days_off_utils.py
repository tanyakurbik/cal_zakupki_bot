from datetime import datetime, timedelta

import yaml
from dateutil.parser import parse


class DaysOff:
    def __init__(self, path_to_days_off="../days_off.yaml"):
        self.dates = set()
        with open(path_to_days_off) as days_off_file:
            data = yaml.safe_load(days_off_file)
            for year in data:
                for month in data[year]:
                    for day in data[year][month]:
                        self.dates.add(parse(f"{day}.{month}.{year}").date())

    def is_day_off(self, date: datetime.date):
        # print(date)
        return date in self.dates

    def plus_n_workdays(self, start_date: datetime.date, number_of_workdays: int):
        result_date = start_date
        for _ in range(number_of_workdays):
            result_date += timedelta(days=1)
            if self.is_day_off(result_date):
                result_date += timedelta(days=1)
        return result_date

    def plus_n_calendar_days(self, start_date, number_of_days):
        result_date = start_date + timedelta(days=number_of_days)
        if self.is_day_off(result_date):
            return self.plus_n_workdays(result_date, 1)
        return result_date


if __name__ == "__main__":
    days_off = DaysOff()
    print(days_off.plus_n_calendar_days(parse("23.04.2021").date(), 9))
