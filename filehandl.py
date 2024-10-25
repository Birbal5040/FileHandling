try:
    file=open("C:\\Users\\birba\\OneDrive\\Desktop\\Python_DSA\\FileHandling\write.txt","r")
    print(file.read())

except:
    print("File not found, please create first.")

else:
    file.close()
    print("File closed successfully")