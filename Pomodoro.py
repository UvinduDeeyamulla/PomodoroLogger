import time
import winsound
import pandas as pd
import streamlit as st


st.title("Pomodoro logger",text_alignment="center")
Goals = st.text_area("Set goals for the sessions(Seperate each goal with a ' comma (,) ')")
Goal_list = Goals.split(",")
def countdown(minutes):
    seconds = minutes * 60 #convert the argument(minutes) into seconds
    bar = st.progress(0)
    timer_text = st.empty()

    while seconds: # while 0 = while False 
        mins = seconds // 60 #Floor division (65//60 = 1.083-> returns 1)
        secs = seconds % 60 # returns 0.083 for 65 
        timer = f"⌛{mins:02d}:{secs:02d}" # d = int formating (for 0 -> returns 00)
        timer_text.header(timer,text_alignment="center")  
        ### \r = carriage return (Updates the existing line)-> terminal
        bar.progress((minutes*60-seconds+1)/(minutes*60)) #Standardization [0,100]
        time.sleep(1) # For each iteration pause for 1 second
        seconds -= 1 
       


def log(start, end, work_time, cycle):
    new_entry_df = pd.DataFrame([{
        "Start Time": start,
        "End Time" : end,
        "Duration (Minutes)": work_time, 
        "Cycle Number": cycle
    }])
# filename = "Pomodoro_log.csv"
    ## Updated_df = pd.DataFrame()

    # if os.path.exists(filename):
    ## if Updated_df.empty == True: To check whether a df is empty 
    
    #     Current_df = pd.read_csv(filename)
    # else:
    return new_entry_df
    # Updated_df.to_csv(filename,index=False)

def Terminate():
    return False

def pomodoro(work=0 , short_break=0  , cycles=0):
    Final_df = pd.DataFrame()
    for cycle in range(1,cycles+1):
        print(f"\n Pomodoro cycle: {cycle}: Work for {work} minutes")

        start = time.ctime()
        st.write("Study session", cycle, "started!📚")
        countdown(work) # Countdown function is called {cycles} times setting it to {work} mins each round because it's inside a for loop         
        end = time.ctime()
        st.success(f"Study session {cycle} over!⏱️")
        New_entry = log(start = start, end = end, work_time = work, cycle=cycle)
        Final_df = pd.concat([Final_df,New_entry])
        
        for beep in range(2):
            winsound.Beep(1000,1000) # frequency = 1000 Hz, time = 1000 ms
        print("Work session completed!")

        if cycle < cycles:
            print(f"Take a {short_break} minute break.")
            st.write("Session",cycle,"Short break started!⛓️‍💥")
            countdown(short_break) # Calling the countdown function setting it to {short_break} mins.
            winsound.Beep(1000,1000)
            st.success(f"Short break {cycle} over!🏁 🔥Back to work!🔥")
            print("Break done! Back to work.")
        else:
            time.sleep(1)
            st.write("Summary of the study cycles")
            st.write(Final_df)
            time.sleep(1)
            st.write("Congratulations! All cycles were completed👏")
            time.sleep(1)
            for goal in Goal_list:
                st.write(goal, "Completed✅")
                time.sleep(1)

            print(f"\n Congratulations! All {cycle} cycles completed") # When the iteration meets cycle = cycles  





Work_session = int(st.text_input("Enter time for study session (in minutes) *Integer only",value = 0))


Break_session = int(st.text_input("Enter break duration (in minutes) *Integer only",value = 0))


Number_of_cycles = int(st.text_input("Enter the number of study cycles *Integer only",value = 0))

# st.button("Start",on_click=pomodoro(Work_session,Break_session,Number_of_cycles))

pomodoro(Work_session,Break_session,Number_of_cycles)
