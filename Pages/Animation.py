import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(
    page_title="Animation",
    page_icon=":house:",
    layout="wide",
)

st.title("Animation")

placeholder = st.empty()

# Parameters for the sine wave
x = np.linspace(0, 10, 500)  # X values
frequency = 1  # Base frequency of the sine wave

# Simulate an animation
for frame in range(100):
    y = np.sin(2 * np.pi * (frequency * x - 0.02 * frame))  # Create sine wave values
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"Frame {frame}", color='blue')
    ax.set_ylim(-1.5, 1.5)
    ax.legend(loc="upper right")
    ax.set_title("Mock Animation")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    
    # Display the animation frame in the placeholder
    placeholder.pyplot(fig)
    
    # Add a small delay to simulate animation speed
    time.sleep(0.05)

# Show completion message
st.success("Animation Complete!")

