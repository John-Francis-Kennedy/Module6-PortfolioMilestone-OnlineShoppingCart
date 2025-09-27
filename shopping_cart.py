
from dataclasses import dataclass, field
from typing import List

@dataclass
class ItemToPurchase:
    item_name: str = "none"
    item_price: int = 0
    item_quantity: int = 0
    item_description: str = "none"

    def print_item_cost(self) -> str:
        subtotal = self.item_price * self.item_quantity
        return f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${subtotal}"

    def print_item_description(self) -> str:
        return f"{self.item_name}: {self.item_description}"


@dataclass
class ShoppingCart:
    customer_name: str = "none"
    current_date: str = "January 1, 2020"
    cart_items: List[ItemToPurchase] = field(default_factory=list)

    def add_item(self, item: ItemToPurchase) -> None:
        self.cart_items.append(item)

    def remove_item(self, item_name: str) -> None:
        for i, it in enumerate(self.cart_items):
            if it.item_name == item_name:
                del self.cart_items[i]
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item: ItemToPurchase) -> None:
        for it in self.cart_items:
            if it.item_name == item.item_name:
                # Only apply changes if non-default
                if item.item_description != "none":
                    it.item_description = item.item_description
                if item.item_price != 0:
                    it.item_price = item.item_price
                if item.item_quantity != 0:
                    it.item_quantity = item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self) -> int:
        return sum(it.item_quantity for it in self.cart_items)

    def get_cost_of_cart(self) -> int:
        return sum(it.item_price * it.item_quantity for it in self.cart_items)

    def print_total(self) -> None:
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        total_items = self.get_num_items_in_cart()
        print(f"Number of Items: {total_items}")
        if total_items == 0:
            print("SHOPPING CART IS EMPTY")
            print("Total: $0")
            return
        for it in self.cart_items:
            print(it.print_item_cost())
        print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self) -> None:
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for it in self.cart_items:
            print(it.print_item_description())


def print_menu(cart: ShoppingCart) -> None:
    menu = (
        "MENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit"
    )
    choice = ""
    while choice != "q":
        print()
        print(menu)
        choice = input("Choose an option:\n").strip().lower()

        if choice == "q":
            break
        elif choice == "a":
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            desc = input("Enter the item description:\n")
            price = int(input("Enter the item price:\n"))
            qty = int(input("Enter the item quantity:\n"))
            cart.add_item(ItemToPurchase(name, price, qty, desc))
        elif choice == "r":
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)
        elif choice == "c":
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            qty = int(input("Enter the new quantity:\n"))
            # Only quantity changes here; others remain default so they won't overwrite
            cart.modify_item(ItemToPurchase(item_name=name, item_quantity=qty))
        elif choice == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()
        else:
            # Invalid input: loop continues and menu is shown again
            continue


def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


if __name__ == "__main__":
    main()
