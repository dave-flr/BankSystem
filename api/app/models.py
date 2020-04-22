from pony.orm import Database, Required

db = Database()


class User(db.Entity):
    login = Required(str, unique=True)
    password = Required(str)

