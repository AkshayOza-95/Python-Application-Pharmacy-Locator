# Local Healthcare Costs tool
## Abstract:
A python application that enables the user to quickly search for the lowest cost drug prices and compare hospitals in the Pittsburgh region based on charge data. The drug tool is a dynamic search. The hospital charge tool returns comparisons based on CMS/Medicare data 2014-2017 across 12 condition categories and 19 area hospitals.

## Description:
● There are two functions:

o Drug tool:

▪ Input address and drug name and the tool returns the lowest cost generic and/or brand name drug and details on the pharmacy provider in the chosen area (mile radius).

o Hospital charge tool:

▪ Search by condition category and compare all hospitals, or

▪ Compare two hospitals across all categories

● The tool returns a comparison using average levels of overcharge (i.e., the average % difference in Hospital Charges and Actual Total Payments), and

● Average levels of % uncovered (i.e., the average remaining share of Total Payments left to the patient after Medicare Payment)

## Prerequisites:

● To run from base code, the program requires Python with installed packages including:

o selenium

o common packages including bs4, pandas, seaborn and matplotlib

● For Selenium along with installing the selenium library; you will have to install chromedriver.exe for your OS and change the executable path for the driver that you set up. For example:


● For the hospital charge portion of the tool, data has been collected and prepared. The main() program will function by drawing on prepared csv files including:

o ‘hospitals.csv’
o ‘PA hospital scores.csv’

## User guide:

### Running the program:

● After ensuring the prerequisites are in place and the appropriate data files are in the correct path, the main program can be executed.

● Note that the drug search tool is dynamic and will require more time to return output on searches.

● Program sequence: First user prompt:

o 1. Search drugs prices

o 2. Search hospital charges

o 0. Quit

● Option 1: Drug tool

o Prompt:

▪ 1. To see data a drug

▪ 0: To Quit

o Select 1 and enter drug name, home address, distance within address (miles)

o Tool returns chosen drug, generic and brand name, with lowest cost and pharmacy details

o User may continue drug searches or return to menu

● Option 2: Hospital charge data

o User prompt:

▪ 1. Find hospital by illness category

▪ 2. Compare two hospitals across categories

▪ 0. Quit

o Select 1 and choose the desired condition category:

o Tool returns comparison of regional hospitals and their “overcharge” and “uncovered” average values

▪ Overcharge %: (Total charges - Actual total payment) / Total charges

▪ Uncovered %: (Actual total payments - Medicare payments) / Actual total payments

o or Select 2 and choose two hospitals from the list to compare:

o Tool returns comparison of two regional hospitals and their “overcharge” and “uncovered” average values across all condition categories

o Tool also returns data table and visualization

o Users may continue hospital charge searches or return to the main menu.

● Option 0: stop program
