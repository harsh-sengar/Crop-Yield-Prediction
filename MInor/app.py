from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
import pickle
import numpy as np
from keras.layers import SimpleRNN, Dense, Dropout, LSTM
from keras.models import Sequential
from keras.models import model_from_json 

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	def save(dicti, name):
		with open(name, 'wb') as fp:
			pickle.dump(dicti, fp, protocol=pickle.HIGHEST_PROTOCOL)
	def load(name):
		with open(name, 'rb') as fp:
			data=pickle.load(fp)
			return data
	dictionary = load("data/dict1")
	def CreateTrainDataset(data, k=10):
		dataX, dataY = [],[]
		for i in range(data.shape[0]-k):
			x=data[i:i+k]
			dataX.append(x)
			y=data[i+k]
			dataY.append(y)
		return np.array(dataX), np.array(dataY)
	if request.method == 'POST':
		comment = request.form['comment']
	    
		data1 = [comment]
		data1=str(data1)
		def CreateDataset(dis):
			lst=[]
			for year in dictionary[dis]:
				lst.append(dictionary[dis][year])
			lst=np.array(lst)
			trainData = lst[:90]
			testData = lst[90:]
			x_train, y_train = CreateTrainDataset(trainData)
			x_test, y_test = CreateTrainDataset(testData)
			return x_train, x_test, y_train, y_test
		x_train, x_test, y_train, y_test = CreateDataset(comment)
		json_file=open('data/model.json','r')
		loaded_model=json_file.read()
		json_file.close()
		model=model_from_json(loaded_model)
		model.load_weights("data/CropNameWt.h5")
		model.compile(loss='mean_squared_error', optimizer='rmsprop', metrics=['accuracy'])
		ypred = model.predict(x_test);
		return render_template('result.html',prediction = ypred)



if __name__ == '__main__':
	app.run(debug=True)