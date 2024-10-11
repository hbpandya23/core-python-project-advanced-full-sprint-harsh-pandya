import usrInput
import parseFile

#function to start the processsing of the employees.
def startProcess(tup):
    #tup = tuple we got from the checkPath function.
    count_files = 0                 #counting # of files that are being processed.
    count_emp = 0                   #counting number of employees that are being processed.

    #function that is iterating through the tuple received as an 
    # argument. And then calling several functions to process tup.
    for t in tup:
        list_first = parseFile.getJSONContent(t)
        list_second = parseFile.processEachEmp(list_first)
        count_emp += len(list_second)
        parseFile.generateFormattedFile(list_second,t)
        count_files += 1

    #printing out files and employees processed.    
    printOutput(count_files,count_emp)    
    return None

#checing and handlling of errors, if the path is correct or not/if
# there are .json/.pdf files in the path provided.
def errorHandle(checkReturn):
    if (checkReturn == 1):        # check of the reutn was int or not. if int, we will exit the script
        print("Provided Path is not valid, Exiting script!")
    else:                         # checking if returned tup is empty or not.
        count_len = len(checkReturn)   
        if (count_len != 0):      # if not empty we will call and startprocess function. 
            startProcess(checkReturn)
        else:                     # if empty, we will exit the script.
            print("No files found in provided path, Exiting script!")
            print("Hello")
    return None

#printing final output, howmany files and emp processed.
def printOutput(numFiles, numEmps):

    print(f"""
            ============================================================
            ---------------------Processing Summary---------------------
            ============================================================
                            Number of files processed:   {numFiles}
                            Number of employee entries
                            formatted and calculated:   {numEmps}
          """)

    return None

#this is the main function. Starting point of the
def main():
    str_path = usrInput.getUsrInput("Please enter a value: ")
    result = usrInput.checkPath(r'%s' % str_path, [])
    errorHandle(result)
main()


