from flask import Flask, render_template_string
import os
app = Flask(__name__)
TEMPLATE = '''<h1>Attendance</h1><table border=1><tr><th>ts</th><th>faces</th></tr>{rows}</table>'''
@app.route('/')
def index():
    p = 'data/attendance.csv'
    rows=''
    if os.path.exists(p):
        with open(p) as f:
            next(f)
            for line in f:
                ts,faces = line.strip().split(',')
                rows += f'<tr><td>{ts}</td><td>{faces}</td></tr>'
    return render_template_string(TEMPLATE, rows=rows)
if __name__=='__main__':
    app.run(debug=True)