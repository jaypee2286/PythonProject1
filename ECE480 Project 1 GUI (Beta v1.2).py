######################################################################
## Jorge Camacho                                                    ##
## John Paul Canlas                                                 ##
## Allen Khachikian                                                 ##
## Leonard Mendoza                                                  ##
## Justin Shen                                                      ##
##                                                                  ##
## ECE480 Spring 2013                                               ##
## Prof. Chandra                                                    ##
##                                                                  ##
## Project #1 - Disk Head Movement Program                          ##
##                                                                  ##
## This program simulates hard disk head movement given a           ##
##  set of requests. It can simulate movement for six different     ##
##  algorithms: FIFO, STSF, SCAN, CSCAN, LOOK, & CLOOK              ##
######################################################################

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import ntpath

### calculate() FUNCTION START
def calculate():
    selection = ("You selected the option " +str(combobox.current()+1))
    sel = combobox.current() + 1
    data = list(lst) #copy lst to perserve fifo structure
    total = 0 #total movements throughout list
    del path[:] #clear path[] list for new calculation
    del mov[:] #clear mov[] list for new calculation
    
    if sel == 1: #FIFO
        print("You have selected FIFO.")
        for i in range(len(data)-1):
            x = data[i] #current pos. for this pass
            print("Here is the current position: " + str(x))
            y = abs(x-data[i+1]) #find difference between current pos. and next pos.           
            total += y #add the difference to our total
            mov.append(y) #add current difference to mov-list
            path.append(data[i]) #add current request to path
            print("Here is the distance moved: " + str(y))
        print("Here is the ending position: " + str(data[len(data)-1]))
        mov.append(total) # add total of differences to mov-list
        path.append(data[i+1]) #add final request to path
        print("Here is the total distance moved: " + str(total))
        print("Here is the movement list: " + str(mov))

    elif sel == 2: #STSF
        start = data[0] #save the start point before sorting
        end = data[len(data)-1] #save the end point before sorting
        data.sort() #sort the list
        print("Sorted list: " + str(data))
        pos = data.index(start) #save the current pos. of the start point
        pos2 = pos+1 #save the current pos. of the start point
        pos3 = pos-1 #save the current pos. of the start point
        print("You have selected STSF.")
        for j in range(len(data)-1):
            right_difference = abs(data[pos] - data[pos2]) #find difference to the right of the current pos
            left_difference = abs(data[pos] - data[pos3]) #find difference to the left of the current pos
            print("Current Position: " + str(data[pos]))
            path.append(data[pos])

            if left_difference <= right_difference: #move left of current pos.
                total += left_difference #add left difference total
                mov.append(left_difference) #add current difference to mov-list
                pos = pos3 #pos is equal to pos3 which remains unchanged until condition is met
                pos3 -= 1 #decrement pos3 for new view
                print("Here is the distance moved: " + str(left_difference))
                
            elif right_difference <= left_difference: #move right of current pos.
                total += right_difference #add right difference total
                mov.append(right_difference) #add current difference to mov-list
                pos = pos2 #pos is equal to pos2 which remains unchanged until conidition is met
                pos2 += 1 #increment pos3 for new view
                print("Here is the distance moved: " + str(right_difference))

        path.append(data[pos])
        mov.append(total)
        print("Here is the ending position: " + str(data[pos]))
        print("Here is the total distance moved: " + str(total))
        print("Here is the movement list: " + str(mov))
        
    elif sel == 3: #SCAN
        print("You have selected SCAN.")
        start = data[0] #save the starting point before sorting
        end = data[len(data)-1] #record what is at the end
        data.sort()
        data.insert(0,0) #insert a zero at the beginning
        pos = data.index(start) #save current pos. of starting point
        pos2 = pos #save current pos. of starting point
        print("Here is the starting position: " + str(data[pos]))
        print("Going down...")
        while pos > 0:
            print("Here is the current position: " +str(data[pos]))
            x = data[pos] #current pos.
            a = data[pos-1] #1 below current pos.
            y = abs(x-a) #find difference between positions
            path.append(data[pos]) #record path taken            
            total += y #add to total difference
            mov.append(y) #add current difference to mov-list
            print("Here is the distance moved: " + str(y))
            pos += -1 #decrement pos to find next set

        #print("\nNo more requests in this direction. Switching directions.\n")
        print("Currently at position: " + str(pos))
        print("Going up...")
        #total += data[pos2+1] #we've reached 0, now add to total difference
                              #from 0 to starting point+1
        print("Now at one after the original starting point.")
        while pos < (len(data)-1):
            print("Here is the current position: " +str(data[pos]))
            x = data[pos] #current pos.
            a = data[pos2+1]#1 above current pos.
            y = abs(x-a) #find difference
            path.append(data[pos]) #record path taken   
            total += y #add onto the total difference
            mov.append(y) #add current difference to mov-list
            print("Here is the distance moved: " + str(y))
            pos = pos2+1 #increment pos by 1
            pos2 += 1 # increment pos2 by 1
        
        path.append(data[pos])
        mov.append(total)            
        print("Here is the ending position: " + str(data[pos]))
        print("Here is the total distance moved: " + str(total))
        print("Here is the movement list: " + str(mov))
            
            
    elif sel == 4: #CSCAN
        print("You have selected CSCAN.")
        start = data[0] #save the starting point before sorting
        end = data[len(data)-1] #record what is at the end
        data.sort()
        data.insert(0,0) #insert a zero at the beginning
        pos = data.index(start) #current index pos. of starting point
        init = pos #current index pos. of starting point
        pos2 = len(data)-1 #index of the the end point
        print("Here is the starting position: " + str(data[pos]))
        print("Going down...")
        while pos > 0: #calcualte until we hit the start of the list
                print("Here is the current position: " +str(data[pos]))
                x = data[pos] #current pos.
                a = data[pos-1] #1 below current pos.
                y = abs(x-a) #differnce between current pos and 1 below
                path.append(data[pos]) #record path taken  
                total += y #add onto the total difference
                mov.append(y) #add current difference for this pass
                print("Here is the distance moved: " + str(y))
                pos += -1 #decrement pos. for next pass
        
        print("Currently at position: " + str(pos))
        path.append(pos)
        print("Going to the other end of the list...")
        total += data[pos2] #we've reached 0, now add to total difference
                                                #from 0 to end of the list
        mov.append(data[pos2]) #add overhead of moving one list to another
        print("Here is the distance moved: " + str(data[pos2]))
        while pos2 > init: #move from top to bottom before hitting starting point
                print("Here is the current position: " +str(data[pos2]))
                x = data[pos2] #current pos. 
                a = data[pos2-1] #1 below current pos 
                y = abs(x-a) #find the difference
                path.append(data[pos2]) #record path taken 
                total += y #add to the total difference
                mov.append(y) #add current difference for this pass
                print("Here is the distance moved: " + str(y))
                pos2 += -1 #decrement pos2
                
        print("Here is the ending position: " + str(data[pos]))
        path.append(data[pos])
        mov.append(total)
        print("Here is the total distance moved: " + str(total))
        print("Here is the movement list: " + str(mov))
            
    elif sel == 5: #LOOK
        print("You have selected LOOK AHEAD")
        start = data[0]
        end = data[len(data)-1]
        data.sort()
        pos = data.index(start)
        pos2 = pos
        print("Here is the starting position: " + str(data[pos]))
        print("Going up.\n")
        while pos < len(data)-1:
            x = data[pos]
            a = data[pos+1]
            y = abs(x-a)
            total += y
            mov.append(y)
            path.append(x)
            print("Moving to position: " + str(data[pos+1]))
            print("Here is the distance moved: " + str(y))
            pos += 1

        print("\nNo more requests in this direction. Switching directions.\n")

        while pos > 0:
            x = data[pos]
            a = data[pos2-1]
            y = abs(x-a)
            total += y
            mov.append(y)
            path.append(x)
            print("Moving to position: " + str(data[pos2-1]))
            print("Here is the distance moved: " + str(y))
            pos = pos2-1
            pos2 -= 1
                    
        print("\nNo more requests.\n")
        print("Here is the ending position: " + str(data[pos]))
        mov.append(total)
        path.append(data[pos])
        print("Here is the total distance moved: " + str(total))
        print("Here is the movement list: " + str(mov))

    elif sel == 6: #CLOOK
        print("You have selected CLOOK.")
        start = data[0] #save the starting point before sorting
        end = data[len(data)-1] #record what is at the end
        data.sort()
        print("Sorted list: " + str(data))
        pos = data.index(start) #current position of the starting point
        print("Here is the starting position: " + str(data[pos]))
        print("Going up...")
        while pos < len(data)-1:
            print("Here is the current position: " +str(data[pos]))
            x = data[pos]
            a = data[pos+1]
            y = abs(x-a)
            total += y #add onto the total time
            mov.append(y)
            path.append(data[pos])
            print("Here is the distance moved: " + str(y))
            pos += 1
            
        #print("\nNo more requests in this direction.\n")    
        print("Currently at position: " + str(data[pos]))
        path.append(data[pos])    
        print("Going to the first index...")
        pos = 0; #retract to the beginning of the list
        total += data[len(data)-1]-data[pos] #now at pos2+1
        mov.append(data[len(data)-1]-data[pos])
        print("Here is the distance moved: " + str(data[len(data)-1]-data[pos]))
        while pos+1 < data.index(start): #post+1 insures we dont revisit origin 
            print("Here is the current position: " +str(data[pos]))
            x = data[pos]
            a = data[pos+1]
            y = abs(x-a)
            total += y #add onto the total time
            mov.append(y)
            path.append(data[pos])
            print("Here is the distance moved: " + str(y))
            pos += 1
            
        print("Here is the ending position: " + str(data[pos]))
        mov.append(total)
        path.append(data[pos])
        print("Here is the total distance moved: " + str(total))    
        print("Here is the movement list: " + str(mov))
            
    else:
        messagebox.showinfo("Error", "You have not entered valid inputs.")

    ## ENABLE and clear all text boxes for editting
    text_Box1.config(state=NORMAL)
    text_Box2.config(state=NORMAL)
    text_Box3.config(state=NORMAL)
    text_Box1.delete(1.0, END)
    text_Box2.delete(1.0, END)
    text_Box3.delete(1.0, END)
    print("Here is the path list: " + str(path)) #print path list to console
    ## UPDATE text boxes 
    for i in range (len(path)-1):
        text_Box1.insert(INSERT, str(path[i]) + "-" + str(path[i+1]) + "\n")
    for j in range (len(mov)-1):
        text_Box2.insert(INSERT, str(mov[j]) + "\n")
    text_Box3.insert(INSERT, str(total))

    ## DISABLE all text boxes after updating to prevent user modification
    text_Box1.config(state=DISABLED)
    text_Box2.config(state=DISABLED)
    text_Box3.config(state=DISABLED)
    
