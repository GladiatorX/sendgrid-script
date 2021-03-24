import pandas as pd
import time
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

moreThanOnce = # list of emailID that appear more than once
SENDGRID_API_KEY = 'XXXX' # your API key recieve from Send Grid
  
def sendMail ( fromEmail, toEmail, cardNumber, cardName, qrNumber):             #fromEmail, toEmail):
    message = Mail(
        from_email=fromEmail,
        to_emails=toEmail,
        subject='Entry pass (QR Code) for EVENT to be held on 19th Oct 2019',
        html_content='''
        <html>
            <body>
                <img src='https://www.someevent.in/attachments/header.jpg'>
                <hr><div style='border: 1px solid #e1dede; background: #eff0f1; width: 720px; height: 280px;'>
                <div style='height: 270px;width: 710px;background: white;margin: 5px;'> <span><center style='padding-bottom: 50px; padding: 10px; font-family: sans-serif;'><strong>EVENT ENTRY PASS</strong></center></span>
                <br/><div style='width: 450px; float: left; margin-top: 20px;'>
                <section><label style='padding: 10px;'>EVENT Card Registration Number:</label><strong>{}</section><br/>
                <section><label style='padding: 10px;'>Name:</label><strong>{}</strong></section><br/><br>

                <p style='padding: 20px;font-size: small; font-weight: 600;'><small>NOTE: PLEASE CARRY ENTRY PASS AT THE VENUE. REQUIRED TO BE PRODUCED AS AND WHEN REQUESTED BY THE OFFICIALS. </small></p></div>";
                <div class='right' style='width: 210px; float: right; margin-top: 20px;'>

                <img src='https://www.someevent.in/images/QRcodes/{}.png' width='100' height='100'>

                <p><small><strong>Venue: Some Community Centre <br/>Date: 19th Oct 2019<br/>Time: 9.00am to 5.00pm</strong></small></p></div></div></div></div>
            </body>
        </html>    
        '''.format( cardNumber, cardName, qrNumber))    
        
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        #print(response.body)
        #print(response.headers)
    except Exception as e:
        print(str(e))





#######################################################Define Max_len
#df= df[34000:] #df[:n-1] #from 500 onwards
#######################################################

totalSent = 0
totalNotSent = 0

df = pd.read_csv("CliesnEmailData.csv") # the file has "Email" as a column that holds all email id of the customers

for index,row in df.iterrows():
    #if its an email only
    if ((type(row["Email"]) == str) ):
        #if it is unique only
        if row["Email"].strip() not in moreThanOnce :
            #send email
            fromEmail = "donotreply@someevent.com"
            toEmail =  row['Email']#
            cardNumber = row['Registration No']
            cardName = row['Name']#
            qrNumber = row['QrValue']#
            print( row['Email']," Sent: INDEX",index)
            sendMail(fromEmail, toEmail, cardNumber, cardName, qrNumber)
            #time.sleep(1)
            totalSent += 1
        else:
            print( row['Email'],"  not sent, INDEX",index)
            totalNotSent += 1

print("SENT===============>",totalSent) 
print("NOT SENT============>",totalNotSent)



