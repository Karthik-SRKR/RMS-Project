# Creating a dataframe for orders manipulation
import pandas as pd
from openpyxl import * 

orders = pd.read_excel("RMS_db.xlsx")
cols = orders.columns




##########################################################################################




# Insert function for orders dataset
def insert_order(orders,i1,i2,i3,i4):
    orders = pd.read_excel("RMS_db.xlsx")
    # func to append the new records
    def append_row_to_excel(new_row, excel_path):
        df_excel = pd.read_excel(excel_path)
        result_df = pd.concat([df_excel, new_row], ignore_index=True)
        result_df.to_excel(excel_path, index=False)
    if len(orders["Ord_id"])==0 :
        new_order = pd.DataFrame([{"Ord_id":1, "Name_of_the_customer":i1, "Item_ordered":i2, "Quantity_of_items":i3, 
                                    "Price_of_order":i4, "Ord_date":pd.to_datetime('today').normalize().strftime('%d-%m-%Y')}])
        new_order.to_excel("RMS_db.xlsx", index=False)
    elif i1 in pd.Series(orders["Name_of_the_customer"]).values :
        new_order = pd.DataFrame([{"Ord_id":orders["Ord_id"][orders["Name_of_the_customer"]==i1].reset_index(drop=True)[0], "Name_of_the_customer":i1, "Item_ordered":i2,
                                    "Quantity_of_items":i3, "Price_of_order":i4, "Ord_date":pd.to_datetime('today').normalize().strftime('%d-%m-%Y')}])
        append_row_to_excel(new_order,"RMS_db.xlsx")
    else:
        l = pd.Series(orders['Ord_id']).values.max()
        new_order = pd.DataFrame([{"Ord_id":l+1, "Name_of_the_customer":i1, "Item_ordered":i2, "Quantity_of_items":i3,
                                    "Price_of_order":i4, "Ord_date":pd.to_datetime('today').normalize().strftime('%d-%m-%Y')}])
        append_row_to_excel(new_order,"RMS_db.xlsx")
    
    

def display_ord_id(i1):
    orders_dummy = pd.read_excel("RMS_db.xlsx")
    ord_id = orders_dummy.loc[(orders_dummy["Name_of_the_customer"]==i1), : ].reset_index(drop=True)["Ord_id"][0]
    ord_id_txt = 'Your assigned Order-id is :- "' + str(ord_id) + '"'
    return ord_id_txt


# Update function for ordered_items in dataset
def update_order(orders,i1,i2,i3,i4,i5):
    orders = pd.read_excel("RMS_db.xlsx")
    upd_condition = (orders["Ord_id"]==i1) & (orders["Item_ordered"]==i2)
    orders.loc[upd_condition, ["Item_ordered","Quantity_of_items","Price_of_order"]] = [i3,i4,i5]
    orders.to_excel("RMS_db.xlsx", index=False)
    orders = pd.read_excel("RMS_db.xlsx")


# Fetch function for orders in the function
def fetch_order(orders,i1):
    orders = pd.read_excel("RMS_db.xlsx")
    req_df = orders.loc[(orders["Ord_id"]==i1), : ].reset_index().drop('index', axis=1)
    return req_df


# Generate bill function
def generate_bill(orders, i1):
    orders = pd.read_excel("RMS_db.xlsx")
    bill_amount = orders.loc[(orders["Ord_id"]==i1), : ].reset_index(drop=True)["Price_of_order"].sum()
    bill_amount_txt = 'Your bill amount is :- "' + str(bill_amount) + '/-"'
    return bill_amount_txt











##################################################################################################







from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title("RMS")

Label(window, text="Restaurant Management System (RMS)", fg="red", font=("arial bold",35)).pack()

items_frame = Frame(window,bg='sky blue')
items_frame.pack(side="left", fill="both", expand=True)
orders_frame = Frame(window,bg='light green')
orders_frame.pack(side="right", fill="both", expand=True)

