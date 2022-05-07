class User:
    def __init__(self, user_id, first_name, last_name, password, age, email, phone_number):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.age = age
        self.email = email
        self.phone_number = phone_number

    def return_user(self):
        return (
            self.user_id,
            self.first_name,
            self.last_name,
            self.password,
            self.age,
            self.email,
            self.phone_number
        )