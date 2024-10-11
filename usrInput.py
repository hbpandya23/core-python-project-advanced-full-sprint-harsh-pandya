import os.path
 
# checking if the path is valid or not.
# if valid then we will check all the files in dir if provided dir,
# skipping _formatted.json files and
# appending .json and .pdf files to dataFiles.
def checkPath(filePath, dataFiles):
    if not os.path.exists(filePath):
        print(1)#filePath + " does not exist.")
        return 1
    elif os.path.isdir(filePath):
        for file in os.listdir(filePath):
            checkPath(os.path.join(filePath, file), dataFiles)
    elif not filePath.endswith("_formatted.json") and filePath.endswith(".json") or filePath.endswith(".pdf"):
        dataFiles.append(filePath)
    return tuple(dataFiles)

# Getting input from the user for the path of the file.
def getUsrInput(msg):
    user_input = input(msg)
    return user_input
