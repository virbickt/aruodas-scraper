from flask import Flask, render_template, url_for, request, redirect
import psycopg2
from datetime import datetime

app = Flask(__name__)
#connection = psycopg2.connect(
#    database="db0s0f727mk3m2",
#    user="hbexbkvtllxqez",
#    password="ffc439da81a7f6dda2244ca684c2253194a1f49b9a875579b831c018470843c3",
#    host="ec2-54-220-35-19.eu-west-1.compute.amazonaws.com",
#    port="5432"
#)

#cur = connection.cursor()

#cur.execute('''CREATE TABLE model
#    id serial PRIMARY KEY,
#    content VARCHAR(255) NOT NULL,
#    date_created DATE %(date)}
#''', {'date': datetime.now()})


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        #cur.execute('''
        #INSERT INTO model
        #VALUES %(task_content)
        #''', {'task_content': task_content})

        try:
            connection.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        # print all tasks/predictions
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)