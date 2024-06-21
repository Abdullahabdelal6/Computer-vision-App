AI Coach

This project is an AI application that utilizes Computer Vision technology, Pose Estimation, and Speech Recognition 
to provide accurate tracking of exercise repetitions during gym workouts. By doing so, it aims to enhance users' fitness routines.



Project Structure


main.py: The main Python script that runs the Streamlit app.
ExerciseAiTrainer: Pose estimation logic specific for each exercise.
AiTrainer_utils.py: utils functions (resize image, calculate distance)
PoseModule2.py: Body Pose estimation logic
requirements.txt: List of Python libraries required for this project.
mp3 files: Voice of the AI trainer
mp4 files: Demo video of exercises (push up, curl, squat, etc)


How to Run
To run the application, open your terminal and execute the following command:

  ```bash
  streamlit run main.py

Technologies Used
Computer Vision: For pose estimation and exercise tracking.
Speech Recognition: For voice-activated controls.
Streamlit: For the web application interface.
Technologies: Python, OpenCV, Streamlit, mediapipe, Speech Recognition API
