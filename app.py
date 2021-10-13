from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle
import pandas as pd
from application_logger.app_logger import Logger

app = Flask(__name__, template_folder='templates')

logfile_path = 'LogFiles/prediction_log.txt'
logger_object = Logger()


@app.route('/')
@cross_origin()
def home_page():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
@cross_origin()
def result_page():
    logfile = open(logfile_path, mode='a')
    logger_object.log(logfile, "Preparing for obtaining user input.'")
    if request.method == 'POST':
        try:
            occupation = float(request.form['occupation'])
            occupation_husband = float(request.form['occupation_husband'])
            marriage = float(request.form['marriage'])
            age = float(request.form['age'])
            yrs_married = float(request.form['yrs_married'])
            children = float(request.form['children'])
            religious = float(request.form['religious'])
            education = float(request.form['education'])
            logger_object.log(logfile, "User input obtained successfully.")
            logfile.close()
        except Exception as e:
            logger_object.log(logfile, "Exception occured while obtaining user input. Exception :" + str(e))
            logger_object.log(logfile, "Failed to obtain user input.")
            logfile.close()
            raise Exception()

        try:
            logfile = open(logfile_path, mode='a')
            df_pred = pd.DataFrame(index=[1])

            # Input for Occupation
            if occupation == 2:
                df_pred['occ_2_1.0'] = 1
                df_pred['occ_3_1.0'] = 0
                df_pred['occ_4_1.0'] = 0
                df_pred['occ_5_1.0'] = 0
            elif occupation == 3:
                df_pred['occ_2_1.0'] = 0
                df_pred['occ_3_1.0'] = 1
                df_pred['occ_4_1.0'] = 0
                df_pred['occ_5_1.0'] = 0
            elif occupation == 4:
                df_pred['occ_2_1.0'] = 0
                df_pred['occ_3_1.0'] = 0
                df_pred['occ_4_1.0'] = 1
                df_pred['occ_5_1.0'] = 0
            else:
                df_pred['occ_2_1.0'] = 0
                df_pred['occ_3_1.0'] = 0
                df_pred['occ_4_1.0'] = 0
                df_pred['occ_5_1.0'] = 1


            # Input for Occupation of husband
            if occupation_husband == 2:
                df_pred['occ_husb_2_1.0'] = 1
                df_pred['occ_husb_4_1.0'] = 0
                df_pred['occ_husb_5_1.0'] = 0
            elif occupation_husband == 4:
                df_pred['occ_husb_2_1.0'] = 0
                df_pred['occ_husb_4_1.0'] = 1
                df_pred['occ_husb_5_1.0'] = 0
            else:
                df_pred['occ_husb_2_1.0'] = 0
                df_pred['occ_husb_4_1.0'] = 0
                df_pred['occ_husb_5_1.0'] = 1

            # Input for Marriage rating
            if marriage == 1:
                df_pred['rate_marriage_2.0'] = 0
                df_pred['rate_marriage_3.0'] = 0
                df_pred['rate_marriage_4.0'] = 0
                df_pred['rate_marriage_5.0'] = 0
            elif marriage == 2:
                df_pred['rate_marriage_2.0'] = 1
                df_pred['rate_marriage_3.0'] = 0
                df_pred['rate_marriage_4.0'] = 0
                df_pred['rate_marriage_5.0'] = 0
            elif marriage == 3:
                df_pred['rate_marriage_2.0'] = 0
                df_pred['rate_marriage_3.0'] = 1
                df_pred['rate_marriage_4.0'] = 0
                df_pred['rate_marriage_5.0'] = 0
            elif marriage == 4:
                df_pred['rate_marriage_2.0'] = 0
                df_pred['rate_marriage_3.0'] = 0
                df_pred['rate_marriage_4.0'] = 1
                df_pred['rate_marriage_5.0'] = 0
            else:
                df_pred['rate_marriage_2.0'] = 0
                df_pred['rate_marriage_3.0'] = 0
                df_pred['rate_marriage_4.0'] = 0
                df_pred['rate_marriage_5.0'] = 1

            # Input for age
            if age == 17.5:
                df_pred['age_22.0'] = 0
                df_pred['age_27.0'] = 0
                df_pred['age_32.0'] = 0
                df_pred['age_37.0'] = 0
                df_pred['age_42.0'] = 0
            elif age == 22:
                df_pred['age_22.0'] = 1
                df_pred['age_27.0'] = 0
                df_pred['age_32.0'] = 0
                df_pred['age_37.0'] = 0
                df_pred['age_42.0'] = 0
            elif age == 27:
                df_pred['age_22.0'] = 0
                df_pred['age_27.0'] = 1
                df_pred['age_32.0'] = 0
                df_pred['age_37.0'] = 0
                df_pred['age_42.0'] = 0
            elif age == 32:
                df_pred['age_22.0'] = 0
                df_pred['age_27.0'] = 0
                df_pred['age_32.0'] = 1
                df_pred['age_37.0'] = 0
                df_pred['age_42.0'] = 0
            elif age == 37:
                df_pred['age_22.0'] = 0
                df_pred['age_27.0'] = 0
                df_pred['age_32.0'] = 0
                df_pred['age_37.0'] = 1
                df_pred['age_42.0'] = 0
            else:
                df_pred['age_22.0'] = 0
                df_pred['age_27.0'] = 0
                df_pred['age_32.0'] = 0
                df_pred['age_37.0'] = 0
                df_pred['age_42.0'] = 1

            # Input for yrs_married
            if yrs_married == 0.5:
                df_pred['yrs_married_2.5'] = 0
                df_pred['yrs_married_6.0'] = 0
                df_pred['yrs_married_9.0'] = 0
                df_pred['yrs_married_13.0'] = 0
                df_pred['yrs_married_16.5'] = 0
                df_pred['yrs_married_23.0'] = 0
            elif yrs_married == 2.5:
                df_pred['yrs_married_2.5'] = 1
                df_pred['yrs_married_6.0'] = 0
                df_pred['yrs_married_9.0'] = 0
                df_pred['yrs_married_13.0'] = 0
                df_pred['yrs_married_16.5'] = 0
                df_pred['yrs_married_23.0'] = 0
            elif yrs_married == 6:
                df_pred['yrs_married_2.5'] = 0
                df_pred['yrs_married_6.0'] = 1
                df_pred['yrs_married_9.0'] = 0
                df_pred['yrs_married_13.0'] = 0
                df_pred['yrs_married_16.5'] = 0
                df_pred['yrs_married_23.0'] = 0
            elif yrs_married == 9:
                df_pred['yrs_married_2.5'] = 0
                df_pred['yrs_married_6.0'] = 0
                df_pred['yrs_married_9.0'] = 1
                df_pred['yrs_married_13.0'] = 0
                df_pred['yrs_married_16.5'] = 0
                df_pred['yrs_married_23.0'] = 0
            elif yrs_married == 13:
                df_pred['yrs_married_2.5'] = 0
                df_pred['yrs_married_6.0'] = 0
                df_pred['yrs_married_9.0'] = 0
                df_pred['yrs_married_13.0'] = 1
                df_pred['yrs_married_16.5'] = 0
                df_pred['yrs_married_23.0'] = 0
            elif yrs_married == 16.5:
                df_pred['yrs_married_2.5'] = 0
                df_pred['yrs_married_6.0'] = 0
                df_pred['yrs_married_9.0'] = 0
                df_pred['yrs_married_13.0'] = 0
                df_pred['yrs_married_16.5'] = 1
                df_pred['yrs_married_23.0'] = 0
            else:
                df_pred['yrs_married_2.5'] = 0
                df_pred['yrs_married_6.0'] = 0
                df_pred['yrs_married_9.0'] = 0
                df_pred['yrs_married_13.0'] = 0
                df_pred['yrs_married_16.5'] = 0
                df_pred['yrs_married_23.0'] = 1

            # Input for children
            if children == 0:
                df_pred['children_1.0'] = 0
                df_pred['children_2.0'] = 0
                df_pred['children_3.0'] = 0
                df_pred['children_4.0'] = 0
                df_pred['children_5.5'] = 0
            elif children == 1:
                df_pred['children_1.0'] = 1
                df_pred['children_2.0'] = 0
                df_pred['children_3.0'] = 0
                df_pred['children_4.0'] = 0
                df_pred['children_5.5'] = 0
            elif children == 2:
                df_pred['children_1.0'] = 0
                df_pred['children_2.0'] = 1
                df_pred['children_3.0'] = 0
                df_pred['children_4.0'] = 0
                df_pred['children_5.5'] = 0
            elif children == 3:
                df_pred['children_1.0'] = 0
                df_pred['children_2.0'] = 0
                df_pred['children_3.0'] = 1
                df_pred['children_4.0'] = 0
                df_pred['children_5.5'] = 0
            elif children == 4:
                df_pred['children_1.0'] = 0
                df_pred['children_2.0'] = 0
                df_pred['children_3.0'] = 0
                df_pred['children_4.0'] = 1
                df_pred['children_5.5'] = 0
            else:
                df_pred['children_1.0'] = 0
                df_pred['children_2.0'] = 0
                df_pred['children_3.0'] = 0
                df_pred['children_4.0'] = 0
                df_pred['children_5.5'] = 1

            # Input for religious
            if religious == 1:
                df_pred['religious_2.0'] = 0
                df_pred['religious_3.0'] = 0
                df_pred['religious_4.0'] = 0
            elif religious == 2:
                df_pred['religious_2.0'] = 1
                df_pred['religious_3.0'] = 0
                df_pred['religious_4.0'] = 0
            elif religious == 3:
                df_pred['religious_2.0'] = 0
                df_pred['religious_3.0'] = 1
                df_pred['religious_4.0'] = 0
            else:
                df_pred['religious_2.0'] = 0
                df_pred['religious_3.0'] = 0
                df_pred['religious_4.0'] = 1

            # Input for education
            if education == 9:
                df_pred['educ_12.0'] = 0
                df_pred['educ_14.0'] = 0
                df_pred['educ_16.0'] = 0
                df_pred['educ_17.0'] = 0
                df_pred['educ_20.0'] = 0
            elif education == 12:
                df_pred['educ_12.0'] = 1
                df_pred['educ_14.0'] = 0
                df_pred['educ_16.0'] = 0
                df_pred['educ_17.0'] = 0
                df_pred['educ_20.0'] = 0
            elif education == 14:
                df_pred['educ_12.0'] = 0
                df_pred['educ_14.0'] = 1
                df_pred['educ_16.0'] = 0
                df_pred['educ_17.0'] = 0
                df_pred['educ_20.0'] = 0
            elif education == 16:
                df_pred['educ_12.0'] = 0
                df_pred['educ_14.0'] = 0
                df_pred['educ_16.0'] = 1
                df_pred['educ_17.0'] = 0
                df_pred['educ_20.0'] = 0
            elif education == 17:
                df_pred['educ_12.0'] = 0
                df_pred['educ_14.0'] = 0
                df_pred['educ_16.0'] = 0
                df_pred['educ_17.0'] = 1
                df_pred['educ_20.0'] = 0
            else:
                df_pred['educ_12.0'] = 0
                df_pred['educ_14.0'] = 0
                df_pred['educ_16.0'] = 0
                df_pred['educ_17.0'] = 0
                df_pred['educ_20.0'] = 1

            df_pred.to_csv('UserInput/test.csv')
            logger_object.log(logfile, "Successfully converted User input to 'test.csv'.")
            logfile.close()
        except Exception as e:
            logger_object.log(logfile, "Exception occured during creation of 'test.csv'. Exception :" + str(e))
            logger_object.log(logfile, "Failed to create 'test.csv'")
            logfile.close()
            raise Exception()

        try:
            logfile = open(logfile_path, mode='a')
            # Standardizing the data
            scaler_file = 'Model/standard_scaler.pickle'
            scaled_model = pickle.load(open(scaler_file, 'rb'))
            logger_object.log(logfile, "Successfully loaded the scaler file.")
            logfile.close()
        except Exception as e:
            logger_object.log(logfile, "Exception occured while loading the scaler file. Exception :" + str(e))
            logger_object.log(logfile, "Failed to load the scaler file.")
            logfile.close()
            raise Exception()

        try:
            logfile = open(logfile_path, mode='a')
            df_test_scaled = scaled_model.transform(df_pred)
            logger_object.log(logfile, "Successfully standardized input data.")
            logfile.close()
        except Exception as e:
            logger_object.log(logfile, "Exception occured while standardizing. Exception :" + str(e))
            logger_object.log(logfile, "Failed to standardize the input data.")
            logfile.close()
            raise Exception()

        try:
            logfile = open(logfile_path, mode='a')
            model_file = 'Model/logistic_regression_model.pickle'
            loaded_model = pickle.load(open(model_file, 'rb'))
            logger_object.log(logfile, "Successfully loaded the model for prediction.")
            logfile.close()
        except Exception as e:
            logger_object.log(logfile, "Exception occured while loading the model. Exception :" + str(e))
            logger_object.log(logfile, "Failed to load the model for prediction.")
            logfile.close()
            raise Exception()

        try:
            logfile = open(logfile_path, mode='a')
            prediction = loaded_model.predict(df_test_scaled)
            logger_object.log(logfile, "Successfully predicted the output.")
            logfile.close()
            print("Prediction is :", prediction)
            return render_template("result.html", prediction=prediction[0])
        except Exception as e:
            logger_object.log(logfile, "Exception occured while predicting the output. Exception :" + str(e))
            logger_object.log(logfile, "Failed to predict the output.")
            logfile.close()
            raise Exception()
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
