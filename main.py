from payment.payment_method import CreditCardPayment, UPIPayment
from payment.store import Store


def main():

    store = Store()

    while True:

        try:
            print("\nWelcome to Payment system:")
            print("Press 1 for Add cash")
            print("Press 2 to Refund")
            print("Press 3 to Check balance")
            print("Press 4 to Check transaction history")
            print("Press 5 to Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:

                print("Press 1 for Credit Card")
                print("Press 2 for UPI")

                method_choice = int(input("Enter payment method: "))
                amount = float(input("Enter amount: "))

                if method_choice == 1:
                    payment = CreditCardPayment()
                elif method_choice == 2:
                    payment = UPIPayment()
                else:
                    print("Invalid payment method")
                    continue

                store.add_cash(payment, amount)

            elif choice == 2:
                amount = float(input("Enter refund amount: "))
                store.refund(amount)

            elif choice == 3:
                store.show_balance()

            elif choice == 4:
                store.show_history()

            elif choice == 5:
                print("Exiting system. Thank you!")
                break

            else:
                print("Invalid choice.")

        except ValueError as ve:
            print("Error:", ve)

        except Exception as e:
            print("Unexpected error:", e)


if __name__ == "__main__":
    main()
