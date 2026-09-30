"""Simple table model used by the restaurant booking pages."""


class Table:
    def __init__(self, number, zone, seats, minimum, status, customer, date, time, guests):
        self.number = number
        self.zone = zone
        self.seats = seats
        self.minimum = minimum
        self.status = status
        self.customer = customer
        self.date = date
        self.time = time
        self.guests = guests

    def describe(self):
        if self.status == "reserved":
            return "จองแล้ว"
        return "ว่างพร้อมรับจอง"
