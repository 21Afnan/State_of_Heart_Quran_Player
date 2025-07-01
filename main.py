from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pygame
from PIL import Image,ImageTk
import time
class Quran():
    def __init__(self):
        self.window=Tk()
        self.window.title("Quran Player")
        self.window.geometry("600x450")
        self.window.resizable(False,False)
        self.window.iconbitmap("window_icon.ico")
        self.mood_surah_mapping = {
            "Sad": "93-Ad-Duha.mp3",
            "Anxious": "94-As-Sharh.mp3",
            "Grateful": "55-Ar-Rahman.mp3",
            "Calm": "18-Al-Kahf.mp3",
            "Lost": "01-Al-Fatiha.mp3",
            "Motivated": "103-Al-Asr.mp3",
            "Angry": "03-Aal-e-Imran.mp3",
            "Lonely": "19-Maryam.mp3"
        }
        self.create_page1()
        self.current_pos =0
        self.window.mainloop()
    def create_page1(self):
        try:
            img_path="quran.png"
            background_img=Image.open(img_path)
            backgrnd_img=background_img.resize((600,450))
            self.bg=ImageTk.PhotoImage(backgrnd_img)
            Label( self.window,image=self.bg).place(relwidth=1,relheight=1)
        except Exception as e:
            messagebox.showerror("Error",f"Could not load background image {e}")
        self.Label1=Label(self.window,text="   ٱلرَّحِيمِ ٱلرَّحْمَٰنِ ٱللَّٰه بِسْمِ",bg="#12242d",fg="White",font=("Arial Rounded MT Bold",30))
        self.Label1.grid(row=0,column=0,columnspan=3,padx=60,pady=40)
        self.label=Label( self.window,text=" عَلَيْكُمْ ٱلسَّلَامُ",bg="#12242d",fg="White",font=("Arial Rounded MT Bold",30))
        self.label.grid(row=1,column=0,padx=190,pady=30)
        self.button=Button( self.window,text="START",bg="#12242d",command=self.buttonclicked,fg="White",font=("Arial Rounded MT Bold",30),width=8)
        self.button.grid(row=2,column=0,pady=20)


    def buttonclicked(self):
        self.label.grid_forget()
        self.button.grid_forget()
        self.create_page2()

    def create_page2(self):
        try:
            img_path = "quran.png"
            background_img = Image.open(img_path)
            backgrnd_img = background_img.resize((600, 450))
            self.bg = ImageTk.PhotoImage(backgrnd_img)
            Label(self.window, image=self.bg).place(relwidth=1, relheight=1)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load background image {e}")
        Label(self.window,text="State of Heart Quran Player",bg="#12242d",fg="White",font=("Arial Rounded MT Bold",30)).grid(row=0,columnspan=3,padx=25,pady=5)
        moods=[ 'Sad', 'Anxious', 'Grateful', 'Calm',
             'Lost',
            'Motivated', 'Angry', 'Lonely']
        self.mood_var = StringVar()
        combobox=ttk.Combobox(self.window,values=moods,width=40,font=("Arial",15),state="readonly",textvariable= self.mood_var)
        combobox.set("Choose your state of heart")
        combobox.grid(row=1,column=0,columnspan=3)
        self.surah_label = Label(self.window, text="", bg="#12242d", fg="White", font=("Arial Rounded MT Bold", 20))
        self.surah_label.grid(row=3, column=0, columnspan=5, pady=20)
        self.load_icons()
    def back_button_pressed(self):
        try:
            pygame.mixer.music.stop()
        except pygame.error:
            pass  # I
        for widget in self.window.winfo_children():
            widget.destroy()
        self.create_page1()

    def load_icons(self):
        try:
            self.play_icon = Image.open("pause_icon.png")
            self.play_icon = self.play_icon.resize((30, 30))
            self.play_img = ImageTk.PhotoImage(self.play_icon)

            self.pause_icon = Image.open("play_icon.png")
            self.pause_icon = self.pause_icon.resize((30, 30))
            self.pause_img = ImageTk.PhotoImage(self.pause_icon)

            self.replay_icon = Image.open("replay_icon.png")
            self.replay_icon = self.replay_icon.resize((30, 30))
            self.replay_img = ImageTk.PhotoImage(self.replay_icon)

            Button(self.window, text="", image=self.play_img, command=self.PlayAudio, bg="white").grid(row=2,column=0,padx=10,pady=30)
            Button(self.window, text="", image=self.pause_img,command=self.PauseAudio, bg="white").grid(row=2,column=1, padx=12, pady=30)
            Button(self.window, text="", image=self.replay_img, command=self.ReplayAudio,bg="white").grid(row=2, column=2, padx=10, pady=15)
            Button(self.window, text="Back", bg="#12242d", command=self.back_button_pressed, fg="White",
                   font=("Arial Rounded MT Bold", 25)).grid(row=4, column=1, padx=10, pady=20)
        except Exception as e:
                 messagebox.showerror("Error", f"Could not load icons: {e}")
    def PlayAudio(self):
        selected_mood = self.mood_var.get().strip().capitalize()
        if selected_mood in self.mood_surah_mapping:
            try:
                pygame.mixer.init()
                audio_file = self.mood_surah_mapping[selected_mood]
                parts = audio_file.split('-')
                surah_name = ' '.join(parts[1:]).replace('.mp3', '')
                full_surah_name = "Surah " + surah_name
                # Remove the previous Surah name label if it exists
                if self.surah_label:
                    self.surah_label.grid_forget()

                # Display the Surah name
                self.surah_label = Label(self.window, text=full_surah_name, font=("Arial Rounded MT Bold", 25),bg="#12242d",fg="white")
                self.surah_label.grid(row=3, column=1,padx=20,pady=10)
                pygame.mixer.music.load(audio_file)
                pygame.mixer.music.play(loops=0, start=self.current_pos / 1000)
            except Exception as e:
                 messagebox.showerror("Error", f"Could not play audio: {e}")

        else:
               self.show_error_message("This is a wrong option you chose!")

    def PauseAudio(self):
        self.current_pos = pygame.mixer.music.get_pos()
        pygame.mixer.music.pause()

    def ReplayAudio(self):
        pygame.mixer.music.play(loops=0, start=0.0)



Quran()

