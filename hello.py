from flask import Flask

#Beim ausführen wird der __name__ variable ein Name von Python zugewiesen. Wenn es sich um das Mainfile handelt,
#schreibt Python __name__ = __main__ , wenn nicht, dann ist __name__ == filename.py
#Durch Flask(__name__) rufen wir eigentlich mit Flask(__main__) auf

# If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as
# application or imported as module the name will be different ('__main__' versus the actual import name). This is
# needed so that Flask knows where to look for templates, static files, and so on. For more information have a look at
# the Flask documentation.
app = Flask(__name__)

#bei @ handelt es sich um einen sog. Decorator. Er nimmt die unten definierte Funktion hello_world und erweitert diese
#Wir übergeben also die Funktion an den Flask Decorator app.route(PFAD)
#Dieser erzeugt für uns eine html Seite unter dem angegeben Pfad. Wir müssen dadurch kein HTML schreiben!

#'/' ist immer die Homepage. Z.B. bei google.com steht eigentlich dahinter noch ein / : google.com/
#Unser Browser blendet dies aber meistens genauso aus, wie z.B. "https//"
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def bye():
    return 'Bye, World!'

@app.route('/name/<username>')
def greet(username):
    return f"Hi {username}"

@app.route('/name/<username>/<number>')
def greet_age(username, number):
    return f"Hi {username}, are you {number} years old?"

#Debug erlaubt es, Anderungen im Quellcode direkt im Browser zu begutachten,
# ohne dass das Programm neu ausgeführt werden muss

#In diesem Fall eigentlich überflüssig. Prüft, ob hello.py als Main ausgeführt wird. Wenn ja, wird app.run ausgeführt
#Sorgt dafür, dass app.run nicht ausgeführt wird, wenn das hello.py woanders importiert wird
if __name__ == "__main__":
    app.run(debug=True)