import requests;


class PayPalApi(object) :

    authValue = {};

    def __init__(self):

        url = "https://api.sandbox.paypal.com/v1/oauth2/token";

        cid = "";
        secret = "";


        headers={
            'Content-Type' : 'application/json',
        }
        body = {'grant_type':'client_credentials'}

        res = requests.post(url, headers=headers, data=body, auth=(cid, sec));
        self.authValue = res.json();

        pass;



    def getOrder(self, orderId):
        print(self.authValue);
        authType = self.authValue.get("token_type");
        authToken = self.authValue.get("access_token");
        auth = authType + " " + authToken;

        url = "https://api.sandbox.paypal.com/v2/checkout/orders/" + str(orderId);
        headers = {'Authorization' : auth}

        res = requests.get(url, headers=headers);

        return res.json();
