# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# HChung,6.13.2020,Modified code to complete assignment 9
# HChung,6.13.2020,Fixed bugs and added error-handling
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Data
strFileName = "EmployeeData.txt"
lstTable = []

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
try:
    lstFileData = Fp.read_data_from_file(strFileName) # create and return list of object rows from file
    lstTable.clear() # Clear list before loading from file
    for line in lstFileData: # Convert list of string to Employee objects
        lstTable.append(Emp(line[0], line[1], line[2].strip())) # Build Employee object on same line as appending it to list

    while True: # while loop to return to menu of options
        # Show user a menu of options
        Eio.print_menu_items()

        # Get user's menu option choice
        strChoice = Eio.input_menu_options()
        if strChoice.strip() == '1':
            # Show user current data in the list of employee objects
            # for row in lstTable: # for testing purposes
            #     print(row.to_string(), type(row)) # for testing purposes
            Eio.print_current_list_items(lstTable)

        elif strChoice.strip() == '2':
            # Let user add data to the list of employee objects
            lstTable.append(Eio.input_employee_data())
            # for row in lstTable: # for testing purposes to show Employee data from refilled list
            #     print(row.to_string(), type(row)) # for testing purposes

        elif strChoice.strip() == '3':
        # let user save current data to file
            Fp.save_data_to_file(strFileName, lstTable)

        elif strChoice.strip() == '4':
        # Let user exit program
            input("Press the Enter Key to exit the Program. Goodbye!")
            break  # and Exit
        else:
            print("Please Enter 1, 2, 3, or 4!")

except FileNotFoundError as e:
    print("Text file " + strFileName + " must exist before running this script!")
    print(e, e.__doc__, type(e), sep='\n')
    input("Press Enter to Exit the Program")

except Exception as e:
    print("There was an error! Check file permissions.")
    print(e, e.__doc__, type(e), sep='\n')
    input("Press Enter to Exit the Program")

# Main Body of Script  ---------------------------------------------------- #