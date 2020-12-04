from common.session import AdventSession

session = AdventSession(day=4, year=2020)
data = session.data.strip()
data = data.split('\n\n')  # each passport


class Passport:
    accepted_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    VALIDATIONS = {
        'byr': lambda val: val.isdigit() and 1920 <= int(val) <= 2002,
        'iyr': lambda val: val.isdigit() and 2010 <= int(val) <= 2020,
        'eyr': lambda val: val.isdigit() and 2020 <= int(val) <= 2030,
        'hgt': lambda val: (
                (val.endswith('cm') and 150 <= int(val[:-2]) <= 193)
                or (val.endswith('in') and 59 <= int(val[:-2]) <= 76)
        ),
        'hcl': lambda val: (
                val[0] == '#'
                and all(char in '0123456789abcdef' for char in val[1:])
        ),
        'ecl': lambda val: (
                val in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
        ),
        'pid': lambda val: val.isdigit() and len(val) == 9,
        'cid': lambda val: True
    }

    def __init__(self, fields: list):
        """
        Creates a ``Passport`` object
        :param fields: a list of strings in the form ``key:value`` containing
            the passport fields
        """
        self.raw = ' '.join(fields)
        self.fields = dict()
        for key, val in [f.split(':') for f in fields]:
            self.fields[key] = val

    def has_required_fields(self) -> bool:
        """
        :return: Whether the passport has all the required fields
        """
        for field in self.required_fields:
            if field not in self.fields:
                return False
        return True

    def has_valid_required_fields(self) -> bool:
        """
        :return: Whether the passport has all valid required fields
        """
        return self.has_required_fields() and self.has_valid_fields()

    def has_valid_fields(self) -> bool:
        """
        :return: Whether all the passports' fields are valid
        """
        for field in self.fields:
            validator = self.VALIDATIONS[field]
            is_valid = validator(self.fields[field])
            if not is_valid:
                return False
        return True


def part1():
    out = 0
    for passport_data in data:
        fields = passport_data.split()
        passport = Passport(fields)
        if passport.has_required_fields():
            out += 1
    return out


print(part1())


def part2():
    out = 0
    for passport_data in data:
        fields = passport_data.split()
        passport = Passport(fields)
        if passport.has_valid_required_fields():
            out += 1
    return out


print(part2())

# session.submit(part1(), part=1)
# session.submit(part2(), part=2)

# session.submit(part1(), part=2)
