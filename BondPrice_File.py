import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    coupon = face * couponRate / ppy
    rate = y / ppy
    periods = int(m * ppy)

    t = np.arange(1, periods + 1)
    cash_flows = np.full(periods, coupon, dtype=float)
    cash_flows[-1] += face

    pv = cash_flows / (1 + rate) ** t
    price = np.sum(pv)

    return price
