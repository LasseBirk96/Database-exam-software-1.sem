import uuid
from database.connector import establish_connection
from flask_bcrypt import Bcrypt
from flask import Flask
import uuid
from entities.User import User
app = Flask(__name__)
bcrypt = Bcrypt(app)


def persist_user(first_name, last_name, password, age, email, phone_number):
    user_id = str(uuid.uuid4())
    passwd = bytes(password, encoding= 'utf-8') #Creates hashed password, NEVER store passwords in plain text
    pw_hash = bcrypt.generate_password_hash(passwd)
    undecoded_hash = pw_hash.decode('utf-8')
    user = User(user_id, first_name, last_name, undecoded_hash, age, email, phone_number)
    persist_user_query = ("INSERT INTO users (user_id, first_name, last_name, password, age, email, phonenumber) VALUES (%s, %s, %s, %s, %s, %s, %s)")
    conn = establish_connection()
    cur = conn.cursor()
    #Execute the tuple with tables
    try:
        cur.execute(persist_user_query, user.return_user())
        conn.commit()
        print("Successfully committed user to databæse")
    except (Exception) as error:
        print("ERROR IN persistence",error)
    finally:
        if conn is not None:
            conn.close()