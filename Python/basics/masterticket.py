TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100

def calculate_price(num_of_tickets):
    return (num_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while (tickets_remaining > 0):
    print("Hello, welcome to Master Ticket")
    print("There are {} tickets remaining".format(tickets_remaining))
    users_name = input("Please enter your name: ")
    tickets_wanted = input("Hi {}, How many tickets would you like to purchase? ".format(users_name))
    try:
        tickets_wanted = int(tickets_wanted)
        if (tickets_wanted > tickets_remaining):
            raise ValueError("{} tickets is not available, there are only {} tickets available".format(tickets_wanted, tickets_remaining))
    except ValueError as err:
        print("Oops you entered an invalid value, try again...")
        print("({})".format(err))
    else:
        total_cost_of_tickets = calculate_price(tickets_wanted)
        print("The amount you have to pay, for {} tickets is £{}".format(tickets_wanted, total_cost_of_tickets))
        proceed = input("Do you want to proceed with your order, Yes/No: ")
        if proceed.lower() == "yes":
            # TODO: Gather credit card information and process it
            print("SOLD!! to {} for £{}".format(users_name, total_cost_of_tickets))
            tickets_remaining -= tickets_wanted
        else:
            print("Thank you for visiting Master Ticket, hopefully we see again {}".format(users_name))
if (tickets_remaining == 0):
    print("Unfortunately all tickets are now sold out")
