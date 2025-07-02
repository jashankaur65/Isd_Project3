from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email

class Client(Observer):
    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer")
        self.__client_number = client_number

        if len(first_name.strip()) == 0:
            raise ValueError("First name cannot be blank")
        self.__first_name = first_name

        if len(last_name.strip()) == 0:
            raise ValueError("Last name cannot be blank")
        self.__last_name = last_name

        try:
            valid = validate_email(email_address)
            self.__email_address = valid.normalized
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"

    @property
    def client_number(self):
        return self.__client_number

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def email_address(self):
        return self.__email_address

    def update(self, subject, message):
        simulate_send_email(self.__email_address, "Account Notification", message)
        print(f"Notification sent to {self}: {message}")

    def __str__(self):
        return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}"
