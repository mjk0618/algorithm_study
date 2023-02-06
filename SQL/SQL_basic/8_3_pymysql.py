from tkinter import *
from tkinter import messagebox

''' 
#### tkinter 기본
root = Tk()
root.title('혼공 GUI 연습')
root.geometry('400x200')

label1 = Label(root, text = '혼공 SQL은')
label2 = Label(root, text = '쉽습니다', font = ('궁서체', 30), bg = 'blue', fg = 'yellow')

label1.pack()
label2.pack()

root.mainloop()
'''

'''
#### Button 구현
def clickButton() :
    messagebox.showinfo('버튼 클릭', '버튼을 눌렀습니다.')

root = Tk()
root.geometry('200x200')

button1 = Button(root, text = '여기를 클릭하세요', fg = 'red', bg = 'yellow', command = clickButton)
button1.pack(expand = 1)

root.mainloop()
'''

''' 
#### 위젯 정렬 및 여백 
root = Tk()
button1 = Button(root, text = '혼공1')
button2 = Button(root, text = '혼공2')
button3 = Button(root, text = '혼공3')

button1.pack(side = TOP, fill = X, padx = 10, pady = 10)
button2.pack(side = TOP, fill = X, padx = 10, pady = 10)
button3.pack(side = TOP, fill = X, padx = 10, pady = 10)

root.mainloop()
'''

#### 프레임, 엔트리, 리스트박스
root = Tk()
root.geometry('200x250')
upFrame = Frame(root)
upFrame.pack()
downFrame = Frame(root)
downFrame.pack()

editBox = Entry(upFrame, width = 10)
editBox.pack(padx = 20, pady = 20)

listbox = Listbox(downFrame, bg = 'yellow')
listbox.pack()

listbox.insert(END, '하나')
listbox.insert(END, '둘')
listbox.insert(END, '셋')

root.mainloop()