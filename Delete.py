import os

if os.path.exists("C:\\Users\\birba\\OneDrive\\Desktop\\Python_DSA\\FileHandling\writess.txt"):
    os.remove("C:\\Users\\birba\\OneDrive\\Desktop\\Python_DSA\\FileHandling\writess.txt")
    print("File deleted successfully")
    
else:
    print("File not found")
    
