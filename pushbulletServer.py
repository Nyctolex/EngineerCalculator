import sympy
from all_symbols import *
import asyncio
import os
import sys
import traceback
from asyncpushbullet import *
import sys
sys.path.insert(1, '.\\labCalculator')
from labCalculator import lab_calculator
from labCalculator import labFormat
import expresstion_praser
PROXY = os.environ.get("https_proxy") or os.environ.get("http_proxy")
EXIT_INVALID_KEY = 1
EXIT_PUSHBULLET_ERROR = 2
EXIT_OTHER = 3

NEW_FORMULA = "New formula".lower()
GET_EQUATION = "Get eq".lower()
GET_DEREVATIVE_error = "Get error".lower()

class MathServer():
    def __init__(self, api_key, name):
        self.api_key = api_key
        self.my_name = name
        self.api_key = api_key
        self.pb = None
        self.formula_string = None
        self.formula = expresstion_praser.prase_string('x**2+y')
        self.operations_dict = {}
        self.loop = asyncio.get_event_loop()
    
    def filter_new_messages(self, messages):
        pass
            # new_messages = []
            # pushes = self.pb.get_pushes()
            # for message in messages:
            #     if ('target_device_iden' in message) and ('body' in message):
            #         if message['target_device_iden'] == self.my_name:
            #             if not message['dismissed']:
            #                 new_messages.append(message)
            # new_messages = new_messages[::-1]
            # return new_messages
    
    def get_new_messages(self):
        pass
        # pushes = self.pb.get_pushes()
        # new_messages = self.filter_new_messages(pushes)
        # return new_messages
    
    def update_formula(self, message):
        self.formula_string = message['body'][len(NEW_FORMULA)+1:]
        self.formula = expresstion_praser.prase_string(self.formula_string)
        push = self.pb.push_note("Updated Formula", "Formula had been updated to:" + self.formula_string)
        print(self.formula)
    
    async def push_equation(self, equation, title= "", body = ""):
        filename = "equation.png"
        labFormat.save_expression_image(equation, filename)
        info = await self.pb.async_upload_file(filename)
        await self.pb.async_push_file(info["file_name"], info["file_url"], info["file_type"], \
            title=title , body=body)
    
    async def handler(self, message):
        pb =self.pb
        body = message['body'].lower()
        if NEW_FORMULA in body:
            self.update_formula(message)
        elif GET_EQUATION in body:
            print("pushing Image")
            self.push_equation(self.formula)
        elif GET_DEREVATIVE_error in body:
            print("pushing relative eror")
            await self.push_equation(lab_calculator.get_error_formula(self.formula, error_dict),\
                title="Error Formula")
        else:
            await pb.async_push_note(title="Error", body="Couldn't understand " + body)
    
    async def run(self):
        try:
            async with AsyncPushbullet(self.api_key, proxy=PROXY) as pb:
                self.pb = pb
                async with LiveStreamListener(pb) as lsl:
                    await pb.async_push_note(title="Server is working", body="Hey! I'm awake ")
                    async for push in lsl:
                        if 'target_device_iden:nickname' in push and push['target_device_iden:nickname'] == 'HomeServer':
                            await self.handler(push)
        except InvalidKeyError as ke:
            print(ke, file=sys.stderr)
            return EXIT_INVALID_KEY

        except PushbulletError as pe:
            print(pe, file=sys.stderr)
            return EXIT_PUSHBULLET_ERROR

        except Exception as ex:
            print(ex, file=sys.stderr)
            traceback.print_tb(sys.exc_info()[2])
            return EXIT_OTHER

with open('token.txt', 'r') as api_key_file:
    api_key = api_key_file.read()
name = 'HomeServer'
srv = MathServer(api_key, name)
sys.exit(srv.loop.run_until_complete(srv.run()))