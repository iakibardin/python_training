import mysql.connector
from model.group import Group
from model.contact import Contact
class DbFixture:
    # выборка всех контактов
    sel_all_cont = "select distinct a.id, a.firstname, a.middlename, a.lastname, a.nickname, a.address, " \
                   "a.email, a.email2, a.email3, a.home, a.mobile, a.work, a.phone2 " \
                   "from addressbook as a where a.deprecated = '0000-00-00 00:00:0'"


    def __init__(self, host,name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list ")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    # функция возвращает список контактов из произвольного запроса
    def get_contact_list_from_sel(self, sel):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(sel)
            for row in cursor.fetchall():
                (id, firstname, middlename, lastname, nickname, address, email, email2, email3, home, mobile,
                work, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname,
                                            nickname=nickname,
                                            address=address, email1=email, email2=email2, email3=email3,
                                            home_number=home, mobile_number=mobile,
                                            work_number=work, home_number2=phone2))
        finally:
                cursor.close()

        return list

    # все контакты
    def get_contact_list(self):
        return self.get_contact_list_from_sel(self.sel_all_cont)


    def destroy(self):
        self.connection.close()


































#    def get_contact_list(self):
#        list = []
#        cursor = self.connection.cursor()
#        try:
#            cursor.execute("select id, firstname, lastname, address from addressbook where deprecated = '0000-00-00 00:00:00'")
#            for row in cursor:
#                (id, firstname, lastname, address) = row
#                list.append(Contact(id=str(id),firstname=firstname, lastname=lastname, address=address))
#        finally:
#            cursor.close()
#        return list

#    def destroy(self):
#            self.connection.close()

    #email, email2, email3, home, mobile, work, fax*

