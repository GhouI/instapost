from datetime import datetime
from insta import login_to_instagram, ask_for_photos_directory, check_for_jpeg_images, photos_directory
from PostSchedule import PostSchedule

def schedule_posts():
    schedule = PostSchedule()
    while True:
        description = input("Enter the post description (or 'q' to quit): ")
        if description.lower() == 'q':
            break
        time = input("Enter the post time in the format 'YYYY-MM-DD HH:MM:SS': ")
        schedule.add_post(description, time)

def check_and_post_scheduled_image(schedule):
    next_post_time = schedule.get_next_post_time()
    current_time = datetime.now()  # Get current time
    
    if current_time >= next_post_time:
        ask_for_photos_directory()  # Call the function to update the photos_directory
        check_for_jpeg_images(photos_directory)
        # Call the function to post the image
        # post_image_function_from_instabot_library()

def main():
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    login_to_instagram(username, password)
    schedule_posts()
    check_and_post_scheduled_image()

if __name__ == "__main__":
    main()
