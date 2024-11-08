class Order:
    def __init__(self, items, q, p):
        self.items = items
        self.q = q
        self.p = p

    def calc(self):
        tax_rate = 0.1  
        total = self.q * self.p
        total_with_tax = total + (total * tax_rate)
        return total_with_tax

    def save(self):
        print("Saving order to DB...")

    def notify(self):
        print("Sending email...")

#improvement

from abc import ABC, abstractmethod

# Константа для налоговой ставки
TAX_RATE = 0.1

class Order:
    """Класс для хранения данных о заказе."""
    def __init__(self, item_name, quantity, unit_price):
        self.item_name = item_name
        self.quantity = quantity
        self.unit_price = unit_price

class OrderCalculator:
    """Класс для расчета стоимости заказа с учетом налогов."""
    def __init__(self, tax_rate):
        self.tax_rate = tax_rate

    def calculate_total_with_tax(self, order):
        total = order.quantity * order.unit_price
        total_with_tax = total + (total * self.tax_rate)
        return total_with_tax

class NotificationService(ABC):
    """Абстрактный класс для отправки уведомлений."""
    @abstractmethod
    def send_notification(self, message):
        pass

class EmailNotificationService(NotificationService):
    """Класс для отправки уведомлений по электронной почте."""
    def send_notification(self, message):
        print(f"Sending email: {message}")

class SMSNotificationService(NotificationService):
    """Класс для отправки уведомлений по SMS."""
    def send_notification(self, message):
        print(f"Sending SMS: {message}")

# Пример использования
order = Order("Laptop", 2, 1000)
calculator = OrderCalculator(TAX_RATE)
email_service = EmailNotificationService()
sms_service = SMSNotificationService()

# Расчет и отправка уведомлений
print(f"Total price with tax: {calculator.calculate_total_with_tax(order)}")
email_service.send_notification("Order has been placed.")
sms_service.send_notification("Order has been placed.")

