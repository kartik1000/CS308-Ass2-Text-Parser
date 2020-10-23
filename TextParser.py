import tkinter as tk
from tkinter.filedialog import askopenfile 
from tkinter import messagebox
import collections
import random
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

def getPlot(wordcount):
    sweetSpot=20
    sortedCount = sorted(wordcount.items(), key = lambda kv:(kv[1], kv[0]))
    N=len(sortedCount)

    # max
    maxCount=sortedCount[N-sweetSpot:N] # make it [0:N] to include all words
    random.shuffle(maxCount)
    words = [i[0] for i in maxCount]
    counts = [i[1] for i in maxCount]

    fig = Figure(figsize=(12,10))
    a = fig.add_subplot(111)
    a.bar(words, counts, width=0.4, color='orange')
    a.set_title ('Most occuring ' + str(sweetSpot) + ' words in the selected file with their counts', fontsize=12)
    a.set_ylabel('Count', fontsize=10)
    a.set_xlabel('Word', fontsize=10)
    a.set_xticklabels(words, rotation=50)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()
    canvas.draw()

#sets main_filepath to the path of the text file.
def choose_file_function():
    global main_filepath, file_chosen, textbox_content, textbox
    main_filepath = askopenfile()
    main_filepath=main_filepath.name
    try:
        ext = main_filepath.split('.')[-1]
        if ext=="txt":
            file_chosen = 1
            #This button is used to refresh the main text file.
            refresh_file_button=tk.Button(root, text = "*REFRESH*",font=("Fixedsys",13),bg="#458BC6",command = refresh_function)
            refresh_file_button.place(rely=.04,relx=.400) #change relx and rely to change position of button.
            
            #This button is used to refresh the main text file.
            refresh_file_button=tk.Button(root, text = "CHOOSE KEYWORDS",font=("Fixedsys",13),bg="#458BC6",command = choose_keywords_function)
            refresh_file_button.place(rely=.04,relx=.500) #change relx and rely to change position of button.
            
            #This button is used to analyze the main text file.
            analyze_file_button=tk.Button(root, text = "*ANALYZE*",font=("Fixedsys",13),bg="#458BC6",command = analyze_file)
            analyze_file_button.place(rely=.04,relx=.300) #change relx and rely to change position of button.
            
            #This button is used to analyze the main text file.
            analyze_keywords_button=tk.Button(root, text = "ANALYZE FOR \nKEYWORDS",font=("Fixedsys",13),bg="#458BC6",command = find_keywords)
            analyze_keywords_button.place(rely=.04,relx=.650) #change relx and rely to change position of button.
            textbox.destroy()
        else:
            messagebox.showwarning("File Upload Error!","Please Upload a valid text file!")
    except:
        messagebox.showwarning("File Upload Error!","Please Upload a valid text file!")
       

        return

#refreshes the text box displaying the main text file.
def refresh_function():
    analyze_file();
    return

#sets keyword_path to the path of the keywords file.
def choose_keywords_function():
    global keywords_path
    keywords_path = askopenfile()
    keywords_path = keywords_path.name
    print(keywords_path)
    return

#This function analyzes the text file for desired stats.
def analyze_file():
    print(main_filepath)
    file = open(main_filepath, encoding="utf8")
    a= file.read()
    # Stopwords
    stopwords = set(['he','she','the','is','are'])
    #stopwords = set(line.strip() for line in open('stopwords.txt'))
    stopwords = stopwords.union(set(['mr','mrs','one','two','said']))
    # Instantiate a dictionary, and for every word in the file, 
    # Add to the dictionary if it doesn't exist. If it does, increase the count.
    wordcount = {}
    # To eliminate duplicates, remember to split by punctuation, and use case demiliters.
    for word in a.lower().split():
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("â€œ","")
        word = word.replace("â€˜","")
        word = word.replace("*","")
        if word not in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1 
    # Print most common word
    n_print = 1
    display_string = "The most common word is "
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(n_print):
        display_string += str(word) + ": " + str(count) + "\n"
    
    display_string += "The least common word is "
    display_string += str(word_counter.most_common()[-1][0]) + ": " + str(word_counter.most_common()[-1][1])
    messagebox.showinfo("showinfo", display_string) 
    getPlot(wordcount) # may need to move up
    return

#This function finds sentences with given keywords. 
def find_keywords():

    if(keywords_path!=""):
        #preprocessing of main file.
        file = open(main_filepath, encoding="utf8")
        main_file=file.read()
        main_file=main_file.replace("\n","")
        main_file=main_file.split(".")
        
        #preprocessing of file containg keys.
        file_key = open(keywords_path, encoding="utf8")
        key_list= file_key.read()
        key_list=key_list.split("\n")
        
        # searching for keywords and adding them to a list
        sentences=[]
        for i in range(len(main_file)):
            for j in range(len(key_list)):
                if key_list[j] in main_file[i]:
                    sentences.append(main_file[i])
                    break
                    
        #displaying it on the dialog box
        display_string="The Sentence(s) that contain(s) atleast one keyword is/are :"
        for i in range(len(sentences)):
            display_string+="\n"
            display_string+=sentences[i]
        display_string+="\n"     
        messagebox.showinfo("showinfo", display_string)
        return


#Windows size
HEIGHT=300
WIDTH=1000
main_filepath=""
keywords_path=""
file_chosen = 0

#Initializing main window for the GUI.
root=tk.Tk()
#root.attributes('-fullscreen', True) #Uncomment to make application fullscreen.
canvas=tk.Canvas(root,width=WIDTH,height=HEIGHT,bg="#FBFBFB")
canvas.pack()

#This button is used to select the main text file.
choose_file_button=tk.Button(root, text = "CHOOSE FILE",font=("Fixedsys",13),bg="#458BC6",command = choose_file_function)
choose_file_button.place(rely=.04,relx=.200) #change relx and rely to change position of button.

#This is the main textbox where all the results are displayed. Use textbox_content.set(context) to change contents of the textbox.
textbox_content = tk.StringVar()
textbox_content.set("Please choose a file and press *ANALYZE*.") #Similarly use .set to change contents.
textbox = tk.Entry(root,textvariable=textbox_content, state='disabled', font=("Fixedsys",13))
textbox.place(relx=.01,rely=.17,relwidth=.98,relheight=.20)

tk.mainloop()
