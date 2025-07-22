import pandas as pd
from add_flat import add_flat
from price import search_price 
from Remove import remove_flat_by_index
from SearchBHK import search_flats_by_bhk
from locality import search_by_locality

while True:
    print('\n--- Menu ---\n')
    print('1. List of all flats')
    print('2. Search flat by locality')
    print('3. Search flat by price')
    print('4. Search flat by BHK')
    print('5. Add a new flat')
    print('6. Remove a flat')
    print('7. Exit')

    try:
        n = int(input('\nPlease select an option (1-7): '))
    except ValueError:
        print("Please enter a valid number.")
        continue

    match n:
        case 1:
            df = pd.read_csv(r"C:\Users\kaznq\OneDrive\Desktop\Project\flats.txt",header=0)
            df.index = range(1, len(df) + 1)
            print(df)
        case 2:
            search_by_locality()
        case 3:
            search_price()
        case 4:
            search_flats_by_bhk()
        case 5:
            add_flat()
        case 6:
            remove_flat_by_index()
        case 7:
            print("Exiting program...")
            break
