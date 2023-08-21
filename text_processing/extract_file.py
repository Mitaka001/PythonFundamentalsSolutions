path_to_file = input().split("\\")
filename, extension = path_to_file[-1].split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")
