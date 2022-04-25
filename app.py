from flask import Flask,request
from flask_cors import CORS, cross_origin
import pickle
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/get',methods=['GET','POST'])
def get():
    fuel = {'Petrol': 0, 'Diesel': 1, 'CNG': 2, 'LPG': 3, 'Electric': 4}
    transmission = {'Manual': 0, 'Automatic': 1}
    seller_type = {'Dealer': 0, 'Individual': 1, 'Trustmark Dealer': 0}
    owner = {'First Owner': 0, 'Second Owner': 1, 'Third Owner': 2,'Fourth & Above Owner': 3, 'Test Drive Car': 4}
    
    model = ""
    
    if request.method=='POST':
        year = int(request.json['year'])
        present_price = float(request.json['pprice'])/100000
        kms = float(request.json['kms'])
        fuel = fuel[request.json['fuel']]
        seller_type = seller_type[request.json['seller_type']]
        transmission = transmission[request.json['transmission']]
        owner = owner[request.json['owner']]
    
        with open('car_model', 'rb') as f:
            model = pickle.load(f)
    
        ans = model.predict([[year, present_price, kms, fuel, seller_type, transmission, owner]])
        
        return str(ans[0]*100000)
    return "Get Request"
if __name__=="__main__":
    app.run()
