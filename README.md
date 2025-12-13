## 🍅 Streamlit Pomodoro Logger

A simple, web-based Pomodoro Timer built with Streamlit and Python, designed to help you focus and log your work sessions automatically.

![screenshot](Assets/Pomodoro.png)

-----

## ✨ Key Features

  * **Customizable Timer:** Set your own durations for work sessions and short breaks.
  * **Goal Setting:** Input specific goals at the start of your session (separated by commas).
  * **Session Logging:** Automatically records the start time, end time, duration, and cycle number of each work session into a Streamlit DataFrame.
  * **Visual Feedback:** Uses a dynamic progress bar and digital timer within the Streamlit interface.
  * **Audio Alerts:** Uses `winsound` to beep when a session starts or ends (Windows-compatible feature).

-----

## 🚀 Installation & Setup

This is a Python application that uses Streamlit for its interface.

### Prerequisites

  * Python 3.x

### Steps

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Uvindu Deeyamulla/UKD-pomodoro-repo.git
    cd UKD-pomodoro-repo
    ```

2.  **Install Dependencies:**

    The core dependencies are listed below. Ensure you have them installed:

    ```bash
    pip install streamlit pandas
    ```

3.  **Run the Application:**

    Execute the application using the Streamlit CLI:

    ```bash
    streamlit run Pomodoro.py
    ```

    The app will automatically open in your default web browser.

-----

## ▶️ Usage

1.  **Set Your Goals:** Enter your goals in the text area, separated by commas (e.g., "Finish Chapter 5, Outline Presentation, Check Email").
2.  **Configure Times:** Enter the duration (in minutes) for your work session, break, and the total number of cycles.
3.  **Start:** Since the `pomodoro` function is called directly at the end of the script, the timer will start automatically once you input valid integers for the session times.

### Log Output

Upon completion of all cycles, a summary table will be displayed directly in the Streamlit application showing the following data for each session:

| Column | Description |
| :--- | :--- |
| **Start Time** | The time the work session began (`time.ctime()`). |
| **End Time** | The time the work session ended. |
| **Duration (Minutes)** | The set duration of the work session. |
| **Cycle Number** | Which Pomodoro cycle the data belongs to. |

-----

## 🛠️ Technologies Used

  * **Python 3.x**
  * **Streamlit:** For creating the interactive web interface.
  * **Pandas:** For creating and displaying the session log (`Final_df`).
  * **`winsound`:** For playing sound alerts (Note: This module is specific to **Windows**).

-----

## 👤 Contact


Uvindu Deeyamulla - udeeyamulla@gmail.com 
