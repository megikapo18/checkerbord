from flask import  flask ,render_template
app = flask(__name__)

@app.route('/<x>/<y>/<color1>/<color2>')
def checkborder (x,y,color1,color2):
    return render_template ('indez.html',row=x,col=y,color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True)