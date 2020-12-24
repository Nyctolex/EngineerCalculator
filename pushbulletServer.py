import sympy
from all_symbols import *
from pushbullet import Pushbullet
import sys
sys.path.insert(1, 'C:\\Users\\chris-chen\\Documents\\TAU\\EngeeMath\\EngineerCalculator\\labCalculator')
import lab_calculator
import labFormat
#from .labCalculator import labFormat
#from .labCalculator.lab_calculator import lab_calculator
import expresstion_praser

NEW_FORMULA = "New formula".lower()
GET_EQUATION = "Get eq".lower()
GET_DEREVATIVE_error = "Get error".lower()

class MathServer():
    def __init__(self, api_key, name):
        self.api_key = api_key
        self.my_name = name
        self.pb = Pushbullet(api_key)
        self.formula_string = None
        self.formula = expresstion_praser.prase_string('x**2+y')
        self.operations_dict = {}
        while True:
            self.run()
    
    def filter_new_messages(self, messages):
        new_messages = []
        pushes = self.pb.get_pushes()
        for message in messages:
            if ('target_device_iden' in message) and ('body' in message):
                if message['target_device_iden'] == self.my_name:
                    if not message['dismissed']:
                        new_messages.append(message)
        new_messages = new_messages[::-1]
        return new_messages
    
    def get_new_messages(self):
        pushes = self.pb.get_pushes()
        new_messages = self.filter_new_messages(pushes)
        return new_messages
    
    def update_formula(self, message):
        self.formula_string = message['body'][len(NEW_FORMULA)+1:]
        self.formula = expresstion_praser.prase_string(self.formula_string)
        push = self.pb.push_note("Updated Formula", "Formula had been updated to:" + self.formula_string)
        print(self.formula)
    
    def push_equation(self, equation):
        name = "equation.png"
        labFormat.save_expression_image(equation, name)
        with open(name, "rb") as pic:
            file_data = self.pb.upload_file(pic, name)
        push = self.pb.push_file(**file_data)
    
    def run(self):
        messages = self.get_new_messages()
        for message in messages:
            print("New Messages")
            body = message['body'].lower()
            if NEW_FORMULA in body:
                self.update_formula(message)
            elif GET_EQUATION in body:
                print("pushing Image")
                self.push_equation(self.formula)
            elif GET_DEREVATIVE_error in body:
                print("pushing relative eror")
                self.push_equation(lab_calculator.get_error_formula(self.formula, error_dict))
            else:
                self.pb.push_note("Error", "Couldn't understand " + body)
            self.pb.dismiss_push(message.get("iden"))


api_key = "o.cjbX42vfDbs6pJqZDHVp9ivihxfptDaa"
name = 'uju33m770o0sjyWM7YCvbo'
srv = MathServer(api_key, name)


#push = pb.push_note("This is the title", "This is the body")
# with open("linear_data.png", "rb") as pic:
#     file_data = pb.upload_file(pic, "linear_data.png")

# push = pb.push_file(**file_data)

#pushes = pb.get_pushes()
# for message in pushes:
#     pass
#print(pushes[0])

#latest = pushes[0]
#print(pushes)
# We already read it, so let's dismiss it
#pb.dismiss_push(latest.get("iden"))


# x, y, z = sympy.symbols('x y z')
# expr = x * y ** 3 - y * x ** 3
# sp.preview(expr, viewer='BytesIO', outputbuffer=f)
#sympy.preview(expr, viewer='file', filename='output.png')
# e = x**2
# p1 = plot(e, show=False)
# p =  sympy.plotting.plot(e, show=False)
# p.saveimage('/plot.png', format='png')