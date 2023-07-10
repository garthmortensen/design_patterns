import random

# this seems closer, but im not sure its the best design pattern

class StockTicker:
    """StockTicker class represents a stock ticker subject."""

    def __init__(self, symbol):
        """Initialize the StockTicker object with a stock symbol."""
        self.symbol = symbol
        self.observers = []

    def attach(self, observer):
        """
        Attach an observer to the stock ticker.

        Args:
            observer (Observer): The observer object to attach.
        """
        self.observers.append(observer)
        print(f"Attached observer: {observer.name}")

    def detach(self, observer):
        """
        Detach an observer from the stock ticker.

        Args:
            observer (Observer): The observer object to detach.
        """
        self.observers.remove(observer)
        print(f"Detached observer: {observer.name}")

    def generate_price(self):
        """Generate a random stock price."""
        return round(random.uniform(50, 200), 2)

    def update_price(self):
        """Update the stock price and notify all observers."""
        price = self.generate_price()
        print(f"New price for {self.symbol}: ${price}")
        self.notify(price)

    def notify(self, price):
        """
        Notify all observers about the updated stock price.

        Args:
            price: The updated stock price.
        """
        print(f"Notifying observers of {self.symbol} with price: ${price}")
        for observer in self.observers:
            observer.update(self.symbol, price)


class StockMarketDashboard:
    """StockMarketDashboard class represents an observer component."""

    def __init__(self, name):
        """Initialize the StockMarketDashboard object with a name."""
        self.name = name

    def update(self, symbol, price):
        """
        Update the dashboard with the new stock price.

        Args:
            symbol: The stock symbol.
            price: The updated stock price.
        """
        print(f"{self.name} received update for {symbol} with price: ${price}")


# Example usage
ticker = StockTicker("AAPL")

# Create stock market dashboards
dashboard1 = StockMarketDashboard("Dashboard 1")
dashboard2 = StockMarketDashboard("Dashboard 2")

# Attach dashboards to the ticker
ticker.attach(dashboard1)
ticker.attach(dashboard2)

# Update ticker price and notify observers
ticker.update_price()

# Detach dashboard1 from the ticker
ticker.detach(dashboard1)

# Update ticker price again and notify observers
ticker.update_price()
