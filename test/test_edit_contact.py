from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="update", middlename="update", lastname="update", nickname="update",
                               photo_directory="C:\\Users\\ikibardin\\Desktop\\newscreen.jpg", title="update",
                               company="update", address="update", home_number="update", mobile_number="update",
                               work_number="update", fax="update", email1="update", email2="update", email3="update",
                               homepage="update.com",
                               day_of_birth="//div[@id='content']/form/select[1]//option[4]",
                               month_of_birth="//div[@id='content']/form/select[2]//option[3]", year_of_birth="1995",
                               day_of_annivesary="//div[@id='content']/form/select[3]//option[4]",
                               month_of_annivesary="//div[@id='content']/form/select[4]//option[3]",
                               year_of_annivesary="2015", address2="update update update 2",
                               home_number2="update update update 3", note="updatetestnote"))
    app.session.logout()