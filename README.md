# Titanic_Kaggle_Group

The open source project we participated in is called the Titanic Disaster Machine Learning on Kaggle.com. For this project, the three of us used Python, three Anaconda packages for Python, Jupyter notebook, and Kaggle.com for submissions. The Jupyter notebook included all of the necessary libraries that we had to use in order to make our calculations, but the .py file in our github requires the user to download them.

Our task was to train our machine to predict whether any particular individual survived the tragic crash of the Titanic. The algorithm uses predictor variables (sex, age, class, etc.) to determine the binary response (survived, did not survive) of individuals. 
In order to build this program, we used Python language to read the train.csv file. Then we used the regression model in order create our predictions after it calculated the multiple variables related to the likelihood of an individual's survival. We used the model on the test.csv file and submitted our predictions to Kaggle to get a score.

In order to run our program, the user must go to this website https://www.continuum.io/downloads and download Anaconda. The Anacondas package list include NumPy, Pandas, and Sklearn. NumPy is a fundamental package for scientific computing and Pandas is an open source data analysis tool for Python.  Sklearn contains the logistic regression that we use. Follow this github link (https://github.com/akane478/Titanic_Kaggle_Group), download the files, and write the command “python final_model.py” into the terminal after entering the correct directory. 

The way our team collaborated and organized was fairly simple. Matt was the most skilled coder so he took the lead on head coder. He wrote and improved most of the code. Simon and Allie split responsibility for using analyzation, the Excel sheets, visualization using Jupyter, and documentation. We worked a little bit every week familiarizing ourselves with Python, Anaconda, the libraries, and Kaggle submissions. By the end of the last week, we were finalizing our code and making sure it ran smoothly. 

__________________________________________________________________________________________________________________________________________
Running this program requires 3 packages:

  1) Numpy
  
  2) Pandas
  
  3) Sklearn

I suggest that you download Anaconda. Simply open the terminal and write "conda install scikit-learn". Anaconda contains all of the packages that are necessary to run this program.  If you do not wish to do so, follow these instructions.

1) Numpy - Numpy is considered the fundamental package for scientific computing with Python.  Go to https://pypi.python.org/pypi/numpy and download the appropriate file type.  For more information on numpy, visit http://www.numpy.org/.

2) Pandas - Pandas makes manipulating and extracting data from excel spreadsheets very easy.  Go to http://pandas.pydata.org/getpandas.html and download the appropriate file type.  For more information on pandas, visit http://pandas.pydata.org/index.html.

3) Sklearn - Sklearn provides the logistic regression that we use as the base of our model.  Use the command "pip install -U scikit-learn" if you have the latest version of pip.  Visit http://scikit-learn.org/stable/ to learn more.

Description of contained files:

1) final_model.py - The final model that we went with.  It scored an accuracy of 77.033% when applied to the test.csv.  It takes into account the sex, fare paid, class, and a custom variable named "YMCA" that was a 1 if the person was either female OR (male AND less than 16 years old) and 0 if not.  You can run this by accessing the directory through the terminal and inputting the command "python final_model.py".  You must have python 3.5.2 installed.  If you do not, get it here: https://www.python.org/downloads/ 

2) sex_model.py - Only takes sex into account.  This was made first to be sure that we could get a logistic regression up and running.

3) sex_age.py - Takes into account age and sex.  This file helped us realize that age isn't the most effective variable, which is why we created YMCA.

4) train.csv - Contains the information we used to train our model.  It has a filled out "survived" column.

5) test.csv - The data on which we scored our model.  It does NOT have a filled out "survived" column.

6) YMCA_Sex_Pclass_Fare_submission.csv - Contains the results of applying our model to the test.csv.  This is what we submitted to Kaggle.
