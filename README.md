# python_project
Personal project
1. Ateme Encoder API Request test:
-	Library: 
	+ http.client
	+ xml.etree.ElementTree 
-	Scenarios:
	CMS	->	Ateme Encoder:
	+ Create job: jobUUID = createNewJob(inputFilePath)
	+ Add Preset
		addPreset(jobUUID, presetName)
	+ Add output path
		addOutput(jobUUID, outputFile)
	+ Add segment
		addSegment(jobUUID)
	+ Add input to segement
		addInputToSegment(jobUUID, inputFilePath, inputSubPath)
	+ Get Input Segment
		getInputSegment(jobUUID)
	+ Add Drm key
		#addDRM(jobUUID, keyString, url)
	+ Start Encoding Job
		startJob(jobUUID)
	+ Get Encoding Status
		getJobStatus(jobUUID)

2. 	Selenium Webdriver:
-	Library: selenium
	+ module: webdriver
-	Relate Libaray: os, time, datetime
-	Selenium tutorial: **Selenium_windows/Selenium_Install_tut.md**