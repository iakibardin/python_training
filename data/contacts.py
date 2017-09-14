from model.contact import Contact
import random
import string

constant = [
    Contact(firstname="firstname1", lastname="lastname1", middlename="middlename1", nickname="nickname1",
            title="title1"),
    Contact(firstname="firstname2", lastname="lastname2", middlename="middlename2", nickname="nickname2",
            title="title2")
]





def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits +  " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname=firstname, lastname=lastname, middlename=middlename, nickname=nickname, photo_directory=photo_directory,
            title=title,
                     company=company, address=address, home_number="11111", mobile_number="22222", work_number="33333",
                     fax="44444", email1="mail1", email2="mail2", email3="mail3", homepage="test.com",
                     day_of_birth="//div[@id='content']/form/select[1]//option[3]",
                     month_of_birth="//div[@id='content']/form/select[2]//option[2]", year_of_birth="1990",
                     day_of_annivesary="//div[@id='content']/form/select[3]//option[3]",
                     month_of_annivesary="//div[@id='content']/form/select[4]//option[2]", year_of_annivesary="2010",
                     address2=address2,
                     home_number2="55555", note="testnote"
            )
    for firstname in [random_string("firstname", 20)]
    for lastname in [random_string("lastname", 20)]
    for middlename in [random_string("middlename", 20)]
    for nickname in [random_string("nickname", 20)]
    for photo_directory in ["C:\\Users\\ikibardin\\Desktop\\newscreen.jpg"]
    for title in [random_string("title", 20)]
    for company in [random_string("company", 20)]
    for address in [random_string("address", 20)]
    for address2 in [random_string("address2", 20)]
    for note in [random_string("note", 20)]
]