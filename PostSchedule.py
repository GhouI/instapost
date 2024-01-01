from datetime import datetime

class Node:
    def __init__(self, description, time, next=None):
        self.description = description
        self.time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")  # Convert string to datetime
        self.next = next

class PostSchedule:
    def __init__(self):
        self.head = None

    def add_post(self, description, time):
        new_post = Node(description, time)
        if not self.head:
            self.head = new_post
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_post

    def get_next_post_time(self):
        current = self.head
        next_post_time = None
        while current:
            if not next_post_time or current.time < next_post_time:
                next_post_time = current.time
            current = current.next
        return next_post_time

    def display_schedule(self):
        current = self.head
        while current:
            print(f"Description: {current.description}, Time: {current.time}")
            current = current.next
