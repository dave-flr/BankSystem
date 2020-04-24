from datetime import datetime

from pony.orm import Database, Required, Optional, PrimaryKey, Set

db = Database()


class Customer(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    last_name = Required(str)
    id_card = Required(str, unique=True)
    passport = Optional(str, unique=True)
    direction = Required(str)
    phone_number = Required(str, unique=True)
    email = Required(str, unique=True)
    birth_date = Required(str)
    created_at = Required(str, default=datetime.now().strftime("%c"))

    # Login credentials
    username = Required(str, unique=True)
    password_hash = Required(str)

    access_failed_count = Required(int, sql_default='0')

    saving_accounts = Set(lambda: SavingAccount)


class SavingAccount(db.Entity):
    id = PrimaryKey(int, auto=True)
    creation_date = Required(str)
    freeze_start_date = Required(str)
    freeze_end_date = Required(str)
    currency_type = Required(str)
    freeze = Required(bool)
    amount = Required(float)
    amount_gained = Required(float)

    customer = Required(Customer)  # A saving Account has a Customer

    deposit_certificates = Set(lambda: TransactionCertificate)  # A saving account has many deposit certificates


class TransactionCertificate(db.Entity):
    id = PrimaryKey(int, auto=True)
    date_hour = Required(str)
    currency = Required(str)
    amount = Required(str)
    balance = Required(str)
    type = Required(str)  # Deposit or Withdrawal

    saving_account = Required(SavingAccount)
