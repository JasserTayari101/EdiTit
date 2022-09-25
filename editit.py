import tkinter as tk

root=tk.Tk()
root.title("JasserEditor")

#devide the frame into two rows
root.rowconfigure(0,minsize=50)
root.rowconfigure(1,weight=1,minsize=550)
#make a single expandable column
root.columnconfigure(0,weight=1,minsize=800)

#create and position the title bar that will hold the file name
title_bar=tk.Frame(root,bg="#6f46cf")
title_bar.grid(row=0,column=0,sticky="nsew")
#Add initial file name to unknown.txt
tk.Label(title_bar,text="unknown.txt",bg="#6f46cf",fg="#cdc5de",font=("Hack",25)).grid(row=0,column=0,sticky="w")

rest_box=tk.Frame(root,bg="red")
rest_box.grid(row=1,column=0,sticky="nsew")
#devide rest_box into two columns 1)file opener and save as and 2)text editor
rest_box.rowconfigure(0,weight=1,minsize=550)
rest_box.columnconfigure(0,weight=0,minsize=100)
rest_box.columnconfigure(1,weight=1,minsize=500)
#create buttons frame
buttons_frm=tk.Frame(rest_box,bg="yellow")
buttons_frm.grid(row=0,column=0,sticky="nsew")

butn1=tk.Button(buttons_frm,text="Open")
butn1.pack(padx=2,pady=10)

def re_save():
    f=open(file_name,"w")
    f.write(text_edt.get("1.0",tk.END))
    f.close()


def save_prepare():
    def file_save():
        import os
        global file_name
        file_name=entry.get()
        if not file_name:
            file_name=default_file_name
        if os.path.exists(file_name):
            tk.Label(frame,text=f"'{file_name}' already exists!",fg="red").grid(row=1,column=0)
        else:
            f=open(file_name,"w")
            f.write(text_edt.get("1.0",tk.END))
            f.close()
            tk.Label(title_bar,text=file_name,bg="#6f46cf",fg="#cdc5de",font=("Hack",25)).grid(row=0,column=0,sticky="w")
            tk.Button(buttons_frm,text="Save",command=re_save).pack(padx=2,pady=10)
            window2.destroy()
    window2=tk.Tk()
    frame=tk.Frame(window2)
    frame.pack()
    frame.rowconfigure([0,1],weight=1,minsize=50)
    frame.columnconfigure([0,1,2],weight=1,minsize=75)
    
    label=tk.Label(frame,text="Enter file name:")
    label.grid(row=0,column=0)
    
    entry=tk.Entry(frame)
    entry.grid(row=0,column=1)
    entry.insert(0,default_file_name)
    
    save_btn=tk.Button(frame,text="Save",command=file_save)
    save_btn.grid(row=0,column=2)

butn2=tk.Button(buttons_frm,text="Save as",command=save_prepare)
butn2.pack(padx=2)

#create text editor frame
text_edt=tk.Text(rest_box,bg="green",fg="white")
text_edt.grid(row=0,column=1,sticky="nsew")

default_file_name="unknown.txt"



if __name__ == "__main__":
  root.mainloop()
