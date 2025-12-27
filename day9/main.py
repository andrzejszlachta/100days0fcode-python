import art

users = []

def add_user():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    next_user = input("Are there any other bidders? Type 'yes' or 'no': ")
    users.append({
        name: bid
    })
    if next_user == 'yes':
        print("\n" * 100)
        add_user()

def get_result():
    highest_bidder_name = ""
    highest_bid = 0
    for user in users:
        for key in user.keys():
            if user[key] > highest_bid:
                highest_bidder_name = key
                highest_bid = user[key]
    print(f"The winner is {highest_bidder_name} with bid of ${highest_bid}.")


print(art.logo)
print("Welcome to the secret auction program.")
add_user()
get_result()
