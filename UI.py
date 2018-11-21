import module_manager
module_manager.review()
from tkinter import *
from image_util import *
import tkinter.ttk as ttk


'''
button1 = tkinter.button(text="Join Us")
entry_field = tk.Entry()

def phrase_generator():
    phrases =["Hello,","What's up,","Welcome back,"]
    name = str(entry1().get())
    return phrases[random.randint(0,4)] + name
    
def phrase_display():
    greeting = phrase_generator()
    
    greeting_display = tk.Text(master=window,height=,width=)
    
button2 = Button(text="Go",command=)'''

'''
def entrystyle():
    data = open("pic.dat").read()
    global s1, s2
    s1 = PhotoImage("search1", data=data, format="gif -index 0")
    s2 = PhotoImage("search2", data=data, format="gif -index 1")
    style = ttk.Style()
    style.element_create("Search.field", "image", "search1",
        ("focus", "search2"), border=[22, 7, 14], sticky="ew")
    style.layout("Search.entry", [
        ("Search.field", {"sticky": "nswe", "border": 1, "children":
            [("Entry.padding", {"sticky": "nswe", "children":
                [("Entry.textarea", {"sticky": "nswe"})]
            })]
        })]
    )
    style.configure("Search.entry", background="#b2b2b2")

if __name__ == '__main__':
    root = Tk()
    root.configure(background="#b2b2b2")
    entrystyle()
    e1 = ttk.Entry(root, style="Search.entry", width=20)
    e1.pack()
    root.mainloop()'''

def init(data):
    data.cx = data.width//2
    data.cy = data.height//2
    data.input = ""
    data.logo = PhotoImage(file="octopedia_logo.gif")
    data.mode = "homeScreen" 
    data.searchBarLeftX = data.width//3
    data.searchBarRightX = data.width*2//3
    data.searchBarTopY = data.height//2
    data.searchBarBottomY = data.height//2 + data.height//10
    data.LogInLeftX = 18/20*data.width
    data.LogInRightX = 19/20*data.width
    data.LogInTopY = 1/20*data.height
    data.LogInBottomY = 1/20*data.height + 1/40*data.width
    
def clickLogIn(event,data):
    return data.LogInLeftX <= event.x <=  data.LogInRightX and data.LogInTopY <=\
    event.y <= data.LogInBottomY
        
def mousePressed(event, data):        
    # in homeScreen & click "Log in" -> go to registration page
    if data.mode == "homeScreen" and clickLogIn(event,data):
        data.mode = "login"
    
    # in registration page & log in -> user account page
    pass

def keyPressed(event, data):
    # in homescreen & "enter" -> send request to chatbot
    if data.mode == "homeScreen" and event.keysym == "Enter":
        pass
    pass
    
def promptForQuery(data):
    '''
    canvas.create_text(data.searchBarLeftX+(data.searchBarRightX-data.searchBarLeftX)/2,\
    data.searchBarTopY+(data.searchBarBottomY-data.searchBarTopY)/2,text="Ask me anything",\
    fill="purple1",font="Palatino 10 bold")'''
    data.input = input()

def timerFired(data):
    pass
    '''
    if data.mode == "homeScreen":
        if len(data.input)>0:
            pass # draw IM
        else : 
            promptForQuery(data)
            canvas.create_line(data.searchBarLeftX,data.searchBarTopY,\
            data.searchBarLeftX,data.searchBarBottomY)'''
    
def drawLogo(canvas,data):
    canvas.create_image(data.cx,data.cy-100,image=data.logo)

def drawSearchBox(canvas,data):
    canvas.create_rectangle(data.searchBarLeftX,data.searchBarTopY,\
data.searchBarRightX,data.searchBarBottomY,fill="white",outline="purple1",width=5)
    
def drawLogInButton(canvas,data):
    canvas.create_rectangle(data.LogInLeftX,data.LogInTopY,data.LogInRightX,\
    data.LogInBottomY,fill="white",outline="purple1",width=1)
    canvas.create_text(data.LogInLeftX+(data.LogInRightX-data.LogInLeftX)/2,\
    data.LogInTopY+(data.LogInBottomY-data.LogInTopY)/2,text="Log in",\
    fill="purple1",font="Palatino 10 bold")
    
def drawIM(canvas,data):
    canvas.create_rectangle(data.searchBarLeftX,data.searchBarBottomY,\
data.searchBarRightX,2*data.searchBarBottomY-data.searchBarTopY,\
fill="white",outline="purple1",width=5)

def redrawAll(canvas, data):
    drawLogo(canvas,data)
    if data.mode == "homeScreen":
        canvas.create_text(data.width//10,data.height//10,text="Ask Octopus",\
        fill="purple1",font="Palatino 25 bold")
        drawLogo(canvas,data)
        drawSearchBox(canvas,data)
        drawLogInButton(canvas,data)
        canvas.create_line(data.searchBarLeftX+10,data.searchBarTopY,\
            data.searchBarLeftX+10,data.searchBarBottomY)
        #entrystyle()
        if len(data.input)>0:
            drawIM(canvas,data)
    elif data.mode == "login":
        pass
    elif data.mode == "UserAccount":
        pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1000, 500)