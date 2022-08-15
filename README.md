# Crop-Yield-Prediction
A Sustainable Development Research Project in which developed a model that predicts crop yield and suggests crops for a given district by considering factors like temperature, rainfall, area, etc.

# Description

Agriculture is one of the major and the least paid occupation in India. Machine learning can bring a boom in the agriculture field by changing the income scenario through growing the optimum crop. This paper focuses on predicting the yield of the crop by applying various machine learning
techniques. The outcome of these techniques is compared on the basis of mean absolute error. The prediction made by machine learning algorithms will help the farmers to decide which crop to grow to get the maximum yield by considering factors like temperature, rainfall, area, etc.

# Required libraries
* Numpy
* Matplotlib
* Pandas
* Tensorflow
* Sklearn
* XGBoost
<br/>
Make sure to install the above libraries and finally run the scripts

# Models Utilized
* **Logistic regression:**<br/><br/> 
Logistic regression is a statistical model which is used primarily for classification tasks. Logistic regression uses an equation similar to the equation of linear regression, however, it models the dependent (or output) variable as a binary (or categorical) value using a logistic or sigmoid function. A L2 regularized logistic regression model has been used for the experiments.<br/><br/>

* **Neural network:**<br/><br/>
Inside the human brain, multiple neurons are interconnected, where each neuron takes a sensory input and produces a response. Similarly in an artificial neural network, each input node is connected to numerous neurons in multiple hidden layers, which are in turn are connected to the output nodes in the output layers. The layers are fully connected, and each interconnection has a weight associated with it, which are learned during the training process. Back propagation and gradient descent algorithm are used to train the neural net.<br/><br/>

* **Random Forest:**<br/><br/>
It is an ensemble learning technique based on Random bagging sampling also known as bagging method, where bagging means row sampling with replacement on dataset. Using bagging random samples of dataset are prepared and then training different base learners(decision tree) on those datasets. Random Forest is parallelizable and base learners can be run on different cores while grading boosting is not parallelizable so train time complexity of Random Forest is better than Boosting. Random Forest can handle missing data and outliers fairly well. This process of using multiple base learners can help reduce variance. In Random Forest, infromation gain or gini is used in decision trees for optimization and majority vote of base learners to predict final output.<br/><br/>

* **Extreme gradient boosting (XGBoost):**<br/><br/>
It is an ensemble learning technique based on gradient boosted decision trees, where errors made by the older models are corrected by adding new models. In gradient boosting the models are generated to predict the errors of the previous models, and they are added sequentially to make the final prediction. This process of adding models continues until no further improvements are possible. In extreme gradient boosting, gradient descent algorithm is used to optimize (minimize) the loss function.<br/><br/>

**Note: For information on the observations and results gained through the research project refer to the report provided**
