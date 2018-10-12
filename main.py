from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

form =  """
    <html>
    <head> 
        <style> 
            * {margin: 0;
                padding: 0;
                }
            form {
                background-color: #eee;
                padding: 20x;
                margin: 0 auto;
                width: 540px;
                font: 16x sans-serif;
                border-radius: 10px;
            }

            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }

        </style>

    </head>
    <body>
        <form action='/'  method='POST' >
            <label ><bold>Rotate by:</bold>
                <input type='text' name='rot' value='0' />
            </label>
            
            <br>
            
            <input type='textarea' name='text'  />

            <input type='submit' name='Submit' />
            


        </form>


    </body>
    </html>
"""

@app.route('/')
def index():
    return form


app.run()

