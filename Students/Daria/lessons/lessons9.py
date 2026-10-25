# name = ['Galina', 'Marina', 'Sasha', 'Alexa']
# try:
#     index = int(input('Get name by index'))
#     print(f'Name by index {index} is: {name[index]}')
# except IndexError:
#     '''Array out of bound exception'''
#     print('You cannot get name by index: {}'. formay(index))
# else: 
#     print('Successfully find by index')

def process_data(file_name):
    print(f"\n--- Attempting to process: {file_name}---")

    try:
        if file_name == "bad_file":
            raise ValueError("Data corruption detected!")
        if file_name == "missig":
            raise FileNotFoundError("The requested file does not exist. ")
        print("Success: Data has been processed successfully.")
    except FileNotFoundError as e:
        print(f"System Error: {e}")
    except ValueError as e:
        print(f"Data Error: {e}")
    except Exception as e: 
        print(f"An unexpected error occurred: {e}")
    finally:
        print(">>> Finally block: Cleaning uo resousrces and closing connection.")
    files_to_test = ["data.txt", "bad_file", "missing"]
    for f in files_to_test:
        process_data(f)
        