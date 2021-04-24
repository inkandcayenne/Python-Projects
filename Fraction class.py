# 1. Напишите класс `Fraction` для работы с дробями. Пусть дробь в нашем классе предстает в виде
# `числитель/знаменатель`. Дробное число должно создаваться по запросу `Fraction(a, b)`, где `a` – это числитель,
# а `b` – знаменатель дроби.
# 2. Добавьте возможность сложения (сложения через оператор сложения) для дроби.
# Предполагается, что операция сложения может проводиться как только между дробями, так и между дробью и целым числом.
# Результат оперции должен быть представлен в виде дроби.
# 3. Добавьте возможность взятия раздости (вычитания через оператор вычитания) для дробей.
# Предполагается, что операция вычитания может проводиться как только для двух дробей, так и для дроби и целого числа.
# Результат оперции должен быть представлен в виде дроби.
# 4. Добавьте возможность умножения (умножения через оператор умножения) для дробей.
# Предполагается, что операция умножения может проводиться как только для двух дробей, так и для дроби и целого числа.
# Результат оперции должен быть представлен в виде дроби.
# 5. Добавьте возможность приведения дроби к целому числу через стандартную функцию `int()`.
# 6. Добавьте возможность приведения дроби к числу с плавающей точкой через стандартную функцию `float()`.
# 7. Создайте дочерний класс `OperationsOnFraction` и добавьте туда собственные методы `getint` и `getfloat`,
# которые будут возвращять целую часть дроби и представление дроби в виде числа с плавающей точкой соответственно.

def common_denominator(x, y):
    while y != 0:
        x, y = y, x % y
    return x


class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '{}/{}'.format(self.a, self.b)

    def __add__(self, other):
        if isinstance(other, Fraction):
            c = int(other.b / common_denominator(x=other.b, y=self.b) * self.b / common_denominator(x=other.b,
                                                                                                    y=self.b) * common_denominator(
                x=other.b, y=self.b))
            result_1 = int(self.a * c / self.b + other.a * c / other.b)
            result_2 = c
            return '{}/{}'.format(result_1, result_2)
        else:
            result = self.a + other * self.b
            return '{}/{}'.format(result, self.b)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            c = int(other.b / common_denominator(x=other.b, y=self.b) * self.b / common_denominator(x=other.b,
                                                                                                    y=self.b) * common_denominator(
                x=other.b, y=self.b))
            result_1 = int(self.a * c / self.b - other.a * c / other.b)
            result_2 = c
            return '{}/{}'.format(result_1, result_2)
        else:
            result = self.a - other * self.b
            return '{}/{}'.format(result, self.b)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            result_1 = int(self.a * other.a)
            result_2 = int(self.b * other.b)
            return '{}/{}'.format(result_1, result_2)
        else:
            result = self.a * other
            return '{}/{}'.format(result, self.b)

    def __int__(self):
        result = int(self.a // self.b)
        return result

    def __float__(self):
        result = float(self.a / self.b)
        return result


class OperationsOnFraction(Fraction):
    def __init__(self, a, b):
        super().__init__(a=a, b=b)

    def getint(self):
        res = super().__int__()
        return res

    def getfloat(self):
        res = super().__float__()
        return res


# Examples
a = Fraction(23, 45)
b = Fraction(40, 50)
print(a, b)
print(a+b)
print(a-b)
print(a+230)
print(b-10)
print(a*b)
print(a*3)
print(int(a))
print(float(b))
c = OperationsOnFraction(10423, 576)
print(c.getfloat())
print(c.getint())
