import SMS_ALL_YEAR_Latest
import smslogin_form
from tkinter import*
import os



def main():
    result=smslogin_form.authenticate()
    print(result)
    if result[2]:
        SMS_ALL_YEAR_Latest.call(result[0],result[1])
        main()
        
main()
