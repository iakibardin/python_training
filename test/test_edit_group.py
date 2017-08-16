from model.group import Group

def test_edit_first_group(app):

    app.group.edit_first_group(Group(name="22222", header="2222", footer="222"))
