import random
import uuid


def get_entry(a_list):
    index = random.randint(0, len(a_list) - 1)
    entry = a_list[index]
    return entry


def return_grill_type():
    types_of_grills = [
        "Charcoal Grill",
        "Charcoal Kettle Grill",
        "Kamado Grill",
        "Pellet Grill",
        "Gas Grill",
    ]
    entry = get_entry(types_of_grills)
    return entry


def return_grill_name():
    list_of_grill_names = [
        "Eat Da Meat BBQ",
        "All Fired Up",
        "BBQ Junkies",
        "Rollin’ Smoke",
        "Oh My Grill!",
        "2nd Hand Smoke",
        "2 Men and a Pig",
        "Bull Rush BBQ",
        "Bushwhackers",
        "Come & Taste It",
        "Daddy Mac",
        "BBQ Down Range",
        "Getting Sauced",
        "Grill and Shout!",
        "The Meaties",
        "GoGrill!",
        "Wild BBQ",
        "Grill N’ Roll",
        "Lord of the BBQ",
        "The GrillFather",
        "Holy Smoke",
        "The Smokesman",
        "Broadgrill",
        "Grillmore’s",
        "Hogline",
        "Hog Hammer BBQ",
        "Meat Rushmore",
        "Gnaw Da Bone",
        "Roughnecks BBQ",
        "Salty Dawg BBQ",
        "Saucy Lil Porkers",
        "Meat Beaters BBQ",
        "Nicely Done BBQ",
        "Outlaw Hawgs BBQ",
        "Smoke In Your Eyes",
        "Smoker Bandits",
        "Smokin off the Grid",
        "The Grill Is Gone",
        "Tipsy Pigs",
        "Too Sauced",
        "Totally Sauced",
    ]

    entry = get_entry(list_of_grill_names)
    return entry


def return_brand_name():
    list_of_brand_names = [
        "Weber",
        "Char-Broil",
        "Traeger",
        "Dyna-Glo",
        "Nexgrill",
        "Masterbuilt",
        "Coleman",
        "Kenmore",
        "Char-Griller",
        "KitchenAid",
    ]
    entry = get_entry(list_of_brand_names)
    return entry


def return_amount_of_wheels():
    amount = random.randint(2, 4)
    return amount


def return_amount_of_burners():
    amount = random.randint(1, 5)
    return amount


def return_item_number():
    item_number = random.randint(100000, 999999)
    return item_number


def return_color():
    list_of_colors = [
        "Black",
        "Brown",
        "Orange",
        "Red",
        "Grey",
        "White",
        "Blue",
        "Green",
        "Pink",
        "Purple",
    ]
    entry = get_entry(list_of_colors)
    return entry


def return_product_id():
    product_id = str(uuid.uuid4())
    return product_id


def return_price():
    price = random.randint(2500, 34000)
    return price


def return_length_in_cm():
    length = random.randint(75, 150)
    return length


def return_width_in_cm():
    width = random.randint(75, 150)
    return width


def return_bread_basket():
    number = random.randint(1, 2)
    if number == 1:
        bread_basket = True
        return bread_basket
    bread_basket = False
    return bread_basket
