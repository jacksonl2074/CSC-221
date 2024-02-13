# -*- coding: utf-8 -*-
"""
# Program uses dictionaries to access information a user can use to access
# information about different countries.
# 2.4.24
# CSC221 M1Pro– Review
# Laura K. Jackson
"""

def adictionary():
    '''
    This function contains a dictionary with different statistics for different
    countries.

    Returns
    -------
    allData : Dictionary with strings and floats

    '''
    

    allData = {
        'US': {'pop': 325.7, 'gdp': 19.39, 'ccy': 'USD', 'fx': 1.0},
        'CA': {'pop': 36.5, 'gdp': 1.65, 'ccy': 'CAD', 'fx': 1.35},
        'MX': {'pop': 129.2, 'gdp': 1.15, 'ccy': 'MXN', 'fx': 19.68}
    }

    return allData

def runProgram():              
    '''
    This function calls the dictionary from the previous function and then uses
    it to run the actual program.

    Returns
    -------
    None.

    '''
    # call dictionary function
    countryDict = adictionary()
    
    # user input
    code_country = input("country code: ").upper()
    
    # use while loop to control user input validation
    while code_country != "":
        
        # decision structure to see if user input matches what is in dict.
        if code_country in countryDict:
            user_measure = input("Please enter a statistic (pop, gdp, ccy, or fx): ").lower()
            
            # print(allData[code_country]) # prints inner dict
            
            # while loop to see if user input matches what is in dict.
            while user_measure not in countryDict[code_country]:
            
                print("Please enter a valid stat again.")
                user_measure = input("Please enter a statistic (pop, gdp, ccy, or fx): ").lower()
            
            # variable references the statistics in dict.
            stat = countryDict[code_country][user_measure]
            print(f'{code_country} {user_measure} = {stat}')
    
        else:
            print("Country code not found.")
            
        code_country = input("Please enter a country code: ").upper()
        

    print("Exiting...")
