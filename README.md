## Intro

This project contains SIKULI code to automate some regression test plans.

## Supporting Folders

### !data

Contains data files for various functions, such as:
* .csv files for importing names and slips
* .csv files for comparing bill arrangement values
* .tsl files to import bill layouts

### !reports

Stores reports for comparison
* there is a folder that holds baseline reports
* there are folders to store newly generated reports

##  Files

### tsMain

This file the main driver of this set of scripts.
* It sets up the logging system.
* It generates the starting time stamp
* It calls all scripts
* It generates the ending time stamp

### setupStuff

This file sets up many of the global variables used throughout the scripts

### closeTimeslips

This file used to include code to close Timeslips.
After a while that seemed silly. Now it simply reminds you to close Timeslips before continuing.

### delDataFolder

This file contains code to delete the folder containing the test data. It will be rebuilt.

### startTSandNewDB

This file contains code to create a new empty database.
* StartTS_CreateNewDB - Opens Timeslips and walks through the data creation process.
* checkFor_BillingDate - Closes the Revise Billing Date dialog
* checkFor_SPS - closes the SPS dialog
* checkFor_PEP - closes the PEP message
* checkFor_Sample - closes the Sample Database message

### tweakPrefs

This file first resets preferences to their default, then sets several preferences to values that help speed data entry. These changes are saved in a new preference file.

### createCategories

This file creates a set of categories for use with new tasks and expenses.

### createCustomFields

This file create one of each type of client custom fields.
* Create_CustomFields - opens the Custom fields dialog box and calls CreateOne for each type of custom field; then calls FillList
* CreateOne - Creates a specific custom field
* FillList - Fills the List type custom field with values

### createClient

This file contains code to create one client. 
Initially, it's called with values to create the first client in the database. 
Then it's called to by each billing arrangement script to create a new client for that specific billing arrangement. 

### createTask

This file contains code to create the initial task. 

### createExpense

This file contains code to create the initial expense. 

### importTimekeepers

This file contains code to open TSImport to import additional timekeepers from a file.
That data file is: Desktop\Sikuli\DataFiles\timekeepers.csv.

### editTimekeeper

This file contains code to edit the initial timekeeper that was created in startTSandNewDB.

### importClients

This file contains code to open TSImport to import additional timekeepers from a file.
That data file is: Desktop\Sikuli\DataFiles\towns.csv.
* Import_Clients - Opens TSImport, sets up the template, imports data
* Add_CustomField - Adds the custom fields to the template

### editClient

This file contains code to edit the initial client that was created in createClient, then also edit default rate and interest for all clients.
* EditClient - Drives the process
* Edit_CliGenInfo - edits values in the Contact Info page for initial client
* Edit_CliCustom - edits values in the Custom page for initial client
* Edit_CliRatesNotes - edits billing rates and notes for initial client
* Edit_DefaultRates - loops through all clients, editing default rate settings
* Edit_InterestSetting - edits interest setting and exports it to all other clients

### importTasks

This file contains code to open TSImport to import additional tasks from a file.
That data file is: Desktop\Sikuli\DataFiles\tasks.csv.

### editTask

This file contains code to edit the initial client that was created in createTask.

### importExpenses

This file contains code to open TSImport to import additional expenses from a file.
That data file is: Desktop\Sikuli\DataFiles\expenses.csv.

### editExpense

This file contains code to edit the initial client that was created in createExpense.

### createRefs

This file contains code that changes reference settings, exports them to all clients, then creates global references (from names in a data file) that are used by all clients.
That data file is: Desktop\Sikuli\DataFiles\templateRefs.csv.

### importRefs

This file contains code that sets up a TSImport template and imports client-specific references for each client.
That data file that is imported is: Desktop\Sikuli\DataFiles\refs.csv.

### setupFeeAlloc

### setupExpMarkups

### setupTaxes

### createSlips

### createPayments

### importBillLayout

### printBills

### baCommon

### reviewBillingArrangements

### setupCalTerms

### calendarStuff

### printClients

### printTasks

### printExpenses

### printTimekeepers

### compareReports

