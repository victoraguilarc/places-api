# -*- coding: utf-8 -*-

import pytest
from expects import be_a, be_empty, be_true, equal, expect

from src.common.database.models import UserORM


@pytest.mark.django_db
def test_string_representation(user_orm: UserORM):
    expect(str(user_orm)).to(equal(user_orm.username))


@pytest.mark.django_db
def test_change_password(user_orm: UserORM):
    new_password = 'new_password'
    user_orm.change_password(new_password)

    expect(user_orm.check_password(new_password)).to(be_true)


@pytest.mark.django_db
def test_verbose_name():
    expect(UserORM._meta.verbose_name).to(equal('User'))


@pytest.mark.django_db
def test_verbose_name_plural():
    expect(UserORM._meta.verbose_name_plural).to(equal('Users'))


@pytest.mark.django_db
def test_save_with_username_blank(user_orm: UserORM):
    user_orm.username = ' '
    user_orm.save()

    expect(user_orm.username).to(be_a(str))
    expect(user_orm.username).not_to(be_empty)


@pytest.mark.django_db
def test_save_with_username_none(user_orm: UserORM):
    user_orm.username = None
    user_orm.save()

    expect(user_orm.username).to(be_a(str))
    expect(user_orm.username).not_to(be_empty)