# END calculate()

### browse() FUNCTION START
def browse():
    ## open up an explorer window to browse for file
    filename = filedialog.askopenfilename()
    ## display filename (without full path)
    label_FileName.config(text=ntpath.basename(filename))
    del lst[:] ## clear current LST
    
    ## try to read the file and check if the format is valid
    ## display error notification if it is invalid
    with open(filename,'r') as f:
        try:
            for line in f:
                for item in line.split(','): 
                    value = int(item,10)
                    lst.append(value)
            button_Calculate.config(state=NORMAL)
        except:
            messagebox.showinfo("Error", "Invalid file.")
            button_Calculate.config(state=DISABLED)            
    f.closed ## close file

    ## update REQUESTS box
    ## first enable the box, then update, then disable the box
    ##   to prevent user modification
    text_Box0.config(state=NORMAL)
    text_Box0.delete(1.0, END)
    for i in range (len(lst)):
        text_Box0.insert(INSERT, str(lst[i]) + "\n")
    text_Box0.config(state=DISABLED)
    
# END browse()


### help_instructions() function start
### this function calls a pop up message box that gives a brief
###  explanation of how to use the program
def help_instructions():
    messagebox.showinfo("Instructions", "This program shows a harddisk head movement "
                       "using various algorithms. Select a file using the BROWSE button."
                        "The file must be formatted in the followign way:\n"
                        "#, #, #, #\nThe disk head location requests must be separated by commas."
                        "After selecting a file, choose an algorithm from the dropdown box then"
                        "click the CALCULATE button. The data will display in the text boxes.")
