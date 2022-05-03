# EXAMPLE UI 

import time

while True: 
    # 1 to generate new image or 2 to exit 
    value = input("Please enter 'tweet' to tweet: ")
    if value == "tweet": 
        file = open("signal.txt", "w") 
        content = "This is my finances for the week 1 dollars"
        file.write(f"tweet| {content}")  # call it like tweet| whatever you want to tweet about 
        file.close()
        time.sleep(5)



        

        
