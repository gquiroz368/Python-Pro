import random
result_coin = ''
def flip_coin():
    global result_coin
    flip = random.randint(0, 1)
    if flip == 0:
        result_coin = "HEADS"
    else:
        result_coin = "TAILS"
    return result_coin

def gen_emodji():
    emodji = ["😁", "😐", "👍", "👎"]
    return random.choice(emodji)
