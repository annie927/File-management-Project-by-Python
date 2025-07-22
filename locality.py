import csv

def search_by_locality():
    file_path = r"C:\Users\kaznq\OneDrive\Desktop\Project\flats.txt"
    search_locality = input("Enter the locality to search for: ").strip().lower()

    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip header
            found = False
            print(f"\nFlats in '{search_locality.title()}':\n")
            for row in reader:
                if len(row) > 1 and row[1].strip().lower() == search_locality:
                    print(row)
                    found = True

            if not found:
                print("No flats found in that locality.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)


