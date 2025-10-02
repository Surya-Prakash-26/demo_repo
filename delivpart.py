delivery_partner="Swiggy"
restaurant="Dominos"

def food():
    item="pizza"

    def order_now():
        quantity=2
        print(f"ordering {quantity} {item} using {delivery_partner} from {restaurant}")
    order_now()
food()