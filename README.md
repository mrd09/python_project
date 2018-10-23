# python_project
Personal project
1. Ateme Encoder API Request test:
-	Library: 
	+ http.client
	+ xml.etree.ElementTree 
-	Scenarios:
	CMS	->	Ateme Encoder:
	# 1. Create job: jobUUID = createNewJob(inputFilePath)
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

2. 	Selenium Webdriver:
-	Library: selenium
	+ module: webdriver
-	Relate Libaray: os, time, datetime
-	Selenium tutorial: **Selenium_windows/Selenium_Install_tut.md**