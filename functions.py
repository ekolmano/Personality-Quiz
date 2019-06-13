"""A collection of functions for doing my project"""

def questions_and_answers():
    """ 
    Display questions and options. Get user response
    inspired by https://codereview.stackexchange.com/questions/153495/simple-multiple-choice-quiz
    """

    questions = ["What's your favorite color?",
                 "What's your favorite animal?",
                 "How do you spend your weekends?",
                 "What's the best stress food?",
                 "What's your favorite drink?",
                 "Which superpower would you want?",
                 "What one word would your friends use to describe you?",
                 "Where would you go for vacation?"]

    response_choices = ["a. green\nb. blue\nc. crimson\nd. gray\n",
                        "a. acaconda\nb. fish\nc. cat\nd. turtle\n",
                        "a. thrifting with friends\nb. running errands\nc. camping\nd. napping\n",
                        "a. cup noodles\nb. salad\nc. chocolate\nd. oatmeal\n",
                        "a. bang\nb. black coffee\nc. coca-cola\nd. water\n",
                        "a. super speed\nb. flight\nc. clairvoyance\nd. invisibility\n",
                        "a. honest\nb. reliable\nc. clever\nd. old school\n",
                        "a. backpack through Asia\nb. what's that?\nc. Europe\nd. stay-cation\n"]
    
    response_list = []
    
    for question, response in zip(questions, response_choices):
        
        print(question)
        print("Please, make your choice and hit ENTER.")
        print(response)

        user_response = ''
        while user_response not in ['a', 'b', 'c', 'd']:
            user_response = input("You can respond 'a', 'b', 'c' or 'd'.\n").lower()

        response_list.append(user_response)
        
    return response_list



def increase_counter(my_list):
    """function to add counters ie if response == letter: letter_total += 1"""
    
    a_total = 0
    b_total = 0
    c_total = 0
    d_total = 0
    
    for user_response in response_list:
        
        if user_response == "a":
            a_total += 1
            
        elif user_response == "b":
            b_total += 1
            
        elif user_response == "c":
            c_total += 1
            
        elif user_response == "d":
            d_total += 1
            
    counter_list = [a_total, b_total, c_total, d_total]
    
    return counter_list


def find_max(my_list):
    """find max value of the input list and return"""
    
    list_max = 0
    
    for num in my_list:
    
        if num > list_max:
            list_max = num
        
        else:
             continue
            
    return list_max


def quiz():
    
    """Main function to run quiz"""
    
    # Display questions and options. Get user response
    response_list = questions_and_answers()
   
    # Increase counters accourding to user response
    counter_list = increase_counter(response_list)
    
    # Check list of counters and find the most commonly chosen answer
    list_max = find_max(counter_list)
    
    # Determine result corresponding to chosen answers
    if counter_list[0] == list_max:
        outcome = "Python"
    
    elif counter_list[1] == list_max:
        outcome = "Java"
    
    elif counter_list[2] == list_max:
        outcome = "C++"
    
    elif counter_list[3] == list_max:
        outcome = "Perl"
    
    return outcome