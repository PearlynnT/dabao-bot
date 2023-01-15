def get_init_text(canteen):
    intro = "You've requested to create a new poll.\nCanteen: "
    instructions = "\nPlease follow these steps:\n1. Select the canteen where you would like to dabao from.\n2. Send me the name of this poll."
    return intro + canteen + instructions

def get_stalls_text(canteen):
    if canteen == "Flavours @ UTown (Foodclique)":
        stalls = "\t\tJapanese\n\t\tTaiwanese\n\t\tNoodles\n\t\tChicken Rice\n\t\tMini Wok\n\t\tTenderbreast\n"
        #stalls = ["Japanese", "Taiwanese", "Noodles", "Chicken Rice", "Mini Wok", "Tenderbreast"]
    return stalls

def get_fcjap_text():
    menu = "Japanese\n1. Tenzaru Soba\n2. Salmon Mentai Don\n3. Unadon\n4. Ebi Fried Don\n5. Tori/Kitsune Udon\n6. Chicken Teriyaki Don\n7. Shabu Shabu Seafood Set\n8. Shabu Shabu Chicken Set"
    return menu

def get_fctai_text():
    menu = "Taiwanese\n1. Shrimp Fried Rice w Fish Roe\n2. Pork Chop Fried Rice w Fish Roe\n3. Braised Beef Rice\n4. Pork Chop Rice\n5. Chicken Chop Rice\n6. Braised Pork Rice\n7. Mushroom Noodle (Dry)\n8. Braised Pork Noodle (Dry)\n9. Vinegar Beef Noodle (Dry)"
    return menu

def get_fcjap_order_text(order):
    ordered = "\t\tJapanese\n\t\t{}\n\t\tTaiwanese\n\t\tNoodles\n\t\tChicken Rice\n\t\tMini Wok\n\t\tTenderbreast\n".format(order)
    return ordered