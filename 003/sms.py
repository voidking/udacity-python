from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACd09e2957573ceb7fc6943bc5fd1cad80" 
AUTH_TOKEN = "9799aff41376bf35a4e3baea7584e0dd" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
    to="+8615195892217", 
    from_="+19363374516", 
    body="My name is VoidKing?",  
)

# 使用anoconda会报错
# from twilio.rest import TwilioRestClient ImportError: No module named rest
# 经验证，是因为版本问题，在github上自行下载3.6.9版本，即可解决该问题
# 不过，国内手机接收短信延迟严重，本人试了两次，延迟在20-50分钟