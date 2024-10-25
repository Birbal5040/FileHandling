try:
    with open("C:\\Users\\birba\\OneDrive\\Desktop\\Python_DSA\\FileHandling\write.txt") as f1:
        with open("C:\\Users\\birba\\OneDrive\\Desktop\\Python_DSA\\FileHandling\A.txt","w") as f2:
            for i in f1:
                f2.write(i)
    

except:
    print("File not found, please create first.")

else:
    f1.close()
    print("File closed successfully")