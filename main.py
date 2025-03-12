import os
import tkinter as tk
import webbrowser
import json
import subprocess

FILENAME = "data.json"


def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return {}


def save_data():
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)


data = load_data()


def search_the_item_amazon():
    query_amazon = search.get()
    if query_amazon:
        url_amazon = f"https://www.amazon.com/s?k={query_amazon.replace(' ', '+')}"
        webbrowser.open(url_amazon)


def search_the_item_flipkart():
    flip_query = search.get()
    if flip_query:
        url_flip = f"https://www.flipkart.com/search?q={flip_query.replace(' ', '+')}"
        webbrowser.open(url_flip)


def open_calculator():
    os.system("calc")


def shop_item_add_entry():
    name = shopping_add_entry.get()
    price = price_add_entry.get()
    url = url_add_entry.get()

    if name and price and url:
        data[name] = {"price": price, "url": url}
        save_data()
        shopping_add_entry.delete(0, tk.END)
        price_add_entry.delete(0, tk.END)
        url_add_entry.delete(0, tk.END)
        result_label.config(text="Item added!", fg="green")
    else:
        result_label.config(text="Enter name, price, and URL!", fg="red")


def shopping_search_item():
    query = shopping_search_entry.get()

    if query in data:
        item_price = data[query]["price"]
        item_url = data[query]["url"]

        result_label.config(text=f"Price: ₹{item_price}\nURL: ")
        url_label.config(text="Click here", fg="purple", cursor="hand2")
        url_label.bind("<Button-1>", lambda e: webbrowser.open(item_url))
    else:
        result_label.config(text="Not found!", fg="red")
        url_label.config(text="")


def search_all_sites():
    query = search_entry.get()
    if query:
        url_flip = f"https://www.flipkart.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(url_flip)
        url_amazon = f"https://www.amazon.com/s?k={query.replace(' ', '+')}"
        webbrowser.open(url_amazon)
        url_meesho = f"https://www.meesho.com/search?q={query.replace(' ', '%20')}"
        webbrowser.open(url_meesho)


def delete_search_entry():
    search_entry.delete(0, tk.END)


def delete_item():
    item_name = delete_entry.get()
    if item_name in data:
        del data[item_name]
        save_data()
        result_label.config(text=f"Deleted: {item_name}", fg="red")
        delete_entry.delete(0, tk.END)
    else:
        result_label.config(text="Item not found!", fg="red")


def show_cart():
    if not data:
        result_label.config(text="Cart is empty!", fg="blue")
    else:
        cart_items = "\n".join([f"{key}: ₹{value['price']}" for key, value in data.items()])
        result_label.config(text=cart_items, fg="blue")

def delete_shopping_entry():
    shopping_search_box.delete(0,tk.END)
    url_label.config(text="", fg="black", cursor="")
    result_label.config(text="")

def search_on_meesho():
    query_meesho=search_entry.get()
    if query_meesho:
        url_meesho:str= f"https://www.meesho.com/search?q={query_meesho.replace(' ', '%20')}"
        webbrowser.open(url_meesho)

def open_discount_calculator():
    subprocess.Popen(["python","new.py"])

window = tk.Tk()
window.geometry("500x500")
window.title("Shopping Assistant")
window.resizable(False,False)

search = tk.StringVar()
shopping_search_entry = tk.StringVar()
url_entry = tk.StringVar()
delete_entry_var = tk.StringVar()

tk.Label(window, text="Search Item:").grid(row=0, column=0)
search_entry = tk.Entry(window, textvariable=search)
search_entry.grid(row=0, column=1)

amazon_button = tk.Button(window, text="Search on Amazon", command=search_the_item_amazon)
flipkart_button = tk.Button(window, text="Search on Flipkart", command=search_the_item_flipkart)
amazon_button.grid(row=1, column=0, padx=5, pady=5)
flipkart_button.grid(row=1, column=1, padx=5, pady=5)

all_button = tk.Button(window, text="Search on all sites", command=search_all_sites)
all_button.grid(row=2, column=0)

calculator_button = tk.Button(window, text="Open Calculator", command=open_calculator)
calculator_button.grid(row=2, column=1)

delete_search = tk.Button(window, text="Delete Search", command=delete_search_entry)
delete_search.grid(row=0, column=2)

tk.Label(window, text="Item Name:").grid(row=3, column=0)
shopping_add_entry = tk.Entry(window)
shopping_add_entry.grid(row=3, column=1)

tk.Label(window, text="Price:").grid(row=4, column=0)
price_add_entry = tk.Entry(window)
price_add_entry.grid(row=4, column=1)

tk.Label(window, text="Product URL:").grid(row=5, column=0)
url_add_entry = tk.Entry(window, textvariable=url_entry)
url_add_entry.grid(row=5, column=1)

shopping_list_add = tk.Button(window, text="Add Item", command=shop_item_add_entry)
shopping_list_add.grid(row=6, column=0, columnspan=2, pady=5)

tk.Label(window, text="Search Shopping Item:").grid(row=7, column=0)
shopping_search_box = tk.Entry(window, textvariable=shopping_search_entry)
shopping_search_box.grid(row=7, column=1)

search_button = tk.Button(window, text="Search", command=shopping_search_item)
search_button.grid(row=7, column=2)

tk.Label(window, text="Delete Item:").grid(row=8, column=0)
delete_entry = tk.Entry(window, textvariable=delete_entry_var)
delete_entry.grid(row=8, column=1)

delete_button = tk.Button(window, text="Delete", command=delete_item)
delete_button.grid(row=8, column=2)

show_cart_button = tk.Button(window, text="Show Cart", command=show_cart)
show_cart_button.grid(row=9, column=0, columnspan=2, pady=5)

result_label = tk.Label(window, text="", fg="black", justify="left")
result_label.grid(row=10, column=0, columnspan=2, pady=5)

url_label = tk.Label(window, text="", fg="blue", cursor="hand2")
url_label.grid(row=11, column=0, columnspan=2)

delete_button_shopping_entry = tk.Button(window, text="Delete search", command=delete_shopping_entry)
delete_button_shopping_entry.grid(row=7, column=3)

meesho_button=tk.Button(window,text="Search on Meesho",command=search_on_meesho)
meesho_button.grid(row=1,column=2)

discount_calculator=tk.Button(window,text="Discount Calculator",command=open_discount_calculator)
discount_calculator.grid(row=2,column=2)

window.mainloop()
