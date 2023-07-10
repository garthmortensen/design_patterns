class Subject:
    """Subject class represents the subject being observed.
    The Observer pattern is commonly used in scenarios where there is a one-to-many relationship between objects, and the objects need to be notified and updated when the state of the observed object changes.
    """

    def __init__(self):
        """Initialize the Subject object."""
        self.observers = []

    def attach(self, observer):
        """
        Attach an observer to the subject.

        Args:
            observer (Observer): The observer object to attach.
        """
        self.observers.append(observer)
        print(f"Attached observer: {observer.name}")

    def detach(self, observer):
        """
        Detach an observer from the subject.

        Args:
            observer (Observer): The observer object to detach.
        """
        self.observers.remove(observer)
        print(f"Detached observer: {observer.name}")

    def notify(self, data=None):
        """
        Notify all observers about an update.

        Args:
            data: Optional data to be passed to the observers.
        """
        print(f"Notifying observers with data: {data}")
        for observer in self.observers:
            observer.update(data)


class Observer:
    """Observer class represents the observer objects."""

    def __init__(self, name):
        """Initialize the Observer object with a name."""
        self.name = name

    def update(self, data):
        """
        Update the observer with new data.

        Args:
            data: The data received from the subject.
        """
        print(f"{self.name} received update with data: {data}")


# Example usage
subject = Subject()

# Create observers
observer1 = Observer("Observer 1")
observer2 = Observer("Observer 2")

# Attach observers to the subject
subject.attach(observer1)
subject.attach(observer2)

# Notify observers
subject.notify("Data for update")

# Detach observer1 from the subject
subject.detach(observer1)

# Notify observers again after detachment
subject.notify("Another data update")
