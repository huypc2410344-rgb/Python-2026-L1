color_list = ["Blue","Yellow","Black","Red","While"]
fav_color = input("What is your favorite color? ")

if fav_color in color_list:
    index = color_list.index(fav_color)
    print(f"your color is at index {index} in my list")
else:
    print("Sorry, I could not find your color")