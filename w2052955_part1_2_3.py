# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID: w2052955 / 20221794
# Date: 13/12/2023


# Importing the graphics module to create the histogram
import graphics

# Creating a function to make and display the histogram according to the counts
def histogram(counts):
    # Getting counts for different outcomes
    count1 = counts[0]
    count2 = counts[1]
    count3 = counts[2]
    count4 = counts[3]

    # Creating the graphics window
    x = graphics.GraphWin("Histogram",625,580) 
    heading = graphics.Text(graphics.Point(130,70),"Histogram results")
    heading.setSize(17)
    heading.draw(x)

    ##### Drawing rectangles for the each outcome #####
    ##### Creating the counts of the each outcome #####
    ##### Creating the labels for the each outcome #####
    progress_rectangle = graphics.Rectangle(graphics.Point(160,490 - count1 *8),graphics.Point(50,500))
    graphics.Text(graphics.Point(105,470 - count1 *8),count1).draw(x)
    r1 = graphics.Text(graphics.Point(104,510),"Progress")
    progress_rectangle.setFill("palegreen2")
    progress_rectangle.draw(x)
    r1.draw(x)

    trailer_rectangle = graphics.Rectangle(graphics.Point(300,490 - count2 * 8),graphics.Point(190,500))
    graphics.Text(graphics.Point(245,470 - count2 * 8),count2).draw(x)
    r2 = graphics.Text(graphics.Point(242,510),"Trailer")
    trailer_rectangle.setFill("darkseagreen")
    trailer_rectangle.draw(x)
    r2.draw(x)

    retriever_rectangle = graphics.Rectangle(graphics.Point(440,490 - count3 * 8),graphics.Point(330,500))
    graphics.Text(graphics.Point(385,470 - count3 * 8),count3).draw(x)
    r3 = graphics.Text(graphics.Point(385,510),"Retriever")
    retriever_rectangle.setFill("darkolivegreen3")
    retriever_rectangle.draw(x)
    r3.draw(x)

    exclude_rectangle = graphics.Rectangle(graphics.Point(580,490 - count4 * 8),graphics.Point(470,500))
    graphics.Text(graphics.Point(520,470 - count4 * 8),count4).draw(x)
    r4 = graphics.Text(graphics.Point(525,510),"Excluded")
    exclude_rectangle.setFill("mistyrose3")
    exclude_rectangle.draw(x)
    r4.draw(x)

    graphics.Line(graphics.Point(590,500),graphics.Point(40,500)).draw(x)

    # Displaying the total of the outcomes
    heading = graphics.Text(graphics.Point(70,540),count1 + count2 + count3 + count4)
    heading.setSize(14)
    heading.draw(x)
    heading = graphics.Text(graphics.Point(154,540),"outcomes in total")
    heading.setSize(14)
    heading.draw(x)
    
# Creating a function to display the results on console
def display(outputs):
    print()
    print("Part 2 : ")
    for i in outputs:
        print(i)

# Creating a function to write results on a text file
def text(outputs):
    fo = open("cw.text","w")
    fo.write("Part 3 : \n")
    for i in outputs:
        fo.write(i)
        fo.write("\n")
        
    fo.close()

# Creating a function to update results according to the outcomes and counts
def results_final(outcome,outputs,count1,count2,count3,count4):
    if outcome == 'Progress':
        outputs.append(f"Progress - {pass_credits},{defer_credits},{fail_credits}")
        count1 += 1
            
    elif outcome == 'Progress (module trailer)':
        outputs.append(f"Progress (module trailer) - {pass_credits},{defer_credits},{fail_credits}")
        count2 += 1
        
    elif outcome == 'Module retriever':
        outputs.append(f"Module retriever - {pass_credits},{defer_credits},{fail_credits}")
        count3 += 1
        
    elif outcome == 'Exclude':
        outputs.append(f"Exclude - {pass_credits},{defer_credits},{fail_credits}")
        count4 += 1

    return outcome,outputs,count1,count2,count3,count4

# Creating a function to get know who is the user(student or staff)
def input_user():
    while True:
        input_user = input("Are you a (student or staff) : ").lower()
        if input_user in ['student','staff']:
            break
        print('Invalid \n')

    return input_user

# Creating a Dictionary
progression_outcomes = {
  (120, 0, 0): 'Progress',
  (100, 20, 0): 'Progress (module trailer)',
  (100, 0, 20): 'Progress (module trailer)',
  (80, 40, 0): 'Module retriever',
  (80, 20, 20): 'Module retriever',
  (80, 0, 40): 'Module retriever',
  (60, 60, 0): 'Module retriever',
  (60, 40, 20): 'Module retriever',
  (60, 20, 40): 'Module retriever',
  (60, 0, 60): 'Module retriever',
  (40, 80, 0): 'Module retriever',
  (40, 60, 20): 'Module retriever',
  (40, 40, 40): 'Module retriever',
  (40, 20, 60): 'Module retriever',
  (40, 0, 80): 'Exclude',
  (20, 100, 0): 'Module retriever',
  (20, 80, 20): 'Module retriever',
  (20, 60, 40): 'Module retriever',
  (20, 40, 60): 'Module retriever',
  (20, 20, 80): 'Exclude',
  (20, 0, 100): 'Exclude',
  (0, 120, 0): 'Module retriever',
  (0, 100, 20): 'Module retriever',
  (0, 80, 40): 'Module retriever',
  (0, 60, 60): 'Module retriever',
  (0, 40, 80): 'Exclude',
  (0, 20, 100): 'Exclude',
  (0, 0, 120): 'Exclude',
}

# Defining variables
outputs = []
count1 = 0
count2 = 0
count3 = 0
count4 = 0

# Getting user input
input_user = input_user()

# Main loop to get input credits and determine outcome
while True:
    try:
       # Getting inputs for PASS, DEFER and FAIL credits
       pass_credits = int(input("\nPlease enter your credits at PASS: "))
       while pass_credits not in [0,20,40,60,80,100,120]:
           print("Out of range\n")
           pass_credits = int(input("Please enter your credits at PASS: "))
           
       defer_credits = int(input("Please enter your credit at DEFER: "))
       while defer_credits not in [0,20,40,60,80,100,120]:
           print("Out of range\n")
           defer_credits = int(input("Please enter your credits at DEFER: "))
           
       fail_credits = int(input("Please enter your credit at FAIL: "))
       while fail_credits not in [0,20,40,60,80,100,120]:
           print("Out of range\n")
           fail_credits = int(input("Please enter your credits at FAIL: "))
           
    except ValueError:
       print("Integer required\n")
       continue

    # Checking if the total is equal to 120
    if pass_credits + defer_credits + fail_credits != 120:
        print("Total incorrect\n")
    else:
        outcome = progression_outcomes.get((pass_credits,defer_credits,fail_credits))
        
        # Updating the results according to the outcome
        outcome,outputs,count1,count2,count3,count4 = results_final(outcome,outputs,count1,count2,count3,count4)
            
        print(outcome,"\n")

        # Breaking the loop if the user is a student
        if input_user == 'student':
            break

        # Asking the user that if they want to know another set of data or quit
        while True:
            print('Would you like to enter another set of data?')
            new = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()

            if new in ['y','q']:
                break
            
        # Checking the user's choice
        if new == 'y':
            continue
        elif new == 'q':
            # Generating histogram, displaying results on console and writing the result to a text file
            counts = [count1,count2,count3,count4]
            histogram(counts)
            display(outputs)
            text(outputs)
            break
        

