import time 
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}") 
    sound_file = "17.AlarmClock/alarmsound.mp3"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        # checks to see if the times are the same
        if current_time == alarm_time:
            print("WAKE UP!")
            is_running = False

            # uses pygame to load and play the sound
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            # this makes the sound play for the entire song
            while pygame.mixer.music.get_busy():
                time.sleep(1)

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)