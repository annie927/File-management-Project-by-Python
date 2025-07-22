def add_flat():
    flat_id = input("Enter flat ID: ")
    locality = input("Enter locality: ")
    bhk = input("Enter BHK: ")
    price_per_sqft = input("Enter price per sqft: ")
    is_available = input("Is available? (yes/no): ")
    builder_name = input("Enter builder name: ")

    with open(r"C:\Users\kaznq\OneDrive\Desktop\Project\flats.txt", "a") as file:
        line = f"{flat_id},{locality},{bhk},{price_per_sqft},{is_available},{builder_name}\n"
        file.write(line)

    print("Flat added and saved to file!")

# ✅ This part is only for testing. It should NOT run when imported.
if __name__ == "__main__":
    while True:
        add_flat()
        cont = input("Add another flat? (yes/no): ")
        if cont.lower() != "yes":
            break
