# -*- coding: utf-8 -*-
"""
This program simulates a driver's license exam
1.28.24
CSC 221 - Dict Review
Laura K. Jackson
"""

def exam_questions():
    '''
    This function contains driver's exam questions, and returns that list (w/dictionaries)
    '''
    
    # driver's license exam questions
    exam = [{"question":"A learner's permit usually requires supervised driving.",
             "answer": False},
            {"question":"The legal age for obtaining a driver's license varies by state in\
             the US.", "answer":True},
            {"question":"A commercial driver's license (CDL) is required for\
             operating a large truck or bus.", "answer":True},
            {"question":"Renewal periods for driver's licenses can vary, but it's\
             typically more frequent than every 10 years.", "answer":False},
            {"question":"A red traffic light always indicates that you must stop",
             "answer":True},
            {"question":"Driving with headphones on in both ears is illegal in many\
             states.", "answer":False},
            {"question":"Driving under the influence (DUI) is a serious offense,\
             not a minor traffic violation.","answer":False},
            {"question":"A yellow diamond-shaped sign is a warning or caution sign"\
             ,"answer":True},
            {"question":"In most states, turning right on red is allowed after a \
             complete stop is there is no oncoming traffic.", "answer":True},
            {"question":"The speed limit on interstate highways is usually higher\
             than on local roads, but it can vary.", "answer":False}]
             
    return exam

def ask_questions():
    '''
    This function runs the actual exam, keeping track of points that user acquires
    and the exam questions are called here at the beginning of the function.
    '''
    
    # call function that has exam questions
    questions = exam_questions()
    
    # set user's score to 0 initially
    user_score = 0
        
    # use a for loop to iterate through questions
    # item references a dictionary
    for item in questions:
        print(item["question"])
        
        user_answer = input("True or False? Enter 1 for True, 2 for False. ")

        # decision structure to evaluate user's answer of 1 or 2 (boolean variables)
        if user_answer == "1":
            user_answer = True
            
        else:
            user_answer = False
        
        # correct answer 
        correct_answer = item["answer"]
        
        # decision structure to evaluate points earned based on user's answer
        if user_answer == correct_answer:
            print("Correct! You have earned 10 points.\n")
            user_score += 10
            
        else:
            print("Incorrect.\n")
            user_score == user_score
    
    # decision structure to evaluate whether user passed or failed exam
    if user_score >= 80:
        print(f'Score: {user_score}')
        print("You have passed the test. Congratulations!")
    
    else:
        print(f'Score: {user_score}')
        print("You did not pass. You must score an 80 or higher to pass.\nTry again.")
        
    