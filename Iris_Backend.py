from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from flask import Flask,jsonify,request,render_template
iris=load_iris()
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,train_size=0.2)
from sklearn.linear_model import LogisticRegression
model3=LogisticRegression()
model3.fit(x_train,y_train)
app = Flask(__name__)
@app.route('/hello/<sepal_length>/<sepal_width>/<petal_length>/<petal_width>')
def hello_name(sepal_length,sepal_width,petal_length,petal_width):
   print()
#  print(iris.target_names[model3.predict([[float(sepal_length),float(sepal_width),float(petal_length),float(petal_width)]])])
   return jsonify(specie=(iris.target_names[model3.predict([[float(sepal_length),float(sepal_width),float(petal_length),float(petal_width)]])]).tolist())
if __name__ == '__main__':
   app.run(debug = True)
