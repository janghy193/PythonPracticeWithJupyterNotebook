class Member():
    def __init__(self, num, name, phone):
        self.num=num
        self.name=name
        self.phone=phone
    def __str__(self):
        return f"{self.num} {self.name} {self.phone}"