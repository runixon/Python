from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'postgresql://postgres:pass@localhost:5432/postgres'
engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)

class UserTable:
    def __init__(self):
        self.engine = engine
        self.session = Session()

    __scripts = {
        "select_all": text("SELECT * FROM users"),
        "select_by_id": text("SELECT * FROM users WHERE user_id = :user_id"),
        "insert": text("INSERT INTO users (user_id, user_email, subject_id) VALUES (:user_id, :user_email, :subject_id) RETURNING user_id"),
        "delete_by_id": text("DELETE FROM users WHERE user_id = :user_id RETURNING user_id, user_email, subject_id"),
        "update": text("UPDATE users SET user_email = :new_email, subject_id = :new_subject_id WHERE user_id = :user_id"),
        "get_all_ids": text("SELECT user_id FROM users")
    }

    def get_all_users(self):
        return self.session.execute(self.__scripts["select_all"]).fetchall()

    def get_user_by_id(self, user_id):
        return self.session.execute(self.__scripts["select_by_id"], {"user_id": user_id}).fetchall()

    def create_user(self, user_id, user_email, subject_id):
        result = self.session.execute(
            self.__scripts["insert"],
            {"user_id": user_id, "user_email": user_email, "subject_id": subject_id}
        )
        self.session.commit()
        return result.scalar()

    def delete_user_by_id(self, user_id):
        result = self.session.execute(self.__scripts["delete_by_id"], {"user_id": user_id})
        self.session.commit()
        return result.fetchone()

    def update_user(self, user_id, new_email, new_subject_id):
        self.session.execute(
            self.__scripts["update"],
            {"user_id": user_id, "new_email": new_email, "new_subject_id": new_subject_id}
        )
        self.session.commit()

    def find_unused_user_id(self):
        result = self.session.execute(self.__scripts["get_all_ids"]).fetchall()
        existing_ids = {row[0] for row in result}

        unused_id = 1
        while unused_id in existing_ids:
            unused_id += 1

        return unused_id

    def close(self):
        self.session.close()

user_table = UserTable()
