import json
import re

"""
    getJSONContent(file)
	Arguments:
	file (str) – The path to the JSON file to get the content of.
	Return:
	list – The content of the file passed into the function. Should be a list of dictionaries, where each dictionary is the employee entry.
	Functionality: Read the JSON file that was passed in, to get the data in the file. 
"""
def getJSONContent(file):
    with open('%s' % file, 'r') as sfile:
        s = json.load(sfile)
        return s
    
"""
generateEmail(firstname, lastname)
•	Arguments:
o	firstname (str) – The employees first name.
o	lastname (str) – The employees last.
•	Return:
o	str – The company email in the format of <first letter of the first name><full last name>@comp.com all in lower case. For example, John Smith’s email would be jsmith@comp.com.
•	Functionality: Generate the email address for the employee entry to follow the format detailed above. 
"""    
def generateEmail(firstname, lastname):
    fletter = firstname[0].lower()
    lname = lastname.lower() 
    email = fletter + lname + "@comp.com"
    return email

"""
generateFormattedFile(empList, ogPath)
	Arguments:
	empList (list) – A list of dictionaries where each dictionary is the employee entry after being formatted as detailed in processEachEmp.
	ogPath (str) – The file path of the original file that was passed in.
	Return: None.
	Functionality: Save the content of the list to a new JSON file to the folder the original file was located and that has the original file name with “_formatted.json” appended at the end. 
"""
def generateFormattedFile(empList, ogPath):
    path_list = ogPath.split('/')
    for items in path_list:
        if '.json' in items:
            global filename
            filename = items.split('.')[0] + '_formatted.json'
    path_list.pop()
    new_path = ''
    for list_items in path_list:
        if(list_items == ''):
            new_path +='/'
        else:
            new_path += list_items + '/'
    print(new_path)          
    with open('%s%s' % (new_path, filename), 'w') as jfile:
        json.dump(empList, jfile, indent=4) 
    jfile.close()           
    return None

"""
validatePhoneNumber(phoneNumber)
	Arguments:
	phoneNumber (str) – The phone number of the employee. 
	Return:
	int – If the phone number is invalid, the number 1 to indicate an error. If the phone number is valid, the 10-digit number as an int. 
	Functionality – Check the given phone number to ensure it is a 10-digit number with no extra characters. 
"""
def validatePhoneNumber(phoneNumber):
    phone_pattern = re.compile(r'^\d{10}$')

    if phone_pattern.match(str(phoneNumber)):
        return phoneNumber
    else:
        return 1

"""
validateZips(zipCode)
	Arguments:
	zipCode (str) – The zip code of the employee. 
	Return:
	int – If the zip code is invalid, the number 1 to indicate an error. If the zip code is valid, the 5-digit number as an int. 
	Functionality – Check the given zip code to ensure it is a 5-digit number with no extra characters. 
"""
def validateZips(zipCode):
    zip_pattern = re.compile(r'^\d{5}$')

    if zip_pattern.match(str(zipCode)):
        return zipCode
    else:
        return 1    

"""
generateSalary(jobId, state)
	Arguments:
	jobId (str) – The job ID of the employee. The job ID could be IT_REP, IT_MNG, HR_REP, HR_MNG, SA_REP, or SA_MNG
	state (str) – The US state the employee is located in. 
	Return: 
	float – The calculated salary of the employee. 
	Functionality: Generate the salary of the employee based on the following criteria.
	Depending on the department, the employee has a given base salary:
	Sales - $60,000
	IT - $80,000
	HR - $70,000
	If the employee is a manager, the employee gets an extra 5% on top of the base salary.
	If the employee lives in the following states, they get an extra 1.5% on top of the base salary and their manager salary if they’re also a manager. 
	New York, California, Oregon, Washington, Vermont. 
"""
def generateSalary(jobId, state):

    salary = 0.0
    departments = {'SA':60000.00, 'IT':80000.00, 'HR':70000.00}
    inc_states = ['NY', 'CA', 'OR', 'WA', 'VT']
    for key in departments:
        if state in inc_states:
            if key in jobId:
                if 'MNG' in jobId:
                    salary += departments[key] + (departments[key] * 5 / 100) + (departments[key] * 1.5 / 100)
                else:
                    salary += departments[key] + (departments[key] * 1.5 / 100)
        else:
            if key in jobId:
                if 'MNG' in jobId:
                    salary += departments[key] + (departments[key] * 5 / 100)
                else:
                    salary += departments[key]            
    return salary

"""
processEachEmp(empList)
	Arguments:
	empList (list) – The list of employee entries extracted from the JSON or PDF file.
	Return:
	list – A list of dictionaries where each dictionary is each employee entry. 
	Functionality: Process each employee entry and format it based on the following criteria.	Ensure the phone numbers and zip codes are valid US phone numbers and zip codes. If they are invalid, skip the entry. If they are valid, save them to the dictionary as an int.
	Remove the last entry of the dictionary as that is extra data that’s not needed. 
	Ensure the first name, last name, address line 1 & 2, city, and job title have proper casing where the first letter of each word is capitalized, and all other letters are lower case. Also ensure there are no extra spaces. 
	Generate the company email and add to the dictionary. 
	Generate the salary and add to the dictionary. 
"""
def processEachEmp(empList):
    for each_pass in empList:
        lenth = len(each_pass) 
        count = 1
        Flag = False
        key_list = ['first name', 'last name', 'address line 1', 'address line 2','city', 'job title']
        for entry in list(each_pass):
            if entry.lower() in key_list:
                each_pass[entry] = each_pass[entry].strip()
                split_list = each_pass[entry].split(" ")
                print(split_list)
                val1 = ""
                for val in split_list:
                    pat = re.compile('^[A-Za-z]+$')
                    if pat.match(val):
                         val = val[0].upper() + val[1:].lower()
                    if (val1 == ""):        
                        val1 += val
                    else:
                        val1 += " " + val    
                each_pass[entry] = val1    
            if 'phone' in entry.lower():
                each_pass[entry] = each_pass[entry].strip()
                if validatePhoneNumber(each_pass[entry]) != 1:
                    each_pass[entry] = int(each_pass[entry])
                else:
                    each_pass[entry] = 1    
            if 'zip' in entry.lower():
                each_pass[entry] = each_pass[entry].strip()
                if validateZips(each_pass[entry]) != 1:
                    each_pass[entry] = int(each_pass[entry])
                else:
                    each_pass[entry] = 1
            if count == lenth:
                each_pass.pop(entry)
                #global ind_name
                #ind_name = entry
            each_pass["Company Email"] = generateEmail(each_pass["First Name"], each_pass["Last Name"])
            each_pass["Salary"] = generateSalary(each_pass["Job ID"], each_pass["State"])    
            count += 1                              
    return empList

#End of Script.
