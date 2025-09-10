from tkinter import *
from tkinter import ttk
import inventory_management as iv_m
from item import *

root = Tk()
root.title('Inventory Management')
width = 750
height = 750
root.geometry(f'{width}x{height}')

# Makes the table for the gui-------------------------------------------------------------------------------------------
set = ttk.Treeview(root)

set.pack()
set['columns'] = ('id', 'Name', 'Quantity', 'Price')
set.column("#0", width=0, stretch=NO)
set.column("id", anchor=CENTER, width=80)
set.column("Name", anchor=CENTER, width=80)
set.column("Quantity", anchor=CENTER, width=80)
set.column("Price", anchor=CENTER, width=80)
set.heading("#0", text="", anchor=CENTER)
set.heading("id", text="ID", anchor=CENTER)
set.heading("Name", text="Name", anchor=CENTER)
set.heading("Quantity", text="Quantity", anchor=CENTER)
set.heading("Price", text="Price", anchor=CENTER)

# data------------------------------------------------------------------------------------------------------------------
file_data = iv_m.read_from_file()
data = []
for item in file_data:
    data.append(item.fields_as_list())

count = 0 # global

for record in data:
    set.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]))
    count += 1

# make the input boxes for the user-------------------------------------------------------------------------------------
Input_frame = Frame(root)
Input_frame.pack()

name = Label(Input_frame, text="Name")
name.grid(row=0, column=1)

quantity = Label(Input_frame, text="Quantity")
quantity.grid(row=0, column=2)

price = Label(Input_frame, text="Price")
price.grid(row=0, column=3)

name_entry = Entry(Input_frame)
name_entry.grid(row=1, column=1)

quantity_entry = Entry(Input_frame)
quantity_entry.grid(row=1, column=2)

price_entry = Entry(Input_frame)
price_entry.grid(row=1, column=3)

# function for button and other thinks like when the window is closed---------------------------------------------------
def input_record():
    global count
    if name_entry.get() != '' and quantity_entry.get() != '' and price_entry.get() != '':
        set.insert(parent='', index='end', iid=count, text='', values=(count+1, name_entry.get(), quantity_entry.get(), price_entry.get()))
        file_data.append(Item(count+1, name_entry.get(), quantity_entry.get(), price_entry.get()))
        count += 1
        #id_entry.delete(0, END)
        name_entry.delete(0, END)
        quantity_entry.delete(0, END)
        price_entry.delete(0, END)

def delete_record():
    selected = set.selection()
    if selected:
        for item in selected:
            set.delete(item)
            file_data.pop(int(item[0]))

def update_record():
    selected = set.selection()
    if name_entry.get() != '' and quantity_entry.get() != '' and price_entry.get() != '':
        if selected:
            for item in selected:
                set.item(selected[0], values=(int(item[0])+1, name_entry.get(), quantity_entry.get(), price_entry.get()))
                file_data.insert(int(item[0]), Item(int(item[0])+1, name_entry.get(), quantity_entry.get(), price_entry.get()))
                file_data.pop(int(item[0])+1)

def save_items():
    iv_m.write_to_file(file_data)

def on_closing():
    save_items()
    root.destroy()

# buttons --------------------------------------------------------------------------------------------------------------
button_frame = Frame(root)
button_frame.pack()

add_item_button = Button(button_frame, text="Input Record", command=input_record)
add_item_button.pack(side=LEFT)

delete_item_button = Button(button_frame, text="Delete Record", command=delete_record)
delete_item_button.pack(side=LEFT)

update_item_button = Button(button_frame, text="Update Record", command=update_record)
update_item_button.pack(side=LEFT)

save_item_button = Button(button_frame, text="Save Record", command=save_items)
save_item_button.pack(side=LEFT)

# radio button ----------------------------------------------------------------------------------------------------------

radio_button_frame = Frame(root)
radio_button_frame.pack()

test1 = StringVar(value="")
test2 = StringVar(value='')

radio_button_1 = Radiobutton(radio_button_frame, text="test 1 option 1", variable=test1, value="test 1 option 1 is working")
radio_button_1.pack()
radio_button_2 = Radiobutton(radio_button_frame, text="test 1 option 2", variable=test1, value="test 1 option 2 is working")
radio_button_2.pack()
radio_button_3 = Radiobutton(radio_button_frame, text="test 2 option 1", variable=test2, value="test 2 option 1 is working")
radio_button_3.pack()
radio_button_4 = Radiobutton(radio_button_frame, text="test 2 option 2", variable=test2, value="test 2 option 2 is working")
radio_button_4.pack()

radio_1_label = Label(radio_button_frame, textvariable=test1, border=1, borderwidth=10, relief="groove")
radio_1_label.pack()
radio_2_label = Label(radio_button_frame, textvariable=test2, border=1, borderwidth=10, relief="groove")
radio_2_label.pack()


# check box ------------------------------------------------------------------------------------------------------------

check_frame = Frame(root)
check_frame.pack()

option1 = IntVar()
option2 = IntVar()
option3 = IntVar()


check_button_1 = Checkbutton(check_frame, text="Option 1", variable=option1)
check_button_1.pack()

check_button_2 = Checkbutton(check_frame, text="Option 2", variable=option2)
check_button_2.pack()

check_button_3 = Checkbutton(check_frame, text="Option 3", variable=option3)
check_button_3.pack()


def show_selection():
    result = []
    if option1.get():
        result.append("Option 1")
    if option2.get():
        result.append("Option 2")
    if option3.get():
        result.append("Option 3")
    label.config(text="Selected: " + ", ".join(result) if result else "Selected:None")


button = Button(root, text="Show Selection", command=show_selection)
button.pack()


label = Label(root, text="Selected: None")
label.pack()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
