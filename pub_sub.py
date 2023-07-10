# This is not what i want.

class EventBroker:
    """EventBroker class represents a central hub for publishing and subscribing to events.
    The Publish-Subscribe (or Publisher-Subscriber) design pattern is commonly used in scenarios where there is a need for loose coupling and asynchronous communication between components
    """

    def __init__(self):
        """Initialize the EventBroker object."""
        self.subscribers = {}

    def subscribe(self, event_type, subscriber):
        """
        Subscribe a subscriber to a specific event type.

        Args:
            event_type (str): The type of event to subscribe to.
            subscriber (Subscriber): The subscriber object to register.
        """
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(subscriber)
        print(f"Subscribed {subscriber.name} to event '{event_type}'")

    def unsubscribe(self, event_type, subscriber):
        """
        Unsubscribe a subscriber from a specific event type.

        Args:
            event_type (str): The type of event to unsubscribe from.
            subscriber (Subscriber): The subscriber object to unregister.
        """
        if event_type in self.subscribers:
            self.subscribers[event_type].remove(subscriber)
            print(f"Unsubscribed {subscriber.name} from event '{event_type}'")

    def publish(self, event_type, data=None):
        """
        Publish an event to all subscribers of a specific event type.

        Args:
            event_type (str): The type of event to publish.
            data: Optional data to be passed to the subscribers.
        """
        if event_type in self.subscribers:
            for subscriber in self.subscribers[event_type]:
                subscriber.notify(event_type, data)


class Subscriber:
    """Subscriber class represents the objects that subscribe to events."""

    def __init__(self, name):
        """Initialize the Subscriber object with a name."""
        self.name = name

    def notify(self, event_type, data):
        """
        Receive and process an event notification.

        Args:
            event_type (str): The type of event received.
            data: The data associated with the event.
        """
        print(f"{self.name} received event '{event_type}' with data: {data}")


# Example usage
broker = EventBroker()

# Create subscribers
subscriber1 = Subscriber("Subscriber 1")
subscriber2 = Subscriber("Subscriber 2")

# Subscribe subscribers to specific event types
broker.subscribe("event_type1", subscriber1)
broker.subscribe("event_type2", subscriber2)
broker.subscribe("event_type2", subscriber1)

# Publish events
broker.publish("event_type1", "Data for event type 1")
broker.publish("event_type2", "Data for event type 2")

# Unsubscribe subscriber1 from event_type2
broker.unsubscribe("event_type2", subscriber1)

# Publish event again after unsubscription
broker.publish("event_type2", "Data for event type 2")
