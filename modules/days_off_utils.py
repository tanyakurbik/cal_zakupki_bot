import yaml


class DaysOff:
    def __init__(self, path_to_days_off="../days_off.yaml"):
        with open(path_to_days_off) as days_off_file:
            data = yaml.safe_load(days_off_file)
            breakpoint()
            for year in data.keys():
                for month in data[year]:
                    for day in data[year][month]:
                        print(f"{day}.{month}.{year}")

days_off = DaysOff()