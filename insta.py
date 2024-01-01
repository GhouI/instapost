from instabot import Bot
import os 
from PostSchedule import PostSchedule

photos_directory = ""  # Define photos_directory as a global variable

def login_to_instagram(username, password):
    bot = Bot()
    bot.login(username=username, password=password)

def ask_for_photos_directory():
    global photos_directory  # Use the global keyword to modify the global variable
    photos_directory = input("Enter the photos directory: ")

def check_for_jpeg_images(directory):
    files = os.listdir(directory)
    if not any(file.lower().endswith(".jpg") or file.lower().endswith(".jpeg") for file in files):
        print("JPEG/JPG image not found")

# Assuming the PostSchedule class has a method for getting the next scheduled post time
# and also assuming you have the code for posting the image using instabot library

def check_and_post_scheduled_image():
    schedule = PostSchedule()
    # Assuming there is a method to add the scheduled posts to the PostSchedule instance
    # schedule.add_post("Some description", "2023-10-10 10:00:00")

    next_post_time = schedule.get_next_post_time()
    
    current_time = datetime.now()  # Get current time
    
    if current_time >= next_post_time:
        global photos_directory  # Use the global keyword to access the global variable
        ask_for_photos_directory()  # Call the function to update the photos_directory
        check_for_jpeg_images(photos_directory)
        # Call the function to post the image
        # post_image_function_from_instabot_library()
