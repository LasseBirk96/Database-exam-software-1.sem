import sys

sys.path.append("postGres")
import uuid
from .connector import establish_connection
from flask_bcrypt import Bcrypt
from flask import Flask
import uuid
from entities.User import User

app = Flask(__name__)
bcrypt = Bcrypt(app)


def persist_user(first_name, last_name, password, age, email, phone_number):
    user_id = str(uuid.uuid4())
    passwd = bytes(
        password, encoding="utf-8"
    )  # Creates hashed password, NEVER store passwords in plain text
    pw_hash = bcrypt.generate_password_hash(passwd)
    undecoded_hash = pw_hash.decode("utf-8")
    user = User(
        user_id, first_name, last_name, undecoded_hash, age, email, phone_number
    )
    persist_user_query = "INSERT INTO users (user_id, first_name, last_name, password, age, email, phonenumber) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    conn = establish_connection()
    cur = conn.cursor()
    # Execute the tuple with tables
    try:
        cur.execute(persist_user_query, user.return_user())
        conn.commit()
        return "Successfully committed user " + email + " to databæse"
    except (Exception) as error:
        print("ERROR IN persistence", error)
    finally:
        if conn is not None:
            conn.close()


def user_login(user_email, user_password):
    conn = establish_connection()
    cur = conn.cursor()
    user_login_query = "SELECT user_id, password FROM users WHERE email = %s"
    try:
        cur.execute(user_login_query, (user_email,))
        entries = cur.fetchall()[0]
        sql_data_password = entries[1]
        sql_pass = bytes(sql_data_password, encoding="utf-8")
        password = bytes(user_password, encoding="utf-8")
        if bcrypt.check_password_hash(sql_pass, password):  # returns True
            return entries[0]
        else:
            print("FAILED LOG IN")
    except (Exception) as error:
        print("ERROR IN logging in", error)
    finally:
        if conn is not None:
            conn.close()


def delete_user(user_email):
    conn = establish_connection()
    cur = conn.cursor()
    user_delete_query = "DELETE FROM users WHERE email = %s"
    try:
        cur.execute(user_delete_query, (user_email,))
        conn.commit()
        return "Successfully deleted user" + user_email
    except (Exception) as error:
        print("ERROR IN deleting", error)
    finally:
        if conn is not None:
            conn.close()


def update_user(user_email, new_phonenumber):
    conn = establish_connection()
    cur = conn.cursor()
    user_delete_query = "UPDATE users SET phonenumber = %s WHERE email = %s"
    try:
        cur.execute(user_delete_query, (new_phonenumber, user_email))
        conn.commit()
        return (
            "Successfully updated user "
            + user_email
            + " phonenumber to "
            + new_phonenumber
        )
    except (Exception) as error:
        print("ERROR IN deleting", error)
    finally:
        if conn is not None:
            conn.close()


def get_user_by_id(user_id):
    conn = establish_connection()
    cur = conn.cursor()
    user_delete_query = "SELECT * FROM users WHERE user_id = %s"
    try:
        cur.execute(user_delete_query, (user_id,))
        user = cur.fetchall()
        return user
    except (Exception) as error:
        print("ERROR IN selecting", error)
    finally:
        if conn is not None:
            conn.close()


def get_user(user_email):
    conn = establish_connection()
    cur = conn.cursor()
    user_delete_query = "SELECT * FROM users WHERE email = %s"
    try:
        cur.execute(user_delete_query, (user_email,))
        user = cur.fetchall()
        return user
    except (Exception) as error:
        print("ERROR IN selecting", error)
    finally:
        if conn is not None:
            conn.close()
