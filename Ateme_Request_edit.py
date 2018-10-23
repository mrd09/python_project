import http.client
import xml.etree.ElementTree as ET
#import json

ateme_host = "127.0.0.1"
ateme_port = 80
requestUrl = "/restapi/jobs"

def getJobStatus(job_uuid):
    requestStatus_url = requestUrl + "/" + job_uuid
    conn = http.client.HTTPConnection(host=ateme_host, port=ateme_port)
    conn.request("GET", requestStatus_url)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    print(data)
    root = ET.fromstring(data)
    print(root)
    stateNodeList = root.findall("state")
    progressNodeList = root.findall("progress")

    stateNode = stateNodeList[0].text
    progressNode = progressNodeList[0].text
    print(stateNode)
    print(progressNode)


def createNewJob(job_name):
    try:
        requestBody = "<job><name>%s</name></job>" % job_name
        conn = http.client.HTTPConnection(host=ateme_host, port=ateme_port)
        conn.request("POST", requestUrl, body=requestBody)
        response = conn.getresponse().read()
        print(response)
        root = ET.fromstring(response)
        jobID = root.attrib["id"]
        print("[Create Job to ATEME Successfully] JobUUID: %s" % jobID)
        return jobID
    except Exception as e:
        print(e)

def addPreset(jobId, presetName):
    try:
        requestAddPreset = requestUrl + "/" + jobId + "/preset"
        requestBody = "<preset><name>%s</name></preset>" % presetName
        conn = http.client.HTTPConnection(host=ateme_host, port=ateme_port)
        conn.request("POST", requestAddPreset, body=requestBody)
        response = conn.getresponse()
        print("[Add Preset to ATEME Successfully] JobUUID: %s" % jobId, response.status, response.reason)
    except Exception as e:
        print(e)


def addOutput(jobId, fileName):
    try:
        requestAddOutPut = requestUrl + "/" + jobId + "/output"
        requestBody = "<output><file>%s</file></output>" % fileName
        conn = http.client.HTTPConnection(host=ateme_host, port=ateme_port)
        conn.request("POST", requestAddOutPut, body=requestBody)
        response = conn.getresponse()
        print("[Add output to ATEME Successfully] JobUUID: %s" % jobId, response.status, response.reason)
    except Exception as e:
        print(e)

def addSegment(jobId):
    try:
        requestAddOutPut = requestUrl + "/" + jobId + "/segments"
        requestBody = "<segment idx=\"1\"/>"
        conn = http.client.HTTPConnection(host=ateme_host, port=ateme_port)
        conn.request("POST", requestAddOutPut, body=requestBody)
        response = conn.getresponse()
        print("[Add segment to ATEME Successfully] JobUUID: %s" % jobId, response.status, response.reason)
    except Exception as e:
        print(e)

def addInputToSegment(jobId, filePath1, filePath2):
    try:
        requestAddOutPut_movie = requestUrl + "/" + jobId + "/segments/1/inputs"
        requestBody1 ="<input><uri>%s</uri></input>" % (filePath1)
        conn1 = http.client.HTTPConnection(host=ateme_host, port=ateme_port)
        conn1.request("POST", requestAddOutPut_movie, body=requestBody1)
        response1 = conn1.getresponse()
        print("[Add Input to Segment to ATEME Successfully: Movie] JobUUID: %s" % jobId, response1.status, response1.reason)

        requestAddOutPut_sub = requestUrl + "/" + jobId + "/segments/1/inputs"
        requestBody ="<input> <uri>%s</uri> </input>" % (filePath2)
        conn = http.client.HTTPConnection(host=ateme_host, port=ateme_port)
        conn.request("POST", requestAddOutPut_sub, body=requestBody)
        response = conn.getresponse()
        print("[Add Input to Segment to ATEME Successfully: Subtitle] JobUUID: %s" % jobId, response.status, response.reason)

    except Exception as e:
        print(e)

def getInputSegment(job_uuid):
    requestStatus_url = requestUrl + "/" + job_uuid + "/segments"
    conn = http.client.HTTPConnection(host=ateme_host, port=ateme_port)
    conn.request("GET", requestStatus_url)
    response = conn.getresponse()
    print("-------------")
    print("[List input]:", response.status, response.reason)
    data = response.read().decode()
    print(data)
    print("-------------")

def startJob(jobId):
    try:
        requestAddOutPut = requestUrl + "/" + jobId + "/state?value=pending"
        conn = http.client.HTTPConnection(host=ateme_host, port=ateme_port)
        conn.request("POST", requestAddOutPut,)
        response = conn.getresponse()
        print("[Start Job Successfully] JobUUID: %s" % jobId, response.status, response.reason)
    except Exception as e:
        print(e)

#def addDRM(jobId, keyString, url):
#    try:
#        requestBody = '<drm type="apple_encryption"><apple_encryption mode="CBC" autogenerated="false"><key mode="AES_128" type="Hexa"><data>%s</data></key><uri>%s</uri></apple_encryption></drm>' % (keyString, url)
#        requestAddDRM = requestUrl + "/" + jobId + "/drm"
#        conn = http.client.HTTPConnection(host=ateme_host, port=ateme_port)
#        conn.request("POST", requestAddDRM, body=requestBody)
#        response = conn.getresponse()
#        print(response.status, response.reason)
#        print("[ADD DRM to Job Successfully] JobUUID: %s" % jobId)
#    except Exception as e:
#        print(e)

#fileList = ["20180330124000_104_8001","20180330133500_96_9039"]
#print(len(fileList))

#fileList = ["A_4"]



# inputFilePath = "C:\\Users\\Castis\\Desktop\\TVOD\\input\\%s.mpg" % fileName
inputFilePath = "C:\\Users\\Castis\\Desktop\\vtvcab\\Subtitle\\Sing.mp4"
inputSubPath = "C:\\Users\\Castis\\Desktop\\vtvcab\\Subtitle\\Sing.mp4.srt"
outputFile = "C:\\Users\\Castis\\Desktop\\vtvcab\\python_HD_sub.ts"
presetName = "HYBRID-HD_BurnedSub"
#keyString = "79F5EA729EBB2642D052F5FE403B03E6"
# 1. Create job
jobUUID = createNewJob(inputFilePath)
# print(jobUUID)
# 2. Add Preset
addPreset(jobUUID, presetName)
# 3. Add output path
addOutput(jobUUID, outputFile)
# 4. Add segment
addSegment(jobUUID)
# 5. Add input to segement
addInputToSegment(jobUUID, inputFilePath, inputSubPath)
# 5.1 Get Input Segment
getInputSegment(jobUUID)
# 6 Add Drm key
#addDRM(jobUUID, keyString, url)
# 7 Start Encoding Job
startJob(jobUUID)
# 8 Get Encoding Status
getJobStatus(jobUUID)

