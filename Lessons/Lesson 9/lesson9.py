# name = ["Galina", "Marina", "Sasha", "Alexa"]


# try:
#     index = int(input("Get name by index: "))
#     print(f'Name by index {index} is: {name[index]}')
# except IndexError:
#     print("You can not get name by this index: {}".format(index))
# else:
#     print("Successfully got name by index: ")

def process_data(file_name):
    """
    Simulates reading data from a file and demostrates
    the use of try-except-finally blocks.
    """
    print(f"\n--- Attempting to precess: {file_name} ---")

    try:
        with open(file_name, "r") as file:
            data = file.read()

        if not data:
            raise ValueError("Data is empty or invalid.")

        # Simulate successful operation
        print("Success: Data has been processed succesfully!")

    except FileNotFoundError as e:
        # Handle specific case when the file is not found
        print(f"System Error: {e}")
    except ValueError as e:
        # Handel specific case whent data is invalid
        print(f"DAta Error: {e}")
    except Exception as e:
        # Hanlde any other unexpceted errors
        print(f"An unexpected error occured: {e}")
    finally:
        print(">>>Finally block: Cleaning up resources and closing connection.")

with open("data.txt", "w") as file:
    file.write("abracadabra\n") 

process_data(1)  


