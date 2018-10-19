from flask import Flask, request
from caeser import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True

form =  """
<!DOCTYPE html>
    <html>
    <head> 
        <style> 
            * {{margin: 0;
                padding: 0;
                }}
            form {{
                background-color: #eee;
                padding: 20x;
                margin: 0 auto;
                width: 540px;
                font: 16x sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                 margin: 10px ;
                 width: 500px;
                 height: 120px;
            }}
            

        </style>

    </head>
    <body>
        <form  action='/'  method='POST' >
        <br>
            <label ><bold>Rotate by:</bold>
                <input type='text' name='rot' value='0' />
            </label>
            
            <br>
            
            <textarea  name='text' >{}</textarea>

            <input type='submit' name='Submit' />
            


        </form>


    </body>
    </html>
"""

@app.route('/')
def index():
    return form.format('')

@app.route("/" , methods=['post'])
def encrypt():
    text1 = request.form['text']
    rot1 = request.form['rot']
    rotated = rotate_string(text1,int(rot1))
    print(rotated)
    new_text = rotated
    updated_form = form.format(new_text)
    return updated_form






app.run()

