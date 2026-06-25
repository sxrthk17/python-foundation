file_name = input("File name: ")

# gif = image/gif, jpg or jpeg = image/jpeg , no extension: application/octet-stream
# .txt text file and .zip Zip file

if file_name.lower().strip().endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
    print("image/jpeg")
elif file_name.endswith(".txt"):
    print("txt file")
elif file_name.endswith("zip file"):
    print("zip file")
else:
    print("application/octet-stream")
