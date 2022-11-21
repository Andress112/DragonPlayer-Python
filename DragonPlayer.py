import pygame
from pygame import mixer
import sys
import os
import threading
import time
from tkinter import filedialog

# Initializing the Modules 

pygame.init()
mixer.init()

# Setting the Rezolution

Whidth_Normal = 300
Height_Normal = 500
Whidth_Slime = 400
Height_Slime = 70

# Loading Data Images

Logo = pygame.image.load("Data\Images\Logo\Small Logo.png")

# Setting the Windou parameters

Screen = pygame.display.set_mode((Whidth_Normal,Height_Normal))
pygame.display.set_caption("DragonPlayer")
pygame.display.set_icon(Logo)

# Colors

Gray = (160,160,160)
Black = (0,0,0)


# Making the Startup funcion and Variables

Starting_Volume = 0.5
Current_Volume = Starting_Volume
Music_Loaded = []
Music_Loaded_dir = []
Music_Paused = True
No_Music_detected = False
def Startup():
    global Music_Loaded
    global Starting_Volume
    global No_Music_detected

    # Cheching the files

    with open('Data/Settings/Loaded Songs.txt', 'r', encoding="utf-8") as file:
        file.seek(0)
        line = file.readline()
        print(line)
    if line != 'Music Loaded :\n':
        with open('Data/Settings/Loaded Songs.txt', 'w', encoding="utf-8") as file:
            file.seek(0)
            file.write('Music Loaded :\n')
        with open('Data/Settings/Loaded Folders.txt', 'w', encoding="utf-8") as file:
            file.seek(0)
            file.write('Music Directorys Loaded :\n')
        
    with open('Data/Settings/Loaded Folders.txt', 'r', encoding="utf-8") as file:
        file.seek(0)
        line = file.readline()
    if line != 'Music Directorys Loaded :\n':
        with open('Data/Settings/Loaded Folders.txt', 'w', encoding="utf-8") as file:
            file.seek(0)
            file.write('Music Directorys Loaded :\n')
        with open('Data/Settings/Loaded Songs.txt', 'w', encoding="utf-8") as file:
            file.seek(0)
            file.write('Music Loaded :\n')


    # Loadint the music
    with open('Data/Settings/Loaded Songs.txt', 'r', encoding="utf-8") as file:
        for i in file.readlines():
            file.seek(0)
            Music_Loaded.append(i.rstrip('\n'))
        try:
            Music_Loaded.pop(0)
        except:
            No_Music_detected = True
            print('Ther is no Music Loaded !')

    # Loadint the already loaded directorys
    with open('Data/Settings/Loaded Folders.txt', 'r', encoding="utf-8") as file:
        for i in file.readlines():
            file.seek(0)
            Music_Loaded_dir.append(i.rstrip('\n'))
        try:
            Music_Loaded_dir.pop(0)
        except:
            print('Ther is no Directorys already loaded !')
    
    # Playing the first song
    
    if len(Music_Loaded) >= 1:
        print('10')
        mixer.music.load(Music_Loaded[0])
        mixer.music.play()
        mixer.music.pause()
        mixer.music.set_volume(Starting_Volume)
    else:
        print('No Music Loaded')
        pass



# Declaring all the funcions

# Exiting the app

def Exit_App():
    sys.exit()

# Adding a new Muzic Folder to the directoy

def Add_Muzic_to_File():
    global Music_Loaded_dir
    global Music_Loaded
    try:
        Muzic_dir = filedialog.askdirectory(title='Select muzic folder')
        if Muzic_dir in Music_Loaded_dir:
            print('This directory is already loaded !')
            return
        else:
            Music_Loaded_dir.append(Muzic_dir)
            Muzic_dir_Music_list = os.listdir(Muzic_dir)
    except:
        return
    Muzic_to_be_saved = []
    for i in Muzic_dir_Music_list:
        Muzic_to_be_saved.append(f'{Muzic_dir}/{i}')
    with open('Data/Settings/Loaded Songs.txt', 'a', encoding="utf-8") as file:
        for i in Muzic_to_be_saved:
            file.write(i)
            file.write('\n')
            Music_Loaded.append(i)
    No_Music_detected = False
    if No_Music_detected == False:
        Load_Song(0)
    with open('Data/Settings/Loaded Folders.txt', 'a', encoding="utf-8") as file:
            file.seek(0)
            file.write(Muzic_dir)
            file.write('\n')

# Loading a song

def Load_Song(Song_positon):
    global Music_Paused
    mixer.music.load(Music_Loaded[Song_positon])
    mixer.music.play()
    if Music_Paused == True:
        mixer.music.pause()


# play or pouse a song

def Play():
    global Music_Paused
    if Music_Paused == True:
        mixer.music.unpause()
        Music_Paused = False
    else:
        mixer.music.pause()
        Music_Paused = True

# The Main Loop

def Player():
    global Screen
    while True :

        # Looking for events

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit_App()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    Screen = pygame.display.set_mode((Whidth_Slime,Height_Slime))
                    Player_Small()
                if event.key == pygame.K_o:
                    Add_Muzic_to_File()
                if event.key == pygame.K_k:
                    Play()

    
        # Filling the Screen With a color

        Screen.fill(Gray)

        # Updating The Screen

        pygame.display.update()

# The Small Player Loop

def Player_Small():
    global Screen
    while True :

        # Looking for events

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit_App()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    Screen = pygame.display.set_mode((Whidth_Normal,Height_Normal))
                    Player()
    
        # Filling the Screen With a color

        Screen.fill(Black)

        # Updating The Screen

        pygame.display.update()


# Calling the first Game loop and startup function

Startup()
Player()