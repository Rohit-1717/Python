file = open("youtube.txt", "w")

try:
    file.write("Rohit or code")
finally:
    file.close()


with open('youtube.txt','w') as file:
    file.write('Rohit or Code')
    