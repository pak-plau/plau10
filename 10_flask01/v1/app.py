# Clyde 'Thluffy' Sinclair
# SoftDev -- Rona Ed.
# Oct 2020

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

# unlike version 0, version 1 does not print “__name__”.
# It will, however, still print “No hablo queso!” on the local host webpage.
