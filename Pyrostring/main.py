import os, asyncio,pandas,sys
from pyrogram import Client
from pyrogram.errors import AuthKeyUnregistered,SessionPasswordNeeded,PhoneCodeInvalid,PasswordHashInvalid
from pandas.errors import EmptyDataError
from typing import List

#config.py
from config import API_ID,API_HASH
path = os.path.dirname(os.path.abspath(__file__))
try:
    numbers = pandas.read_csv(filepath_or_buffer=f"{path}/numbers.csv", header=None)
    NUMBER_LIST  : List[int] = [col[0] for col in numbers.values.tolist()]
except EmptyDataError:
    print('NUMBER LIST IS EMPTY: PLEASE ADD YOUR NUMBER IN: numbers.csv')
    sys.exit()

try:
    strings = pandas.read_csv(filepath_or_buffer=f"{path}/session_string.csv", header=None)
    STRING_LIST  : List[str] = [col[0] for col in strings.values.tolist()]
except EmptyDataError:
    STRING_LIST = []
    




async def multi():
    print("__STARTED__")
    STRING_CACHE: List[str] = []
    for cli in NUMBER_LIST:
        if cli in STRING_LIST:
            continue
        cli = str(cli)
        app = Client(f"{path}/session/{cli}", api_id=API_ID, api_hash=API_HASH)
        await app.connect()
        try:
            name = await app.get_me()
            print(f"{cli} | {name.first_name}")
            session_string = await app.export_session_string()
            data = cli,session_string
            print(data)
            STRING_CACHE.append(data)
        except AuthKeyUnregistered:
            try:
                print(f'{cli} : NEED SESSION')
                send_code = await app.send_code(cli)
                try:
                    await app.sign_in(cli, send_code.phone_code_hash, phone_code = input("Enter the code: "))
                except PhoneCodeInvalid:
                    try:
                        await app.sign_in(cli, send_code.phone_code_hash, phone_code  = input("Phone Code Invalid | Enter the code: "))
                    except PhoneCodeInvalid:
                        print(f'SKIPPING: {cli} WRONG CODE 2x')
                        continue
                        
            except SessionPasswordNeeded:
                try:
                    await app.check_password(input(str("Enter Auth Password: ")))
                except SessionPasswordNeeded:
                    try:
                        await app.check_password(input(str("Invalid Auth | Enter Auth Password: ")))
                    except SessionPasswordNeeded:
                        print(f'SKIPPING: {cli} WRONG AUTH 2x')
                        continue

            name = await app.get_me()
            print(f"{cli} | {name.first_name}")
            session_string = await app.export_session_string()
            STRING_CACHE.append({cli:session_string})
        
    Data_frame = pandas.DataFrame(STRING_CACHE)
    Data_frame.to_csv(path_or_buf='session_string.csv',index=False,mode='a',header=False)
                            


asyncio.run(multi())
