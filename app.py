import streamlit as st
from behavioral_coaching import BehavioralCoaching
from focus_time_management import FocusTimeManagement
from progress_tracking import ProgressTracking
from gamified_training import GamifiedTraining
from resource_sharing import ResourceSharing
from localization import Localization

# Initialize components
coaching = BehavioralCoaching()
focus_tools = FocusTimeManagement()
progress_tracker = ProgressTracking()
gamified_training = GamifiedTraining()
resource_sharing = ResourceSharing()
localization = Localization()

# Streamlit UI
st.title("ADHD AI Agent")
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Select a feature", ["Behavioral Coaching", "Focus Tools", "Progress Tracking", "Gamified Training", "Resource Sharing", "Localization"])

if option == "Behavioral Coaching":
    coaching.run()
elif option == "Focus Tools":
    focus_tools.run()
elif option == "Progress Tracking":
    progress_tracker.run()
elif option == "Gamified Training":
    gamified_training.run()
elif option == "Resource Sharing":
    resource_sharing.run()
elif option == "Localization":
    localization.run()
