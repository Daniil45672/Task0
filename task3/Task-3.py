import http.client
import json
from tkinter import *
import sys
import os
z=[]
from tkinter import Tk,Button

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
root = Tk()
root.title("Сovid")
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "e36cf147d2msh773e180e52d7742p1f4ad1jsnd148121bd4cf",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
res = conn.getresponse()
data = res.read()
corona = data.decode("utf-8")
json = json.loads(corona)
country1 = "India"
country2 = "Turkey"
country3 = "Iran"
country4 = "Indonesia"
country5 = "Philippines"
text = Text(width=500, height=500,  font=("Times New Roman", 20, "italic"))
label = Label(text="Name")
entry = Entry()
label.pack()
entry.pack()
text.pack()

label = Label(text="India \n Turkey \n Iran \n Indonesia \n Philippines").place(x=610, y=45)

def sorting():
  z = entry.get()
  if z == country1:
      for i in range(0,1):
          text.insert('1.0', list(json[i].items())[14])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[12])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[10])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[2])
          text.insert('1.0', '\n')
  elif z == country2:
      for i in range(1,2):
          text.insert('1.0', list(json[i].items())[14])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[12])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[10])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[2])
          text.insert('1.0', '\n')
  elif z == country3:
      for i in range(2,3):
          text.insert('1.0', list(json[i].items())[14])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[12])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[10])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[2])
          text.insert('1.0', '\n')
  elif z == country4:
      for i in range(3,4):
          text.insert('1.0', list(json[i].items())[14])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[12])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[10])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[2])
          text.insert('1.0', '\n')
  elif z == country5:
      for i in range(4,5):
          text.insert('1.0', list(json[i].items())[14])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[12])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[10])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[2])
          text.insert('1.0', '\n')
Button(root, text="Enter", font=("Times New Roman", 20, "italic"), command=sorting, width=24, height=1,).place(x = 900, y = 0)
Button(root, text="Restart", font=("Times New Roman", 20, "italic"), command=restart_program, fg='#ffffff', bg='#CD5C5C',width=24, height=1,).place(x = 0, y = 0)
root.mainloop()
