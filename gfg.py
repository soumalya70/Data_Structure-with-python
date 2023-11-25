def days_to_redeem_hoodie():
    daily_coins = 1  # Daily coin reward
    bonus_coins_every = 8  # Bonus coins every 8 problems
    bonus_coin_reward = 8  # Bonus coin reward
    hoodie_cost = 200 # Hoodie cost
    total_coins = 0  # Initialize total coins earned
    days = 0  # Initialize the number of days

    while total_coins < hoodie_cost:
        total_coins += daily_coins  # Earn a daily coin
        days += 1

        if days % bonus_coins_every == 0:
            total_coins += bonus_coin_reward  # Earn bonus coins every 8 days

    return days

days_needed = days_to_redeem_hoodie()
print(f"You need {days_needed} days to redeem the hoodie.")
