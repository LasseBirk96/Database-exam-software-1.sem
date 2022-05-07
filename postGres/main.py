from database import table, user_queries

#SETS UP THE TABLE
table.set_up_user_table()

#PERSISTS A USER
user_queries.persist_user("Albus", "Dumbledore", "supersecretPassword", 110, "grindelwald4lyfe@gmail.com", "32435465")


#Successful login
user_queries.user_login("grindelwald4lyfe@gmail.com", "supersecretPassword")

#Unsuccessful login, currently throws exception if email doesnt exist, fix this later
user_queries.user_login("grindelwald4lyfe@gmail.com", "notsecret")