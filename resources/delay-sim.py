def interp_step(b0: float, b1: float, t: int, t_cool: int):
    return b0 * (1 - t / t_cool) + b1 * t / t_cool

MAX_STEPS = 100
COOLDOWN = 60 * 5
INTERP_INTERVAL = 15

b0 = 1.0
b1 = 2.0

b = b0

for i in range(0, MAX_STEPS):
    t = i * INTERP_INTERVAL
    print(f"b={b}, {t} seconds elapsed.")
    b = interp_step(b, b1, INTERP_INTERVAL, COOLDOWN)
