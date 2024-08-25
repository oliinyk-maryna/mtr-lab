def print_utility_table():
    print("Корисність результатів:")
    print("------------------------")
    print("| Дуже добре  | 10 |")
    print("| Добре       |  8 |")
    print("| Посередньо  |  6 |")
    print("| Погано      |  3 |")
    print("| Дуже погано |  1 |")
    print("------------------------\n")

def calculate_utility(rain_prob, rain_utility, sun_utility):
    sun_prob = 1 - rain_prob
    utility = (rain_prob * rain_utility + sun_prob * sun_utility)
    
    return utility

def main():
    print_utility_table()

    rain_prob = float(input("Введіть ймовірність дощу (0 to 1): "))
    
    home_rain_utility = float(input("Введіть оцінку відчуттів залишитись вдома, коли йде дощ: "))
    home_sun_utility = float(input("Введіть оцінку відчуттів залишитись вдома, коли сонячно: "))

    forest_rain_utility = float(input("Введіть оцінку відчуттів піти в ліс, коли йде дощ: "))
    forest_sun_utility = float(input("Введіть оцінку відчуттів піти в ліс, коли сонячно: "))

    utility_home = calculate_utility(rain_prob, home_rain_utility, home_sun_utility)
    utility_forest = calculate_utility(rain_prob, forest_rain_utility, forest_sun_utility)

    print(f"\nОчікувана кориснаість залишитись вдома: {utility_home:.2f}")
    print(f"Очікувана кориснаість піти до лісу: {utility_forest:.2f}")

    if utility_forest > utility_home:
        print("\nGo to the forest.")
    else:
        print("\nStay at home =).")

if __name__ == "__main__":
    main()