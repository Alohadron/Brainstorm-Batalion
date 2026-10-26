# name = ["Galina", "Marina", "Sasha", "Alexa"]

# try:
#     index = int(input("Get name by index: "))
#     print(f"Name by index {index} is: {name[index]}")
# except IndexError:
#     print("You can not get name by this index: {}".format(index))
# else:
#     print("Successfully got name by index: ")


def process_data(file_name):
    """
    Simulates reading data from a file and demonstrates
    the use of try-except-finally blocks
    """

    print(f"\n--- Attempting to process: {file_name} ---")

    try:
        if file_name == "bad_file.":
            raise ValueError("Data corruption detected!")
        if file_name == "missing":
            raise FileNotFoundError("The requested file does not exist.")

        print(f"Successfully processed")

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except ValueError as e:
        print(f"DataError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print(">>>Finally block: Cleaning up resources and closing connections.")

files_to_test = ["data.txt", "bad_file", "missing"]

for f in files_to_test:
    process_data(f)