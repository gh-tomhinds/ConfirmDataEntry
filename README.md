## Intro

This project contains SIKULI code to automate some regression test plans.

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

This file first resets preferences to their default, then sets several preferences to values that help speed data entry.

### createCategories

### createCustomFields

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

