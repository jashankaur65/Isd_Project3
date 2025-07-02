from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """Base class for service charge strategies."""
    
    BASE_SERVICE_CHARGE = 5.0

    @abstractmethod
    def calculate_service_charges(self, account):
        """
        Calculate service charges for a given account.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")
