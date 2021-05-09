import art

auction_bid = {}

continue_auction = True

print(art.logo)
while continue_auction:
    name = input("What is your name? \n")
    bid = int(input("Enter your bid $\n"))
    auction_bid[name] = bid
    more_bidders = input("Are there more bidders type yes or no")
    if more_bidders == 'no':
        continue_auction = False

max_bidding_value = 0
max_bidder_name = ""
for bidder_name in auction_bid:
    if auction_bid[bidder_name] > max_bidding_value:
        max_bidding_value = auction_bid[bidder_name]
        max_bidder_name = bidder_name

print(f"Max bidder name is {bidder_name} and value is ${max_bidding_value}")
