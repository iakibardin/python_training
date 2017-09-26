from model.group import Group
import random


def test_modify_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "test", header="test", footer="test"))
    old_groups = db.get_group_list()
    group_old = random.choice(old_groups)
    index = old_groups.index(group_old)
    group_new = Group(name="modified_name", header="modified_header", footer="modified_footer", id = group_old.id)
    app.group.modify_group_by_id(group_old.id, group_new)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group_new
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key= Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)




#def test_modify_group_name(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name = "test"))
#    old_groups = app.group.get_group_list()
#    index = randrange(len(old_groups))
#    group = Group(name="New group")
#    group.id = old_groups[index].id
#    app.group.modify_group_by_index(group, index)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[index] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key= Group.id_or_max)
