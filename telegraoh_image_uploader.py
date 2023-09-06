from html_telegraph_poster import upload_image
path = input("enter image path: ")
link = upload_image(rf'{path}')
print(link)