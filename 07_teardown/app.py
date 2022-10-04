'''
# TNPG: VAT, Vivian Graeber, Ayman Habib, Talia Hsia
# SoftDev
# K07 -- Learning about Flask
# 2022-10-03
# time spent: 15 min
'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
QCC:
0. Java
1. It accesses a folder or directory
2. It prints to the terminal
3. It might print a file that would be inputted in place of '__name__"
4. No, because there is no print statement associated with that line
5. Java 
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
 
 We looked at the code, and made educated guesses based on our prior knowledge of other languages. mainly Java.
'''
