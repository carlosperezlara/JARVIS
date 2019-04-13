from AllModules import *

numEvents = 20000 
sampleRate = 20 
horizontalWindow = 175
trigCh = "AUX" 
trig = -0.15

############### Remember to source the otsdaq environment
############### Assuming the directory structure in the KeySightScope repository is the same as on this computer

AutoPilotStatusFile = '%sAcquisition/ScopeStatus.txt' % ScopeControlDir
AgilentScopeCommand = 'python %sAcquisition/acquisition.py --numEvents %d --sampleRate %d --horizontalWindow %d --trigCh %s --trig %f' % (ScopeControlDir, numEvents, sampleRate, horizontalWindow, trigCh, trig) 

while True:

	inFile = open(AutoPilotStatusFile,"r")
	status = inFile.readline(1)
	time.sleep(1)
	if (status == str(1)):
	   	############### checking the status for the next runs #################  
	    with open(AutoPilotStatusFile,'w') as file:
	        file.write(str(0))
	    print "\n ####################### Running the scope acquisition ##################################\n"
	    os.system(AgilentScopeCommand)
	    print "\n ####################### Done with the scope acquisition ##################################\n"
