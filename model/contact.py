from sys import maxsize
class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, photo_directory=None, title=None, company=None, address=None,
                       home_number=None, mobile_number=None, work_number=None, fax=None, email1=None, email2=None, email3=None, homepage=None, day_of_birth=None,
                       month_of_birth=None, year_of_birth=None, day_of_annivesary=None, month_of_annivesary=None, year_of_annivesary=None,
                       address2=None, home_number2=None, note=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo_directory = photo_directory
        self.title = title
        self.company = company
        self.address = address
        self.home_number = home_number
        self.mobile_number = mobile_number
        self.work_number = work_number
        self.fax =fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.day_of_birth = day_of_birth
        self.month_of_birth = month_of_birth
        self.year_of_birth = year_of_birth
        self.day_of_annivesary = day_of_annivesary
        self.month_of_annivesary = month_of_annivesary
        self.year_of_annivesary = year_of_annivesary
        self.address2 = address2
        self.home_number2 = home_number2
        self.note = note
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
                and self.lastname == other.lastname and self.address == other.address

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize









