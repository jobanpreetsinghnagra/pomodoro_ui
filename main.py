import streamlit as st
import time

st.title("Pomodoro :red[Technique] ")

#get input from user in minutes
time_minutes = st.slider("Select the  time (in minutes) for which you want to :rainbow[focus] for:",min_value=1,max_value=60,value = 25)
st.write(f"You have selected", time_minutes, "minutes ")

starter = 0
if st.button("Start"):
    starter = 1

if starter == 1:
    time_text = "Time to work!!"
    time_bar = st.progress(0, text=time_text)
    
    # Convert minutes to seconds for total duration
    total_seconds = time_minutes * 60
    
    # Number of steps for smooth progress (you can adjust this)
    steps = 100
    
    # Calculate sleep time per step
    sleep_per_step = total_seconds / steps
    
    for step in range(steps + 1):
        # Calculate progress percentage (0 to 1)
        progress = step / steps
        
        # Update progress bar
        time_bar.progress(progress, text=time_text)
        
        # Sleep for calculated time per step
        if step < steps:  # Don't sleep after the last step
            time.sleep(sleep_per_step)
    
    # Clear progress bar and show celebration
    time_bar.empty()
    st.balloons()
    st.success("Pomodoro session completed! Great job! 🍅")

if st.button("Restart"):
    st.rerun()