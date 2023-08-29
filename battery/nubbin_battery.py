from abc import ABC

from car import Car


class NubbinBattery(Battery):

    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days > 730  # 2 years