from .service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, management_fee):
        self._management_fee = float(management_fee)

    def calculate_service_charges(self, account):
        # Use the correct date attribute; your BankAccount class uses 'date_created'
        if account.date_created > self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE + self._management_fee
        return self.BASE_SERVICE_CHARGE
