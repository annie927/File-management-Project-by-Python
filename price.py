def search_price():
    try:
        with open(r"C:\Users\kaznq\OneDrive\Desktop\Project\flats.txt", 'r') as file:
            lines = file.readlines()

        flats = []
        for line in lines[1:]:  # skip header
            parts = line.strip().split(",")
            try:
                flat = {
                    "flat_id": int(parts[0]),
                    "locality": parts[1],
                    "bhk": int(parts[2]),
                    "price_per_sqft": int(parts[3]),
                    "is_available": parts[4].lower(),
                    "builder_name": parts[5]
                }
                flats.append(flat)
            except (IndexError, ValueError):
                print(f"Skipping invalid entry: {line.strip()}")

        user_price = int(input("Enter your budget: "))

        print("\nBudget matched! Here are your options:\n")
        found = False

        for flat in flats:
            if flat["price_per_sqft"] <= user_price and flat["is_available"] == "yes":
                print(f"{flat['locality']} | {flat['bhk']} BHK | ₹{flat['price_per_sqft']}")
                found = True

        if not found:
            print("No available flats under your budget.")

    except FileNotFoundError:
        print("flats.txt not found.")


