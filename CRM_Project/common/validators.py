from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_name(value):
    if not all(c.isalpha() or c == '-' or c == ' ' for c in value):
        raise ValidationError(
            _(f'{value} contains invalid characters'),
            params={'value': value},
        )


# def owner_not_in_users_validator(owner, users):
#     if owner in users.all():
#         raise ValidationError('Owner cannot be in the users list.')


def partner_code_validator(value):
    if value.isdigit():
        len_value = len(value)
        if len_value != 8 and len_value != 10:
            raise ValidationError(
                _(f'{value} invalid format'),
                params={'value': value},
            )
        elif len_value == 8:
            if not its_EDRPOU(value):
                raise ValidationError(
                    _(f'{value} not valid EDRPOU code'),
                    params={'value': value},
                )
    else:
        raise ValidationError(
            _(f'{value} contains invalid characters'),
            params={'value': value},
        )


def its_EDRPOU(code):
    first_and_second_char = int(code[0:2])
    if first_and_second_char < 30 or first_and_second_char > 60:
        coefficient = [1, 2, 3, 4, 5, 6, 7]
    else:
        coefficient = [7, 1, 2, 3, 4, 5, 6]
    sum_code = sum([x * int(y) for x, y in zip(coefficient, code[0:7])]) % 11
    if sum_code < 10:
        return sum_code == int(code[7])
    else:
        coefficient = [x + 2 for x in coefficient]
        sum_code = sum([x * int(y) for x, y in zip(coefficient, code[0:7])]) % 11
        if sum_code < 10:
            return sum_code == int(code[7])


def validate_unique_partner_contact_by_phones(instance):
    # Get all associated PartnerContactPerson for instance
    contact_people = instance.contact_person.all()
    print(contact_people)
    # Check that all phones are unique
    if len(contact_people) != len(set([person.phone for person in contact_people])):
        raise ValidationError('Each partner contact must have a unique phone number')


def validate_users_in_project(instance):
    # user_list = instance.users.all()
    print(instance.users)
    return
    # if self.owner.id in self.users.values_list('id', flat=True):
    #     print(self.owner.id)
    #     print(self.users.values_list('id', flat=True))
    #     raise ValidationError('Owner cannot be in the users list.')