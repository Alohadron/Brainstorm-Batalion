# name = ['Galina', 'Marina', 'Sasha', 'Alexa']

# try:
#     index = int(input('get name by index: '))
#     print(f'name by index {index} is: {name[index]}')
#     #name is a list
#     #print(name) should print all of the names
#     #if we need to print only one exact name then ->
#     #name[index]
#     #print(name[index])
# except IndexError:
#     '''Array out of bound exception'''
#     print('u cannot get name by index: {}'.format(index))#.format(index)
#     #is alternative to (f'...: {index}')
# else:
#     #runs only if block ran without errors
#     print('Succesfully find by index')

def process_data(file_name):
    """ 
    Simulates reading data from a file and demonstrates 
    the use of try-except-finally blocks.
    """
    print(f'\n--- Attempting to process: {file_name} ---')

    try:
        with open(file_name, 'r') as file:
            data = file.read()
        #simulate potential issues
        if file_name == "bad_file":
            raise ValueError("Data corruption detected!")
        if file_name == "missing":
            raise FileNotFoundError("The requested file does not exist")
        #simulate succesful operation
        print("Success: Data has been proccessed successfully.")
    except FileNotFoundError as e: #"as e" means as file, aka with open (name) as file
        #handle specific case when the file not found
        print(f'system error: {e}')
    except ValueError as e:
        #handle specific case when the file is invalid
        print(f'Data error: {e}')
    except Exception as e:
        #handle any other unexpected errors
        print(f'an unexpected error occured: {e}')
    finally:
        #this block executes regardless of wether an exception occured or not
        #It is used for cleanup tasks like closing files or connections
        print("Fianlly block: Cleaning up resources and closing connections")
#list of files to test diffirent scenarios
files_to_test = ['data.txt', 'bad_file','missing']
for f in files_to_test:
    process_data(f)

with open("data.txt", "w") as file:
    file.write('hello\n')

process_data('data.txt')
process_data('banzai.txt')