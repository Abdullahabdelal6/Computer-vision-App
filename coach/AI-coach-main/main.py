import streamlit as st
from Audio import text_to_speech, get_audio
import cv2
import ExerciseAiTrainer as exercise


def main():

    
    st.title('Your AI coach')

    st.write("""
        ## Welcome to your coach
        """)

    
    option = 'WebCam'

    # User can select different exercises
    exercise_general = st.sidebar.selectbox(
        'Select Exercise', ('Bicept Curl', 'Push Up', 'Squat', 'Shoulder Press')
    )

    # Define a button for start the analysis (pose estimation) on the webcam
    st.write(' ## Click button to activate AI Trainer')
    st.write("Say 'Ready' to get started")
    button = st.button('Activate AI Trainer')

    # Visualize video that explains the correct forms for the exercises
    if exercise_general == 'Bicept Curl':
        st.write('## Bicept Curl Execution')
        st.video('curl_form.mp4')

    elif exercise_general == 'Push Up':
        st.write('## Push Up Execution')
        st.video('push_up_form.mp4')

    elif exercise_general == 'Squat':
        st.write('## Squat Execution')
        st.video('squat_form.mp4')

    elif exercise_general == 'Shoulder Press':
        st.write('## Shoulder Press Execution')
        st.video('shoulder_press_form.mp4')

    # if the button is selected, after a Vocal command, start the webcam analysis (pose estimation)
    if button:
        # Ask user if want to start the training (using text to speech)
        text_to_speech('Are you Ready to start Training?')
        # get the audio of the user
        text = get_audio()

        # if user is ready (say 'yes' or 'ready') then start the webcam analysis
        if 'ready' in text.lower() or 'yes' in text.lower():
            text_to_speech("Ok, Let's get started")
            st.write('READY')
            ready = True

            # Initialize webcam
            cap = cv2.VideoCapture(0)
            exer = exercise.Exercise()

            # for each type of exercise call the method that analyze that exercise
            if exercise_general == 'Bicept Curl':
                while ready:
                    exer.bicept_curl(cap)

            elif exercise_general == 'Push Up':
                while ready:
                    exer.push_up(cap)

            elif exercise_general == 'Squat':
                while ready:
                    exer.squat(cap)

            elif exercise_general == 'Shoulder Press':
                while ready:
                    exer.shoulder_press(cap)

            # Release the webcam
            cap.release()
            cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