# END help_instructions()


### help_about() function start
### this function calls a pop up message box that gives a brief
###  explanation about the program and it's creators
def help_about():
    messagebox.showinfo("About", "This program was created for Dr. Chandra in ECE480 at "
                        "Cal Poly Pomona Polytechnic University, Spring 2013 quarter.\n\n"
                        "Jorge Camacho\nJohn Paul Canlas\nAllen Khachikian\nLeonard Mendoza\nJustin Shen")
# END help_about



#########################################
#########################################
#### MAIN FUNCTION & GUI            #####
#########################################
#########################################

## create a GUI using Tk
root = Tk()

## add a frame to the GUI
## all widgets and objects will be put inside this frame
frame = ttk.Frame(root, height=400, width=400, padding="10 10 10 20")
frame.grid(row=0, column=0, sticky=(N, W, E, S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
root.title("ECE480 Project #1") # title of program

## NOTE: This GUI uses a grid formation to place all the widgets/objects.
         # The grid consists of rows and columns.
         # Each object is anchored to a spot or spots on the grid accordingly.

## define lists
lst = []    #holds the list of requests
data = []   #holds the data that we manipulate for calculations
path = []   #holds the path taken for a calculation
mov = []    #holds the distances moved for a calculation

## FILEMENU
## this is a basic filemenu
## users can open a file through this menu as well as
##  get instructions on how to use the program and also
##  a list of the creators
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open...", command=browse)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Instructions", command=help_instructions)
helpmenu.add_separator()
helpmenu.add_command(label="About", command=help_about)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

## algorithm selection box
## this holds the options for the different algorithms
combobox = ttk.Combobox(frame, state='readonly')
combobox['values'] = ('FIFO', 'STSF', 'SCAN', 'CSCAN', 'LOOK', 'CLOOK')
combobox.grid(row=1, column=1, columnspan=3, sticky=W)
label_combobox = Label(frame, anchor=W, justify=LEFT, text="Algorithm:")
label_combobox.grid(row=1, column=0, sticky=W)

## filename display box
## this displays a concatinated filename without the full path
label_FileName = Label(frame, width=20, anchor=W, bg="white", justify=LEFT, relief="ridge")
label_FileName.grid(row=0, column=1, columnspan=3, sticky=W)
label_Filename2 = Label(frame, anchor=W, justify=LEFT, text="Filename:")
label_Filename2.grid(row=0, column=0, sticky=W)

## BROWSE (for file) button
## call function browse() when clicked
button_Browse = Button(frame, text="BROWSE", command=browse) 
button_Browse.grid(row=0, column=4, sticky=W)

## CALCULATE button
## call function calculate() when clicked
button_Calculate = Button(frame, text="CALCULATE", command=calculate, state=DISABLED) 
button_Calculate.grid(row=1, column=4, sticky=W)

## REQUESTS label & text display box
## this displays the data read from the file containing
##  the list of requests
label_Box0 = Label(frame, text="Requests")
label_Box0.grid(row=2, column=0, sticky=N)
text_Box0 = Text(frame, height=10, width=7, state=DISABLED)
text_Box0.grid(row=3,column=0)

## PATH label & text display box
## this displays the order of requests/path taken of the head after calculation
label_Box1 = Label(frame, text="Path")
label_Box1.grid(row=2, column=1, sticky=N)
text_Box1 = Text(frame, height=10, width=7, state=DISABLED)
text_Box1.grid(row=3,column=1)

## DISTANCE (movement) label & text display box
## this displays the head movement distances
label_Box2 = Label(frame, text="Distance")
label_Box2.grid(row=2, column=2, sticky=N)
text_Box2 = Text(frame, height=10, width=7, state=DISABLED)
text_Box2.grid(row=3,column=2)

## TOTAL label & text display box
## this displays the total head distance movement
label_Box3 = Label(frame, text="Total")
label_Box3.grid(row=2, column=3, sticky=N)
text_Box3 = Text(frame, height=1, width=7, state=DISABLED)
text_Box3.grid(row=3,column=3, sticky=N)

root.mainloop()
