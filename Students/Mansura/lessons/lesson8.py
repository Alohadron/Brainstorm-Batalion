name = "Galina", "Marina", "Sasha", "Alexa"

try:
    index = int(input("Get name by index: "))
    print(f"Name by index {index} is: {name[index]}")
except IndexError:
    '''Array out of bound expectations '''
    print("You cannot get name by index: {}".format(index))
else:
    print("Successfully found by index")

def process_data(file_name):
    '''
    Simulates rerading data from a file and demonstrates the use of try-except-finally blocks
    '''
    print(f"\n-- Attempting to process: {file_name} --")

    try:
        if file_name == "bad_file":
            raise ValueError("Data corruption detected")
        if file_name == "missing":
            raise FileNotFoundError("The requested file doesnt exist")

        print("Success: Data has been processed successfully")
    #as e потому что делаем ошибку переменной для использ в принте в д случае
    except FileNotFoundError as e:
        #hand specific case when the file not found
        print(f"System Error: {e}")
    except ValueError as e:
        # handle specific case when data is invalid
        print(f"Data Error: {e}")
    except Exception as e:
        #handle any other unexpected errors
        print(f"An unexpecetd error occured: {e}")
    finally:
        #работает вне зависимости была ошибка или нет. исп для конца файла или соединения
        print(">>> Finally block: Cleaning up resouces and closing connection")


with open("data.txt", "w") as file:
    file.write("hfgfgfghgh\n")

process_data("data.txt")
process_data("banazai.txt")