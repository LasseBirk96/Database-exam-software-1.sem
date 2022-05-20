from database import table, user_queries

def run_setup():

    #This is just to provide proof of CRUD operations, delete table first if you already have one version up

    #SETS UP THE TABLE
    table.set_up_user_table()

    #PERSISTS A USER
    user_queries.persist_user("Albus", "Dumbledore", "supersecretPassword", 110, "grindelwald4lyfe@gmail.com", "32435465")
    user_queries.persist_user("Tony", "Soprano", "juniorsucks", 50, "soprano@gmail.com", "82282882")

    #Successful login
    user_queries.user_login("grindelwald4lyfe@gmail.com", "supersecretPassword")

    #Unsuccessful login, currently throws exception if email doesnt exist, fix this later
    user_queries.user_login("grindelwald4lyfe@gmail.com", "notsecret")

    #Deletes user by email
    user_queries.delete_user("grindelwald4lyfe@gmail.com")

    #Updates users phonenumber, by their email
    user_queries.update_user("soprano@gmail.com", "32984234")


run_setup()