import pytest
from DB  import UserTable

@pytest.fixture
def database():
    db = UserTable()
    yield db
    db.close()

def test_find_unused_user_id(database):
    unused_id = database.find_unused_user_id()
    assert unused_id is not None
    print(f"Найден неиспользуемый user_id: {unused_id}")

def test_create_user(database):
    unused_id = database.find_unused_user_id()
    user_email = "new.user@example.com"
    subject_id = 5

    user_id = database.create_user(unused_id, user_email, subject_id)
    assert user_id == unused_id

    rows = database.get_user_by_id(user_id)
    assert len(rows) == 1
    assert rows[0]._mapping["user_email"] == user_email
    assert rows[0]._mapping["subject_id"] == subject_id

def test_update_user(database):
    unused_id = database.find_unused_user_id()
    user_email = "old.user@example.com"
    subject_id = 10

    # Создаем пользователя с тем же user_id
    database.create_user(unused_id, user_email, subject_id)

    # Обновляем только email и subject_id, но user_id остается прежним
    new_email = "updated.user@example.com"
    new_subject_id = 15
    database.update_user(unused_id, new_email, new_subject_id)

    # Проверяем, что обновился только email и subject_id
    rows = database.get_user_by_id(unused_id)
    assert len(rows) == 1
    assert rows[0]._mapping["user_id"] == unused_id  # user_id не изменился
    assert rows[0]._mapping["user_email"] == new_email
    assert rows[0]._mapping["subject_id"] == new_subject_id

def test_delete_user(database):
    unused_id = database.find_unused_user_id()
    user_email = "temp.user@example.com"
    subject_id = 7

    database.create_user(unused_id, user_email, subject_id)

    deleted_user = database.delete_user_by_id(unused_id)
    assert deleted_user is not None
    assert deleted_user[0] == unused_id
    assert deleted_user[1] == user_email
    assert deleted_user[2] == subject_id

    rows = database.get_user_by_id(unused_id)
    assert len(rows) == 0
