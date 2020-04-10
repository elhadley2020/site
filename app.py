from flask import Flask 
from flask import request

user_agent = request.headers.get('User-Agent')

#variables for architecture test     
x64_test = "x86_64"
architectures = ["x64","x86"]
architecture = ""

#architecture test against user agent
if x64_test in user_agent:
    architecture = architectures[0]
else:
    architecture = architectures[1]

#variables for operating systems test
android_test = "Android"
linux_test = "Linux"
window_test = "Windows"
operating_systems = ["android","linux","windows"]
operating_system = ""

if linux_test in user_agent:
    operating_system = operating_systems[1]
    if android_test in user_agent:
        operating_system = operating_systems[0]
else:
    operating_system = operating_systems[2]
    