#intall this pip install CoWIN-API-by-kunal-kumar-sahoo
from cowin_api import CoWinAPI     #use to get data
import datetime
from plyer import notification     #use for desktop notification

def notifyme(title,message):
    '''
    gives notification title  with message
    '''
    notification.notify(
    title=title,
    message=message,
    app_icon=None,
    timeout=5
    )

def printdetails(centers,session):
    '''
    sends title and message
    '''
    notifyme("alert",f"center name: {centers['name']},\naddress: {centers['address']},\nvaccine: {session['vaccine']},  fees: {centers['fee_type']}")

             
pin_code="110044"

#takes cuurent date
date=datetime.datetime.today().strftime("%d-%m-%Y")

age=18      #age group

cowin=CoWinAPI()

#gives data of all available centers at that pincode and for that age group
available_centers=cowin.get_availability_by_pincode(pin_code,date,age)

#extract valuable data 
for centers in available_centers['centers']:
    session=centers['sessions'][0]
    if session['available_capacity']!=0:
        printdetails(centers,session)
        break
else:
    notifyme("info","no slot available now ")
    

    
