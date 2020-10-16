# Machine-Learning-Face-Recognition-using-openCV
Using python OpenCV module to train and recognize up to 5 faces and generate automated voice feedback

# Project contains 3 python files:
 Creator.py --> Uses your webcam to take multiple pictures of your face and crops it and turns to grayscale to be analyzed later
 
 Trainer.py --> Uses the saved pictures to start analyzing trends and picks up on differentiating features of each face to generate a .YML file
 
 Detector.py --> Will Use the .YML file to run the actual face detection program. It will provide AUDIO FEEDBACK based on who it recognizes. It will also print the percent confidence of each of the detection. (You can change this in the detector.py prgram { variable called conf })

# REQUIRED:
 all 3 python files
 2 folders with "dataSet" and trainer" name
 a webcam set to default and good lighting conditions

# STEPS: 
 STEP 1: Run creator.py and wait until picture taking process is completed
 
 STEP 2: Run the trainer.py to analyze the JPG pictures and create YML file. IT will ask for a number, which is the ID of each of the 5 possible faces. Choose 1-5 accordingly and hit enter.
 
 STEP 3 (OPTIONAL) save .MP3 files to the same folder with audio that you want to play for each unique face detected successfully
 
 STEP 3: Run the detector.py to begin facial analysis/detection

## ENJOY!
### SRI KANIPAKLA
