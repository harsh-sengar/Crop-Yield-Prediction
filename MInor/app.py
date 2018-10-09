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
	dictionary_temperature = load("data/dicttemperature")
	dictionary_rainfall= load("data/dictrainfall")
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
		charts=request.form['charts']
		
		data1 = [comment]
		
		
		def CreateDataset(dis):
			lst_temperature=[]
			lst_rainfall=[]
			for year in dictionary_temperature[dis]:
				lst_temperature.append(dictionary_temperature[dis][year])
				lst_rainfall.append(dictionary_rainfall[dis][year])
			lst_temperature=np.array(lst_temperature)
			lst_rainfall=np.array(lst_rainfall)
			#trainData_temperature = lst_temperature[:90]
			testData_temperature = lst_temperature[90:]
			#trainData_rainfall = lst_rainfall[:90]
			testData_rainfall = lst_rainfall[90:]
			#x_train_t, y_train_t = CreateTrainDataset(trainData_temperature)
			x_test_t, y_test_t = CreateTrainDataset(testData_temperature)
			#x_train_r, y_train_r = CreateTrainDataset(trainData_rainfall)
			x_test_r, y_test_r = CreateTrainDataset(testData_rainfall)
			return x_test_t, x_test_r

		x_test_t, x_test_r = CreateDataset(comment)
		json_t="data/"+comment+"modeltemperature.json"
		json_r="data/"+comment+"modelrainfall.json"
		json_file_t=open(json_t,'r')
		json_file_r=open(json_r,'r')
		loaded_model_t=json_file_t.read()
		loaded_model_r=json_file_r.read()
		json_file_t.close()
		json_file_r.close()
		model_t=model_from_json(loaded_model_t)
		model_r=model_from_json(loaded_model_r)
		name_t="data/"+comment+"temperature.h5"
		name_r="data/"+comment+"rainfall.h5"
		model_t.load_weights(name_t)
		model_r.load_weights(name_r)
		model_t.compile(loss='mean_absolute_error', optimizer='rmsprop', metrics=['accuracy'])
		model_r.compile(loss='mean_absolute_error', optimizer='sgd', metrics=['accuracy'])
		ypred_t = model_t.predict(x_test_t);
		ypred_r = model_r.predict(x_test_r);
		print(ypred_r.shape)
		for j in range(0,12):
			if(ypred_r[0][j]<0):
				ypred_r[0][j]=0

		return render_template('result.html',prediction = ypred_r, prediction2=ypred_t,chart=charts)



if __name__ == '__main__':
	app.run(debug=True)