# Есть файл с протоколом регистраций пользователей на сайте (registrations.txt)
# Каждая строка содержит информацию о имени, электронной почте и возрасте человека.
#
#
# Надо проверить данные из файла, для каждой строки:
#  - присутсвуют все три поля
#  - поле имени содержит только буквы
#  - поле email содержит @ и .
#  - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
#  - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
#  - НЕ присутсвуют все три поля: ValueError
#  - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
#  - поле email НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
#  - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

good_log = open("registrations_good.log", "w", encoding='utf-8')
bad_log = open("registrations_bad.log", "w", encoding='utf-8')


class NotNameError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def not_name(name):
    if name.isalpha():
        pass
    else:
        raise NotNameError('Лишние символы в имени')
    return name


class NotEmailError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def not_email(e_mail):
    at = e_mail.find('@')
    dot = e_mail.find('.')
    if at != -1 and dot != -1:
        pass
    else:
        raise NotEmailError('что-то не так в e-mail')
    return e_mail


with open('registrations_.txt', 'r', encoding='utf-8') as ff:
    for line in ff:

        try:
            name, email, age = line.split(' ')
        except ValueError as exc:
            print('недостаточно данных', line)
            bad_log.write(line)

        else:
            try:
                not_name(name)

            except NotNameError as exc:
                print('имя содержит не только буквы', line)
                bad_log.write(line)
            else:
                try:
                    not_email(email)
                except NotEmailError as exc:
                    print('e-mail не корректен', line)
                    bad_log.write(line)
                else:
                    try:
                        if int(age) > 10 and int(age) < 99:
                            print('ok', age)
                        else:
                            raise ValueError('что-то не так с возрастом')
                    except ValueError as exc:
                        print('возраст не соответствует формату', line)
                        bad_log.write(line)
                    else:
                        good_log.write(line)

good_log.close()
bad_log.close()
