from flask import Flask , render_template
#iniciamos el objeto
app = Flask(__name__)
#ruta principal
@app.route('/')
def home():
    data={
        'titulo':'index',
        'bienbenida':'hola mundo'
    }
    return render_template('index.html',data=data)

if __name__ =='__main__':
    app.run(debug=True, port=5000)