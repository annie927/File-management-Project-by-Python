import pandas as pd

def remove_flat_by_index():
    file_path = r"C:\Users\kaznq\OneDrive\Desktop\Project\flats.txt" # Ensure this is in the same folder as your script

    try:
        # Read the data
        df = pd.read_csv(file_path)

        # Show the table with 1-based indexing
        df.index = df.index + 1
        print("\nAvailable Flats:\n")
        print(df)

        # Get user input
        idx = int(input("\nEnter index of flat to remove (1-based): "))

        if 1 <= idx <= len(df):
            df = df.drop(index=idx)
            df.index = df.index - 1  # Reset index before saving
            df.to_csv(file_path, index=False)
            print("\n✅ Flat removed successfully.\n")
        else:
            print("❌ Invalid index.")
    except FileNotFoundError:
        print("❌ File not found. Make sure 'flats.txt' exists.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