# Naming the items_frame
lb1 = Label(items_frame, text="Items-available", bg="blue", fg="white", font=("arial bold",20), width=40)
lb1.grid(column=0,row=0, padx=20, pady=5)

# creating the items-list
items_list = ["Chicken_Biryani   -350",
              "Mutton_biryani    -400",
              "Mixed_Mugalai     -450",
              "Egg_FriedRice     -250",
              "Chicken_FriedRice -300",
              "Veg_FriedRice     -250",
              "Chicken_Curry     -200",
              "Mutton_Curry      -250",
              "Paneer_Curry      -180",
              "Bagara_Rice       - 60",
              "Special_Curd_Rice -120",
              "IceCream          - 80",
              "DryFriut_Juice    -120",
              "Coke              - 40",
              "Water_bottle      - 20"]
for i,j in enumerate(items_list):
    item_lb = Label(items_frame, text=f"{j}", bg="black", fg="white", font=("Lucida",12), width=22)
    item_lb.grid(column=0, row=i+1, padx=22)


# Naming the orders_frame
lb2 = Label(orders_frame, text="Order-Manipulations Portal", bg="green", fg="white", font=("arial bold",20), width=40)
lb2.grid(columnspan=2,row=0, padx=20, pady=5)

def main_tab():

    orders = pd.read_excel("RMS_db.xlsx")

    # Used to clear the old window contents
    def destroy_main_func():
        ord_lb1.destroy()
        btn1.destroy()
        ord_lb2.destroy()
        btn2.destroy()
        ord_lb3.destroy()
        btn3.destroy()
        ord_lb4.destroy()
        btn4.destroy()

    # Button-click events with individual tabs
    # add_order_tab function
    def add_order_tab():
        destroy_main_func()
        cust_name_lb = Label(orders_frame, text="Customer Name :-", font=("arial",12))
        cust_name_lb.grid(column=0,row=1, padx=(120,0),pady=5)
        cust_name_entry = Entry(orders_frame, width=20)
        cust_name_entry.grid(column=1,row=1, padx=(0,100),pady=5)
        item_lb = Label(orders_frame, text="Item Ordered :-", font=("arial",12))
        item_lb.grid(column=0,row=2, padx=(120,0),pady=5)
        item_combo = ttk.Combobox(orders_frame, width=20)
        item_combo['values'] = tuple(items_list)
        item_combo.grid(column=1,row=2, padx=(0,100),pady=5)
        items_quantity_lb = Label(orders_frame, text="Quantity of items :-", font=("arial",12))
        items_quantity_lb.grid(column=0,row=3, padx=(120,0),pady=5)
        items_quantity_combo = ttk.Combobox(orders_frame, width=20)
        items_quantity_combo['values'] = (1,2,3,4,5,6,7,8,9,10)
        items_quantity_combo.grid(column=1,row=3, padx=(0,100),pady=5)
        
        def destroy_contents():
                # now clearing the components in add_order_frame
                cust_name_lb.destroy()
                cust_name_entry.destroy()
                item_lb.destroy()
                item_combo.destroy()
                items_quantity_lb.destroy()
                items_quantity_combo.destroy()
                back_btn1.destroy()
                submit_btn.destroy()
                main_tab()

        def destroy_add_order_func():
            # assigning filled values into temp-variables
            cust_name = cust_name_entry.get()
            item_name = item_combo.get()
            items_quantity = items_quantity_combo.get()

            if cust_name or item_name or items_quantity != '' :
                items_quantity = int(items_quantity)
                if len(item_name[-3:len(item_name)].lstrip()) == (len(item_name[-3:len(item_name)])-1) :
                    price = float(item_name[-3:len(item_name)].lstrip()) * float(items_quantity)
                else :
                    price = float(item_name[-3:len(item_name)]) * float(items_quantity)
                    
                # Insert filled data into the dataset here by using above created function
                insert_order(orders, cust_name, item_name, items_quantity, price)
    
                # Order added msg pop-up function
                def add_order_popup():
                    messagebox.showinfo("add order","Order added Successfully !")
                add_order_popup()
    
                # Display Order_id 
                txt_id = display_ord_id(cust_name)
                disp_id = Label(orders_frame, text=txt_id, bg="light green",fg="red", font=("Lucida",12))
                disp_id.grid(columnspan=2,row=5, padx=(120,0),pady=5)
    
                def destroy_add_contents():
                    disp_id.destroy()
                    ok_btn.destroy()
                    destroy_contents()
                     
                ok_btn = Button(orders_frame, text="OK", bg="purple", fg="white", font=("Times New Roman",12), borderwidth=3, activebackground="gray", command=destroy_add_contents)
                ok_btn.grid(column=1,row=6, padx=(0,100),pady=5)
            else:
                def isEmpty_popup():
                    response = messagebox.showinfo("add Order","Please enter a valid Customer Details !!!")
                    if response=="OK" :
                        add_order_tab()
                isEmpty_popup()
        

        back_btn1 = Button(orders_frame, text="back", bg="purple", fg="white", font=("Times New Roman",12), borderwidth=3, activebackground="gray", command=destroy_contents)
        back_btn1.grid(column=1,row=4, padx=(150,20),pady=5)

        submit_btn = Button(orders_frame, text="Submit", bg="purple", fg="white", font=("Times New Roman",12), borderwidth=3, activebackground="gray", command=destroy_add_order_func)
        submit_btn.grid(column=1,row=4, padx=(0,100),pady=5)

    # update_order_tab function    
    def update_order_tab():
        destroy_main_func()
        ord_id_lb = Label(orders_frame, text="Order Id :-", font=("arial",12))
        ord_id_lb.grid(column=0,row=1, padx=(120,0),pady=5)
        ord_id_entry = Entry(orders_frame, width=20)
        ord_id_entry.grid(column=1,row=1, padx=(0,140),pady=5)

        def destroy_contents():
            ord_id_lb.destroy()
            ord_id_entry.destroy()
            back_btn2.destroy()
            fetch_updates.destroy()
            main_tab()

        def access_updates():
            ord_id = ord_id_entry.get()
            if ord_id !='' :
                ord_id = int(ord_id)
                if ord_id in pd.Series(orders["Ord_id"]).values:
                    ordered_items = []
                    for i in orders["Item_ordered"][orders['Ord_id']==ord_id] :
                        ordered_items.append(i)
                    sep_1 = Label(orders_frame, text="------------------------------------------------",bg="light green", fg="black")
                    sep_1.grid(columnspan=2,row=3, pady=5)
                    old_item_lb = Label(orders_frame, text="Old item :-", font=("arial",12))
                    old_item_lb.grid(column=0,row=4, padx=(120,0),pady=5)
                    old_item_combo = ttk.Combobox(orders_frame, width=20)
                    old_item_combo['values'] = tuple(ordered_items)
                    old_item_combo.grid(column=1,row=4, padx=(0,140),pady=5)
                    new_item_lb = Label(orders_frame, text="New item :-", font=("arial",12))
                    new_item_lb.grid(column=0,row=5, padx=(120,0),pady=5)
                    new_item_combo = ttk.Combobox(orders_frame, width=20)
                    new_item_combo['values'] = tuple(items_list)
                    new_item_combo.grid(column=1,row=5, padx=(0,140),pady=5)
                    new_items_quantity_lb = Label(orders_frame, text="New Quantity of items :-", font=("arial",12))
                    new_items_quantity_lb.grid(column=0,row=6, padx=(120,0),pady=5)
                    new_items_quantity_combo = ttk.Combobox(orders_frame, width=20)
                    new_items_quantity_combo['values'] = (1,2,3,4,5,6,7,8,9,10)
                    new_items_quantity_combo.grid(column=1,row=6, padx=(0,140),pady=5)

                    def destroy_update_order_func():
                        if old_item_combo.get() != '':
                            # assigning filled values into temp-variables
                            old_item_name = old_item_combo.get()
                            new_item_name = new_item_combo.get()
                            new_items_quantity = int(new_items_quantity_combo.get())
                            if len(new_item_name[-3:len(new_item_name)].lstrip()) == (len(new_item_name[-3:len(new_item_name)])-1) :
                                price = float(new_item_name[-3:len(new_item_name)].lstrip()) * float(new_items_quantity)
                            else :
                                price = float(new_item_name[-3:len(new_item_name)]) * float(new_items_quantity)

                            # update the data in dataset by update_order function
                            update_order(orders, ord_id, old_item_name, new_item_name, new_items_quantity, price)

                            # Order updated pop-up msg
                            def update_order_popup():
                                messagebox.showinfo("update order","Order updated Successfully !")
                            update_order_popup()

                            # now clearing the components in the update_order_tab
                            sep_1.destroy()
                            old_item_lb.destroy()
                            old_item_combo.destroy()
                            new_item_lb.destroy()
                            new_item_combo.destroy()
                            new_items_quantity_lb.destroy()
                            new_items_quantity_combo.destroy()
                            update_btn.destroy()
                            destroy_contents()
                            
                        else:
                            def isEmpty_popup():
                                response = messagebox.showinfo("Orders","Please enter a valid Items to change !!!")
                                if response=="OK" :
                                    update_order_tab()
                            isEmpty_popup()

                    update_btn = Button(orders_frame, text="update", bg="purple", fg="white", font=("Times New Roman",12), borderwidth=3, activebackground="gray", command=destroy_update_order_func)
                    update_btn.grid(column=1,row=7, padx=(0,140),pady=5)
                else:
                    def notFound_popup():
                        response = messagebox.showinfo("Orders"," Order-Id not found in the orders list \n Please enter a valid Order Id !!!")
                        if response=="OK" :
                            update_order_tab()
                    notFound_popup()
            else:
                def isEmpty_popup():
                    response = messagebox.showinfo("Orders","Please enter a valid Order Id !!!")
                    if response=="OK" :
                        update_order_tab()
                isEmpty_popup()

        back_btn2 = Button(orders_frame, text="back", bg="purple", fg="white", font=("Times New Roman",12), borderwidth=3, activebackground="gray", command=destroy_contents)
        back_btn2.grid(column=1,row=2, padx=(140,20),pady=5)

        fetch_updates = Button(orders_frame, text="fetch", bg="purple", fg="white", font=("Times New Roman",12), borderwidth=3, activebackground="gray", command=access_updates)
        fetch_updates.grid(column=1,row=2, padx=(0,140),pady=5)
        
    # fetch_order_tab function
    def fetch_order_tab():
        destroy_main_func()
        ord_id_lb = Label(orders_frame, text="Order Id :-", font=("arial",12))
        ord_id_lb.grid(column=0,row=1, padx=(120,0),pady=5)
        ord_id_entry = Entry(orders_frame, width=20)
        ord_id_entry.grid(column=1,row=1, padx=(0,140),pady=5)

        def destroy_contents():
            ord_id_lb.destroy()
            ord_id_entry.destroy()
            back_btn3.destroy()
            fetch_btn.destroy()
            main_tab()

        def display_orders():
            ord_id = ord_id_entry.get()
            if ord_id !='' :
                ord_id = int(ord_id)
                if ord_id in pd.Series(orders["Ord_id"]).values:

                    # fetch orders by using fetch_order function
                    fetched_df = fetch_order(orders, ord_id)
                    sep_2 = Label(orders_frame, text="--------------------------------------------------------------",bg="light green", fg="black", font=("arial",12))
                    sep_2.grid(columnspan=2,row=3, padx=(120,0), pady=5) 
                    fetched_cust_name = Label(orders_frame, text=f"Name of the Customer :- {fetched_df["Name_of_the_customer"][0]}",bg="light green", fg="black", font=("arial",12))
                    fetched_cust_name.grid(columnspan=2,row=4, padx=(120,0), pady=5)
                    fetched_ord_id = Label(orders_frame, text=f"Order ID :- {fetched_df["Ord_id"][0]}",bg="light green", fg="black", font=("arial",12))
                    fetched_ord_id.grid(columnspan=2,row=5, padx=(120,0), pady=5)
                    fetched_ord_list = {}
                    for i,j,k,l in zip(range(6,len(fetched_df)+6),fetched_df["Item_ordered"],fetched_df["Quantity_of_items"],fetched_df["Price_of_order"]):
                        fetched_ord_list[i] = Label(orders_frame, text=f"{j} ------ {k} =====> {l} Rs.",bg="black",fg="white", width=40, font=("Lucida",11))
                        fetched_ord_list[i].grid(columnspan=2,row=i, padx=22)

                    ith_row = len(fetched_df)+6
                    sep_3 = Label(orders_frame, text="--------------------------------------------------------------",bg="light green", fg="black", font=("arial",12))
                    sep_3.grid(columnspan=2,row=ith_row, padx=(120,0), pady=5)
                    text3 = Label(orders_frame, text="*** Click done! if you fetched the required orders ***",bg="light green", fg="black", font=("arial",12))
                    text3.grid(columnspan=2,row=ith_row+1, padx=(120,0), pady=5)
                    

                    def destroy_fetch_order_func():
                        sep_2.destroy()
                        fetched_cust_name.destroy()
                        fetched_ord_id.destroy()
                        for i in range(6,len(fetched_df)+6):
                            fetched_ord_list[i].destroy()
                        sep_3.destroy()
                        text3.destroy()
                        ok_btn.destroy()
                        destroy_contents()

                    ok_btn = Button(orders_frame, text="Done!", bg="purple", fg="white", font=("Times New Roman",12), borderwidth=3, activebackground="gray", command=destroy_fetch_order_func)
                    ok_btn.grid(column=1,row=ith_row+2, padx=(0,140),pady=5)
                else:
                    def notFound_popup():
                        response = messagebox.showinfo("Orders"," Order-Id not found in the orders list \n Please enter a valid Order Id !!!")
                        if response=="OK" :
                            update_order_tab()
                    notFound_popup()

            else:
                def isEmpty_popup():
                    response = messagebox.showinfo("Orders","Please enter a valid Order Id !!!")
                    if response=="OK" :
                        fetch_order_tab()
                isEmpty_popup()

        back_btn3 = Button(orders_frame, text="back", bg="purple", fg="white", font=("Times New Roman",12), borderwidth=3, activebackground="gray", command=destroy_contents)
        back_btn3.grid(column=1,row=2, padx=(140,20),pady=5)

        fetch_btn = Button(orders_frame, text="fetch", bg="purple", fg="white", font=("Times New Roman",12), borderwidth=3, activebackground="gray", command=display_orders)
        fetch_btn.grid(column=1,row=2, padx=(0,140),pady=5)
    
    # Gen_bill_tab function
    def gen_bill_tab():
        destroy_main_func()
        ord_id_lb = Label(orders_frame, text="Order id :-", font=("arial",12))
        ord_id_lb.grid(column=0,row=1, padx=(120,0),pady=5)
        ord_id_entry = Entry(orders_frame, width=20)
        ord_id_entry.grid(column=1,row=1, padx=(0,140),pady=5)

        def destroy_contents():
            ord_id_lb.destroy()
            ord_id_entry.destroy()
            back_btn4.destroy()
            gen_bill_btn.destroy()
            main_tab()

        def destroy_gen_bill_func():
            ord_id = ord_id_entry.get()
            if ord_id != '' :
                ord_id = int(ord_id)
                if ord_id in pd.Series(orders["Ord_id"]).values:
                    sep_3 = Label(orders_frame, text="----------------------------------------------------",bg="light green", fg="black")
                    sep_3.grid(columnspan=2,row=3, padx=(120,0), pady=5)
                    text3 = Label(orders_frame, text="*** Click DONE! if paid the bill amount ***",bg="light green", fg="black", font=("arial",12))
                    text3.grid(columnspan=2,row=4, padx=(120,0), pady=5)

                    # generate and display bill amount by using generate_bill function
                    bill_text = generate_bill(orders, ord_id)
                    disp_bill = Label(orders_frame, text=bill_text, bg="light green",fg="red", font=("arial",12))
                    disp_bill.grid(columnspan=2,row=5, padx=(120,0), pady=5)

                    def destroy_bill_contents():
                        sep_3.destroy()
                        text3.destroy()
                        disp_bill.destroy()
                        ok_btn.destroy()
                        destroy_contents()

                    ok_btn = Button(orders_frame, text="Done!", bg="purple", fg="white", font=("Times New Roman",12), borderwidth=3, activebackground="gray", command=destroy_bill_contents)
                    ok_btn.grid(column=1,row=6, padx=(0,140),pady=5)
                else:
                    def notFound_popup():
                        response = messagebox.showinfo("Orders"," Order-Id not found in the orders list \n Please enter a valid Order Id !!!")
                        if response=="OK" :
                            update_order_tab()
                    notFound_popup()
            else:
                def isEmpty_popup():
                    response = messagebox.showinfo("Bill","Please enter a valid Order Id !!!")
                    if response=="OK" :
                        fetch_order_tab()
                isEmpty_popup()

        back_btn4 = Button(orders_frame, text="back", bg="purple", fg="white", font=("Times New Roman",12), borderwidth=3, activebackground="gray", command=destroy_contents)
        back_btn4.grid(column=1,row=2, padx=(140,20),pady=5)

        gen_bill_btn = Button(orders_frame, text="genarate", bg="purple", fg="white", font=("Times New Roman",12), borderwidth=3, activebackground="gray", command=destroy_gen_bill_func)
        gen_bill_btn.grid(column=1,row=2, padx=(0,140),pady=5)

    # Creating Order manipulation buttons in orders_frame
    ord_lb1 = Label(orders_frame, text="1.  For adding new orders use this button", font=("Times New Roman",12))
    ord_lb1.grid(column=0,row=1, sticky="w", padx=20)
    btn1 = Button(orders_frame, text="Add Order", bg="purple", fg="white", font=("Times New Roman",12), borderwidth=3, activebackground="gray", command=add_order_tab)
    btn1.grid(column=0,row=2, padx=100,pady=5 )

    ord_lb2 = Label(orders_frame, text="2.  For updating the current order details use this button", font=("Times New Roman",12))
    ord_lb2.grid(column=0,row=3, sticky="w", padx=20)
    btn2 = Button(orders_frame, text="Update Order", bg="purple", fg="white", font=("Times New Roman",12), borderwidth=3, activebackground="gray", command=update_order_tab)
    btn2.grid(column=0,row=4, padx=100,pady=5)

    ord_lb3 = Label(orders_frame, text="3.  For Fetching Customer Order details use this button", font=("Times New Roman",12))
    ord_lb3.grid(column=0,row=5, sticky="w", padx=20)
    btn3 = Button(orders_frame, text="Fetch Order", bg="purple", fg="white", font=("Times New Roman",12), borderwidth=3, activebackground="gray", command=fetch_order_tab)
    btn3.grid(column=0,row=6, padx=100,pady=5)

    ord_lb4 = Label(orders_frame, text="4.  For generating bill use this button", font=("Times New Roman",12))
    ord_lb4.grid(column=0,row=7, sticky="w", padx=20)
    btn4 = Button(orders_frame, text="Generate bill", bg="purple", fg="white", font=("Times New Roman",12), borderwidth=3, activebackground="gray", command=gen_bill_tab)
    btn4.grid(column=0,row=8, padx=100,pady=5)


main_tab()

window.mainloop()
