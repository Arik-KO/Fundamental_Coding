import os

#os.getcwd() -> get location of the current folder
#os.chdir(address) -> like cd in the terminal
current_location = os.getcwd()
print(current_location)


os.mkdir('created_using_os')
# for nested folder creation
# os.makedirs('logs/2024/mars')


files = os.listdir('.')
print(files)

#for joining paths os.path.join()
print(os.path.exists('Readme.md'))
print(os.path.isfile("Readme.md"))
print(os.path.isdir('python_codes'))
