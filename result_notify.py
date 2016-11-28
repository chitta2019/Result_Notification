#This Program will Send you a Sweet SMS when your results will be declared.
#Author Chittaranjan Kumar (@chitta2019)
#Just_for_fun
#V~2.0


import urllib2
import re
import time
import cookielib


#Edit you credentials here!!!!!
username = "<your_way2sms_number>"
password = "<your_password>"
number = "<number_to_send_msg>"
message = "Oops! Results out, Best of Luck. Here you go: http://result1.gtu.ac.in"
message = "+".join(message.split(' '))

#login
url = 'http://site24.way2sms.com/Login1.action?'
data = 'username='+username+'&password='+password+'&Submit=Sign+in'

#cookie
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#header
opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
     
usock = opener.open(url, data)
session_id = str(cj).split('~')[1].split(' ')[0]
send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
send_sms_data = 'ssaction=ss&Token='+session_id+'&mobile='+number+'&message='+message+'&msgLen=136'
opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+session_id)]

while 1:

    html_content = urllib2.urlopen('http://old.gtu.ac.in/results.asp').read()
    matches = re.findall('BE SEM 5 - Regular', html_content);


    if len(matches) == 0: 
       print "Yeah, Result Not Declared. Going to sleep" #will not send anything
       time.sleep(7200) #sleep for 2 hours

    else:
       sms_sent_page = opener.open(send_sms_url,send_sms_data)			
       print "SMS Sent Thanks"
       quit()
