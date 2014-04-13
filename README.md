## Intro

This project contains SIKULI code to automate some regression test plans.

##  Files

### tsMain

This file the main driver of this set of scripts.
<<<<<<< HEAD
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

### createClient.Create_Client

This file contains code to create one client. 
Initially, it's called with values to create the first client in the database. 
Then it's called to by each billing arrangement script to create a new client for that specific billing arrangement. 

### createTask

### createExpense

### importTimekeepers

### editTimekeeper

### importClients

### editClient

### importTasks

### editTask

### importExpenses

### editExpense

### createRefs

### importRefs

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
=======
>>>>>>> ffb8282f9477356627a805891f3230ad7bcd6de8

