# ==========================================
#        TRAFFICSENSE AI
#   Traffic Congestion Predictor
# ==========================================

from sklearn.tree import DecisionTreeClassifier

print("======================================")
print("       🚦 TRAFFICSENSE AI")
print("   Traffic Congestion Predictor")
print("======================================")

# ------------------------------------------
# TRAINING DATA
# ------------------------------------------
# Time:
# 0 = Morning
# 1 = Afternoon
# 2 = Evening
#
# Weather:
# 0 = Sunny
# 1 = Cloudy
# 2 = Rainy
#
# Holiday:
# 0 = No
# 1 = Yes
#
# Traffic:
# 0 = Low
# 1 = Medium
# 2 = High

X = [
    [0, 0, 900, 0],
    [0, 1, 800, 0],
    [0, 2, 950, 0],
    [1, 0, 300, 0],
    [1, 1, 450, 0],
    [1, 2, 500, 0],
    [2, 0, 1000, 0],
    [2, 1, 850, 0],
    [2, 2, 900, 0],

    [0, 0, 300, 1],
    [1, 0, 200, 1],
    [2, 0, 400, 1],

    [0, 0, 700, 0],
    [1, 0, 600, 0],
    [2, 0, 750, 0]
]

y = [
    2,
    2,
    2,
    0,
    0,
    1,
    2,
    2,
    2,

    0,
    0,
    0,

    1,
    1,
    1
]

# ------------------------------------------
# CREATE AI MODEL
# ------------------------------------------

model = DecisionTreeClassifier()

model.fit(X, y)

print("\nAI model trained successfully! ✅")


# ------------------------------------------
# USER INPUT
# ------------------------------------------

while True:

    print("\n--------------------------------------")
    print("Enter information about the traffic")
    print("--------------------------------------")

    print("\nTime of day:")
    print("1. Morning")
    print("2. Afternoon")
    print("3. Evening")

    time = input("Enter choice (1-3): ")

    if time == "1":
        time_value = 0
    elif time == "2":
        time_value = 1
    elif time == "3":
        time_value = 2
    else:
        print("❌ Invalid time choice.")
        continue

    print("\nWeather:")
    print("1. Sunny")
    print("2. Cloudy")
    print("3. Rainy")

    weather = input("Enter choice (1-3): ")

    if weather == "1":
        weather_value = 0
    elif weather == "2":
        weather_value = 1
    elif weather == "3":
        weather_value = 2
    else:
        print("❌ Invalid weather choice.")
        continue

    # --------------------------------------
    # NUMBER OF VEHICLES
    # --------------------------------------

    while True:

        vehicles_input = input(
            "\nEnter number of vehicles: "
        )

        try:
            vehicles = int(vehicles_input)

            if vehicles < 0:
                print("❌ Number cannot be negative.")
                continue

            break

        except ValueError:
            print("❌ Please enter a whole number.")
            print("Example: 750")

    # --------------------------------------
    # HOLIDAY
    # --------------------------------------

    print("\nIs today a holiday?")
    print("1. Yes")
    print("2. No")

    holiday = input("Enter choice (1-2): ")

    if holiday == "1":
        holiday_value = 1
    elif holiday == "2":
        holiday_value = 0
    else:
        print("❌ Invalid choice.")
        continue

    # --------------------------------------
    # AI PREDICTION
    # --------------------------------------

    prediction = model.predict([
        [
            time_value,
            weather_value,
            vehicles,
            holiday_value
        ]
    ])

    result = prediction[0]

    print("\n======================================")
    print("          🤖 AI RESULT")
    print("======================================")

    if result == 0:

        print("🟢 Predicted Traffic: LOW")

        print("\nAI Insight:")
        print(
            "Traffic is expected to be light."
        )

        print(
            "This may be a good time to travel."
        )

    elif result == 1:

        print("🟡 Predicted Traffic: MEDIUM")

        print("\nAI Insight:")
        print(
            "Moderate traffic is expected."
        )

        print(
            "You may experience some delays."
        )

    else:

        print("🔴 Predicted Traffic: HIGH")

        print("\nAI Insight:")
        print(
            "Heavy traffic is expected."
        )

        print(
            "Consider leaving earlier or "
            "choosing an alternative route."
        )

    # --------------------------------------
    # TRY AGAIN
    # --------------------------------------

    again = input(
        "\nDo you want another prediction? (y/n): "
    )

    if again.lower() != "y":
        print("\nThank you for using TrafficSense AI! 🚦")
        break

