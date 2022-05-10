Inc_power = 60
Inc_lifespan = 1000
Inc_price = 5
low_power = 11
low_lifespan = 8000
low_price = 60

input = input().split(" ")
h = int(input[0])
p = int(input[1]) 

life = 0
Inc_cost = 0
low_cost = 0

i = 1
while i > 0:
    life += h
    Inc_cost += (Inc_power*h*p)/100000
    low_cost += (low_power*h*p)/100000
    if life%Inc_lifespan != 0:
        Inc_bulb_cost = ((life//Inc_lifespan)+1)*Inc_price
        low_bulb_cost = ((life//low_lifespan)+1)*low_price
    else:
        Inc_bulb_cost = ((life//Inc_lifespan))*Inc_price
        if life%low_lifespan == 0:
            low_bulb_cost = ((life//low_lifespan))*low_price
        else:
            low_bulb_cost = ((life//low_lifespan)+1)*low_price
    if (low_cost + low_bulb_cost < Inc_bulb_cost + Inc_cost):
        print(i)
        break
    i += 1