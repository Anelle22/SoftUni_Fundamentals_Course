fee = int(input())

trainers = 0.6 * fee
clothes = 0.8 * trainers
ball = 0.25 * clothes
accessories = 0.2 * ball

total_cost = fee + trainers + clothes + ball + accessories

print(total_cost)