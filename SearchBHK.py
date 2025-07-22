import csv
import pandas as pd

def search_flats_by_bhk():
    min_bhk = int(input("Enter required BHK you're looking for: "))

    with open(r"C:\Users\kaznq\OneDrive\Desktop\Project\flats.txt", 'r') as txt_file:
        reader = csv.DictReader(txt_file)
        flats = list(reader)

    print(f"\nFlats with {min_bhk} BHK:\n")
    found = False

    for flat in flats:
        try:
            if int(flat['bhk']) == min_bhk and flat['Availability'].lower() == 'yes':
                print(f"{flat['locality']} | {flat['bhk']} BHK | ₹{flat['price_per_sqft']}")
                found = True
        except:
            continue 

    if not found:
        print(f"No flats found with BHK greater than {min_bhk} and available.")


