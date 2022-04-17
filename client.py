# --------------------------------------------------------------- #
""" Template for importing files """
try:
    import ___________
    print("File has been imported")
    print("File Type: ")
    print("File Name:")
    print("Folder Name:")
    print("---------")

except ImportError:
    print("Error: File failed to import")
    print("File Type:")
    print("File Name:")
    print("Folder Name:")
    print("---------")

""" File is supposed to return "Error: File failed to import" because the import file is a placeholder and doesn't 
exist. """
# --------------------------------------------------------------- #
try:
    import clientexe
    print("File has been imported")
    print("File Type: Python File (.py)")
    print("File Name: clientexe")
    print("Folder Name: Main Module")
    print("---------")


except ImportError:
    print("Error: File failed to import")
    print("File Type: Python File (.py) ")
    print("File Name: clientexe")
    print("Folder Name: Main Module ")
    print("---------")
