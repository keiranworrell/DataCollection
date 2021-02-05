import csv
import tkinter as tk
from tkinter import ttk
from functools import partial  
from os import path

def friendlyLink(c1, c2):
    char1 = (c1.get())
    char2 = (c2.get())
    linkAdded=False
    for edge in edges:
        if ((edge[0] == char1) and (edge[1] == char2) and (edge[4] == 'Friendly')) or ((edge[1] == char1) and (edge[0] == char2) and (edge[4] == 'Friendly')):
            edge[3]=edge[3]+1
            linkAdded = True
            break
    if (not linkAdded):
        edges.append([char1, char2, 'undirected', 1, 'Friendly'])
    char1Present=False
    char2Present=False
    for node in nodes:
        if (node[1] == char1):
            char1Present=True
        elif (node[1] == char2):
            char2Present=True
        if (char1Present and char2Present):
            break
    if (not char1Present):
        print("Warning: {} not in nodes.csv".format(char1))
    if (not char2Present):
        print("Warning: {} not in nodes.csv".format(char2))

def hostileLink(c1, c2):
    char1 = (c1.get())
    char2 = (c2.get())
    linkAdded=False
    for edge in edges:
        if ((edge[0] == char1) and (edge[1] == char2) and (edge[4] == 'Hostile')) or ((edge[1] == char1) and (edge[0] == char2) and (edge[4] == 'Hostile')):
            edge[3]=edge[3]-1
            linkAdded = True
            break
    if (not linkAdded):
        edges.append([char1, char2, 'undirected', -1, 'Hostile'])
    char1Present=False
    char2Present=False
    for node in nodes:
        if (node[1] == char1):
            char1Present=True
        elif (node[1] == char2):
            char2Present=True
        if (char1Present and char2Present):
            break
    if (not char1Present):
        print("Warning: {} not in nodes.csv".format(char1))
    if (not char2Present):
        print("Warning: {} not in nodes.csv".format(char2))

def newNode(char, pn, gen):
    character = (char.get())
    pageNum = (pn.get())
    gender = (gen.get())
    existingChar=False
    for node in nodes:
        if (node[1] == character):
            print("{} already in nodes list".format(character))
            existingChar=True
            break
    if (not existingChar):
        if (len(nodes) == 1):
            id=1
        else:
            id=nodes[-1][0]+1
        nodes.append([id, character, pageNum, gender])

def saveFile():
    with open(nodes_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(nodes)
    with open(edges_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(edges)

function = int(input("Data Collection (1) or Network Analysis (2)?\n"))

# nodes_path = input("Path to nodes.csv (enclose path in \" marks) : ")
# edges_path = input("Path to edges.csv (enclose path in \" marks) : ")

if (path.exists(nodes_path)):
    with open(nodes_path, 'r') as f:
        reader = csv.reader(f)
        nodes = list(reader)
else:
    nodes=[['ID', 'Name', 'Page introduced', 'Gender']]

if (path.exists(edges_path)):
    with open(edges_path, 'r') as f:
        reader = csv.reader(f)
        edges = list(reader)
else:
    edges=[['Source', 'Target', 'Type', 'Weight', 'Friendly/Hostile']]

# If csv files exist but are empty, populate with headings
if (len(nodes)<1):
    nodes=[['ID', 'Name', 'Page introduced', 'Gender']]
if (len(edges)<1):
    edges=[['Source', 'Target', 'Type', 'Weight', 'Friendly/Hostile']]

if (function == 1):
    # Start GUI to collect data and add nodes/edges to lists
    print("Starting data collection UI")

    # Create window with tabs
    root = tk.Tk()
    root.title("Data Collection")
    tabControl = ttk.Notebook(root)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='Record interaction')
    tabControl.add(tab2, text='Record character')

    # Populate interaction tab
    char1 = tk.StringVar()  
    char2 = tk.StringVar()  

    ttk.Label(tab1, text="Character 1").grid(column=0, row=0, padx=30, pady=10)
    c1 = ttk.Entry(tab1, textvariable=char1).grid(column=0, row=1, padx=30, pady=10)

    ttk.Label(tab1, text="Character 2").grid(column=2, row=0, padx=30, pady=10)
    c2 = ttk.Entry(tab1, textvariable=char2).grid(column=2, row=1, padx=30, pady=10)

    callFriendly = partial(friendlyLink, char1, char2)
    callHostile = partial(hostileLink, char1, char2)
    friendly = ttk.Button(tab1, text = "Create friendly link", command = callFriendly).grid(column=0, row=2, padx=30, pady=20)
    hostile = ttk.Button(tab1, text = "Create hostile link", command = callHostile).grid(column=2, row=2, padx=30, pady=20)

    save = ttk.Button(tab1, text = "Save CSV file", command = saveFile).grid(column=1, row=3, padx=10, pady=10)

    #Populate character tab
    name = tk.StringVar()
    page = tk.StringVar()
    gender = tk.StringVar()

    ttk.Label(tab2, text="Character Name: ").grid(column=0, row=0, padx=10, pady=10)
    charName= ttk.Entry(tab2, textvariable=name).grid(column=2, row=0, padx=10, pady=10)

    ttk.Label(tab2, text="Page first appear on: ").grid(column=0, row=1, padx=10, pady=10)
    charName= ttk.Entry(tab2, textvariable=page).grid(column=2, row=1, padx=10, pady=10)

    M = ttk.Radiobutton(tab2, text="Male", variable=gender, value="M").grid(column=0, row=2, padx=20, pady=20)
    F = ttk.Radiobutton(tab2, text="Female", variable=gender, value="F").grid(column=1, row=2, padx=20, pady=20)
    unknown = ttk.Radiobutton(tab2, text="Unknown", variable=gender, value="").grid(column=2, row=2, padx=20, pady=20)

    callNewNode = partial(newNode, name, page, gender)
    add = ttk.Button(tab2, text="Add character", command=callNewNode).grid(column=1, row=3, padx=20, pady=20)

    tabControl.pack(expand=1, fill="both")

    root.mainloop()
elif (function == 2):
    # Generate the network from nodes and edges lists
    print("Generating network")
    
