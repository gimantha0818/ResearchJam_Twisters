**Stepscan Live**

Pressure data. Serial ID of the tile can be identified from the API. 

Install stepscanlive.msi

DAQ.exe can be interfaced to the UI (C++ based) in Example Apps folder. 

DAQ.exe has two configutation files 
1)DAQ.confiq is autogrenerated by stepscan live. 
2)Tilelookup -> serialnumbers.dat (the API will need the 12 tile associated lookup files). 

So you would use the API in a loop. 

E.g.: 
while(TRUE) 
api.read(data)

titleReader.read()


Colours:
Red, Green and Blue

split the two tile array to 3 colours. 720x240 dimensional block. 
1 player only. Get from point A to point B. 

Steps:
1)Starting position

2)Randomize new action -> instructions displayed on Screen UI. 

3)Check correctness. 

4)Limb phase -> contact or no-contact. 10kPa threshold for contact detection. 

5)Allowed to move and not allowed to move and error of action -> Disqualified. 

6)End -> Passed!
