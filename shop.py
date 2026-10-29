def price_after_discount(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("invalid percent")
    return round(price * (1 - percent / 100), 2)
