file = open('youtube.txt', 'w') # w is the mode of file means writable. this will overrite the file content

try:
    file.write('First writing project')
finally:
    file.close()

with open('youtube.txt', 'a') as file: # Here a means append mode. This will add the content with previous content
    file.write('Writing 2')