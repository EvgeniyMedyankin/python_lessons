class Staff:
    """Свойства"""

    def __init__(self, p_position, p_name, p_pay):
        self.position = p_position
        self.name = p_name
        self.pay = p_pay
        print('Creating Staff object')

    def __str__(self):
        return "Position = %s, Name = %s, Pay = %d" % (self.position, self.name, self.pay)

    def calculatePay(self):
        prompt = '\nEnter number of hours worked for %s: ' % self.name
        hours = input(prompt)
        prompt = 'Enter the hourly rate for %s: ' % self.name
        hourly_rate = input(prompt)
        self.pay = int(hours) * int(hourly_rate)
        return self.pay


office_staff = Staff('Basic', 'Yvonne', 0)
print(office_staff.calculatePay())
