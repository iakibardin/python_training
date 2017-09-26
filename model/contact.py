from sys import maxsize
class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, photo_directory=None, title=None, company=None, address=None,
                       home_number=None, mobile_number=None, work_number=None, fax=None, email1=None, email2=None, email3=None, homepage=None, day_of_birth=None,
                       month_of_birth=None, year_of_birth=None, day_of_annivesary=None, month_of_annivesary=None, year_of_annivesary=None,
                       address2=None, home_number2=None, note=None, id=None, all_phones_from_home_page=None, all_emailes_from_home_page=None, hash = None):
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
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emailes_from_home_page = all_emailes_from_home_page
        self.hash = hash

        def str_or_no(string):
            if (string is None) or (string == ""):
                return ""
            else:
                return str(string)

        # для строк, после которых следует перенос \n
        def strn_or_no(string):
            if (string is None) or (string == ""):
                return ""
            else:
                return str(string) + '\n'

        def hash_str(self):
            self.hash = str_or_no(self.lastname) + str_or_no(self.firstname) + str_or_no(self.address) + \
                        strn_or_no(self.email1) + strn_or_no(self.email2) + str_or_no(self.email3) + \
                        strn_or_no(self.home_number) + strn_or_no(self.mobile_number) + strn_or_no(self.work_number) + str_or_no(self.fax)

        if hash is None:
            hash_str(self)
        else:
            self.hash = hash





# изменение полей контактов
    def fill_contact_values(self, contact):
        def hash_str(self):
            self.hash = str_or_no(self.lastname) + str_or_no(self.firstname) + str_or_no(self.company) + \
                        strn_or_no(self.email1)+ strn_or_no(self.email2)+ str_or_no(self.email3)+ \
                        strn_or_no(self.home_number) + strn_or_no(self.mobile_number) + strn_or_no(self.work_number) + str_or_no(self.fax)

        def str_or_no(string):
            if (string is None) or (string == ""):
                return ""
            else:
                return str(string)

        def strn_or_no(string):
            if (string is None) or (string == ""):
                return ""
            else:
                return str(string) +'\n'

        def fill_contact_value(a, b):
            if b is not None:
                return b
            else:
                return a

        self.firstname = fill_contact_value(self.firstname, contact.firstname)
        self.middlename = fill_contact_value(self.middlename, contact.middlename)
        self.lastname = fill_contact_value(self.lastname, contact.lastname)
        self.nickname = fill_contact_value(self.nickname, contact.nickname)
        self.title = fill_contact_value(self.title, contact.title)
        self.company = fill_contact_value(self.company, contact.company)
        self.address = fill_contact_value(self.address, contact.address)
        self.home_number = fill_contact_value(self.home_number, contact.home_number)
        self.mobile_number = fill_contact_value(self.mobile_number, contact.mobile_number)
        self.work_number = fill_contact_value(self.work_number, contact.work_number)
        self.fax = fill_contact_value(self.fax, contact.fax)
        self.email1 = fill_contact_value(self.email1, contact.email1)
        self.email2 = fill_contact_value(self.email2, contact.email2)
        self.email3 = fill_contact_value(self.email3, contact.email3)
        self.homepage = fill_contact_value(self.homepage, contact.homepage)
        hash_str(self)



    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
                and self.lastname == other.lastname and self.address == other.address

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize




