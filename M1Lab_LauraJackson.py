# -*- coding: utf-8 -*-
"""
This program simulates a driver's license exam
1.28.24
CSC 221 - Dict Review
Laura K. Jackson
"""
import exam as e

# main function
def main():
    
    print("This program consists of 10 questions related to driving.\n")
    
    # call function from other file to run program
    e.ask_questions()
    
# calls main function
if __name__ == "__main__":
    main()