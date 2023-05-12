import customtkinter as ctk
from time import strftime
import datetime

ctk.set_appearance_mode('dark')
ctk.set_appearance_mode('default')

#display labels
def display_labels():
    global date_lable, time_frame
    date_lable= ctk.CTkLabel(window, font=font1)
    date_lable.pack()
    
    time_frame= ctk.CTkLabel(window, font=font2, text_color='cyan')
    time_frame.pack(padx=20, pady=(5,15))
    

#display date
def showing_date():
    text= strftime('%A, %d, %b, %Y')
    date_lable.configure(text=text)
    

#display time
def showing_time():
    text2= strftime('%I:%M:%S %p')
    time_frame.configure(text=text2)
    time_frame.after(1000, showing_time)
    
def display_all():
    display_labels()
    showing_date()
    showing_time()

if __name__ =='__main__':
    window = ctk.CTk()
    window.title('Digital Clock Designed by Samson')
    window.geometry('450x100')
    window.resizable(0,0)
    
    font1=('montserat', 14, 'bold')
    font2=('sea-dog outline', 40)
    
    display_all()
    
    
    
    window.mainloop()