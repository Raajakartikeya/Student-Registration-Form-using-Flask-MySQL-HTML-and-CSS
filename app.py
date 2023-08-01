from flask import Flask, render_template, request
import mysql.connector as mysql
app = Flask(__name__)

mydb = mysql.connect(host="localhost", user="root", passwd="sql@1234", database="RAAJA")
mycursor = mydb.cursor()

sqlFormula = "INSERT INTO regform (name,mobileno,email,department,college,age)  VALUES (%s, %s, %s, %s, %s, %s)"
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name']
        mobileno = userDetails['number']
        email = userDetails['email']
        department = userDetails['department']
        college = userDetails['college']
        age = userDetails['age']

        mycursor.execute(sqlFormula, (name,mobileno,email,department,college,age))
        mydb.commit()
        print(name,mobileno,email,department,college,age,sep="\n")
        return render_template('success.html')

    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
