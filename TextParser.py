import tkinter as tk
from tkinter.filedialog import askopenfile 
#sets main_filepath to the path of the text file.
def choose_file_function():
    global main_filepath
    main_filepath = askopenfile()
    main_filepath=main_filepath.name

    #This button is used to refresh the main text file.
    refresh_file_button=tk.Button(root, text = "*REFRESH*",font=("Fixedsys",13),bg="#458BC6",command = refresh_function)
    refresh_file_button.place(rely=.04,relx=.46) #change relx and rely to change position of button.

    #This button is used to refresh the main text file.
    refresh_file_button=tk.Button(root, text = "CHOOSE KEYWORDS",font=("Fixedsys",13),bg="#458BC6",command = choose_keywords_function)
    refresh_file_button.place(rely=.04,relx=.54) #change relx and rely to change position of button.

    #This button is used to analyze the main text file.
    analyze_file_button=tk.Button(root, text = "*ANALYZE*",font=("Fixedsys",13),bg="#458BC6",command = analyze_file)
    analyze_file_button.place(rely=.09,relx=.4) #change relx and rely to change position of button.

    #This button is used to analyze the main text file.
    analyze_keywords_button=tk.Button(root, text = "ANALYZE FOR \nKEYWORDS",font=("Fixedsys",13),bg="#458BC6",command = find_keywords)
    analyze_keywords_button.place(rely=.09,relx=.5) #change relx and rely to change position of button.


    return

#refreshes the text box displaying the main text file.
def refresh_function():
    #insert code
    return

#sets keyword_path to the path of the keywords file.
def choose_keywords_function():
    global keywords_path
    #insert code
    return

#This function analyzes the text file for desired stats.
def analyze_file():
    
    if(main_filepath!=""):
        #insert code
        return
    
#This function finds sentences with given keywords. 
def find_keywords():

    if(keywords_path!=""):
        #insert code
        return


#Windows size
HEIGHT=768
WIDTH=1366
main_filepath=""
keywords_path=""

#Initializing main window for the GUI.
root=tk.Tk()
#root.attributes('-fullscreen', True) #Uncomment to make application fullscreen.
canvas=tk.Canvas(root,width=WIDTH,height=HEIGHT,bg="#FBFBFB")
canvas.pack()

#This button is used to select the main text file.
choose_file_button=tk.Button(root, text = "CHOOSE FILE",font=("Fixedsys",13),bg="#458BC6",command = choose_file_function)
choose_file_button.place(rely=.04,relx=.365) #change relx and rely to change position of button.

#This is the main textbox where all the results are displayed. Use textbox_content.set(context) to change contents of the textbox.
textbox_content = tk.StringVar()
textbox_content.set("Please choose a file and press *ANALYZE*.") #Similarly use .set to change contents.
textbox = tk.Entry(root,textvariable=textbox_content, state='disabled', font=("Fixedsys",13))
textbox.place(relx=.01,rely=.17,relwidth=.98,relheight=.82)

tk.mainloop()