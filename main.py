import sqlite3 as sq

class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def plus(self):
        return self.num1 + self.num2
    
    def min(self):
        return self.num1 - self.num2
    
    def div(self):
        return self.num1 / self.num2
    
    def mult(self):
        return self.num1 * self.num2
    
def opros():
    num = int(input("Num?:"))
    return num

def Apendb(num1, num2, work, res):
    cur.execute(f"""  INSERT INTO CalcResult (FirstNum, SecondNum, Work, Result) VALUES ({num1}, {num2}, "{work}", {res})""")
    print(f"Result {res}")

with sq.connect("dbbase.db") as db:
    cur = db.cursor()

    cur.execute(""" CREATE TABLE IF NOT EXISTS CalcResult (
                FirstNum INTEGER,
                SecondNum INTEGER,
                Work TEXT,
                Result INTEGER
    )""")


    
    num1 = opros()
    num2 = opros()
    WhoWork = input(f"(+,-,*,/)?: ")

    calc = Calculator(num1, num2)

    if WhoWork == "+":
        res = calc.plus()
        Apendb(num1, num2, WhoWork, res)
    elif WhoWork == "-":
        res = calc.min()
        Apendb(num1, num2, WhoWork, res)
    elif WhoWork == "*":
        res = calc.mult()
        Apendb(num1, num2, WhoWork, res)
    elif WhoWork == "/":
        res = calc.div()
        Apendb(num1, num2, WhoWork, res)


