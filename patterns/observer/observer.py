class Observer:
    """Base class for observers in the Observer Pattern."""

    def update(self, subject, message):
        """
        This method should be implemented by subclasses to receive updates.
        :param subject: The subject sending the notification.
        :param message: The message or event data.
        """
        raise NotImplementedError("Subclasses must implement this method.")
