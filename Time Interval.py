# Объект: интервал даты(часов, дней, лет). Реализовать операции с учѐтом столетия(0 до 99) и
# ограничений на дни (0 до 364) и часы (0 до 23), т.е. результат всегда от 0-0-0 до 23-364-99.
# Принять:(+) –сложение, (–) –вычитание,
# (== и !=) –сравнение, (bool) –проверка на ноль,
# (long)–преобразование в часы, (float)–преобразование в года(365 дней),
# (~) –дополнение до конца столетия.


class TimeInterval:
    def __init__(self, years=0, days=0, hours=0):

        self.years = years
        self.days = days
        self.hours = hours

        if self.years >= 0 and self.years <= 99:
            pass
        else:
            print('некорректно введены годы')
            raise ValueError

        if self.days >= 0 and self.days <= 364:
            pass
        else:
            print('некорректно введены дни')
            raise ValueError

        if self.hours >= 0 and self.hours <= 23:
            pass
        else:
            print('некорректно введены часы')
            raise ValueError

    def __str__(self):
        string_returned = ''
        if self.years == 0:
            string_returned += '0'
        else:
            string_returned = string_returned + str(self.years)

        if self.days == 0 and self.hours != 0:
            string_returned = string_returned + '-0-' + str(self.hours)
        elif self.days != 0:
            string_returned = string_returned + '-' + str(self.days) + '-' + str(self.hours)
        return string_returned

    def __add__(self, other):

        total_hours = (self.hours + other.hours) % 24
        add_days = (self.hours + other.hours) // 24

        total_days = (self.days + other.days + add_days) % 365
        add_years = (self.days + other.days + add_days) // 365

        total_years = (self.years + other.years + add_years) % 100

        return TimeInterval(total_years, total_days, total_hours)

    def __sub__(self, other):
        total_hours = (24 + self.hours - other.hours) % 24
        if other.hours == 0:
            sub_days = 0
        else:
            sub_days = self.hours // other.hours - 1

        total_days = (365 + self.days - other.days + sub_days) % 365
        sub_years = (self.days + sub_days) // other.days - 1

        total_years = (99 + self.years - other.years + sub_years) % 99
        return TimeInterval(total_years, total_days, total_hours)

    def __eq__(self, other):
        if self.years != other.years:
            return False
        else:
            if self.days != other.days:
                return False
            else:
                if self.hours != other.hours:
                    return False
                else:
                    return True

    def __ne__(self, other):
        if self.years != other.years:
            return True
        else:
            if self.days != other.days:
                return True
            else:
                if self.hours != other.hours:
                    return True
                else:
                    return False

    def __bool__(self):
        if self.years + self.days + self.hours == 0:
            return False
        else:
            return True

    def long(self):
        result = self.years * 365 * 24 + self.days * 24 + self.hours
        return result

    def __float__(self):
        result = self.years + self.days / 365 + self.hours / 365 / 24
        return result

    def __invert__(self):
        total_hours = (24 - self.hours) % 24
        sub_days = self.hours // 24 - 1

        total_days = (365 - self.days + sub_days) % 365
        sub_years = (self.days + sub_days) // 365 - 1

        total_years = (100 - self.years + sub_years) % 100
        return TimeInterval(total_years, total_days, total_hours)

a = TimeInterval(years = 3, days = 350, hours = 22)
b = TimeInterval(years = 10, days = 2, hours = 11)
c = TimeInterval(years = 98, days = 354, hours = 22)
print(a)
print(a+b)
print(b-a)
print(a == b)
print(a != b)
print(bool(a))
print(float(b))
print(a.long())
print(~c)
