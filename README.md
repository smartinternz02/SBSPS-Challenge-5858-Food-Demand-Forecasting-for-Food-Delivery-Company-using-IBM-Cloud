# Food Demand Forecasting for Food Delivery Company using IBM Cloud
[Project for IBM Build-A-Thon](https://smartinternz.com/ibm-build-a-thon-2021)

---
### Video demo link: [Demo](demo.mp4)
### Project deliverables
- [Screen Shot](Screenshot0.png)
- [Report](Report.pdf)
- [ibm_food.ipynb](ibm_food.ipynb)
- [submission.csv](submission.csv)

### Project Work Flow:

- The user interacts with the UI (User Interface) to upload the input features.
- Uploaded features/input is analyzed by the model which is integrated.
- Once the model analyses the uploaded inputs, the prediction is showcased on the UI.

### Dataset:

Our base data consists of four csv files containing information about test data, train data and other required information.

- train.csv: Contains information like id, week, center id, meal id, checkout price, base price, emailer for promotion, homepage featured, number of orders. This file is used for training.
- test.csv: Contains information like id, week, center id, meal id, checkout price, base price, emailer for promotion, homepage featured. This file is used for testing.
- fulfilment_center_info.csv: Contains information of each fulfilment center.
- meal_info.csv: Contains information of each meal being served.


Dataset obtained from [kaggle.com](https://www.kaggle.com/kannanaikkal/food-demand-forecasting).