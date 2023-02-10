from rest_framework.test import APIClient
from test_cases.Login_test import APITESTCaseK


class AccountApiTest(APITESTCaseK):
    
    def setUp(self):
        super(AccountApiTest,self).setUp()
        self.response = self.register_user()        

    def test_register_user(self):
        '''register user and get token'''
        resp = self.response.json()
        self.assertTrue(resp['status'])
        self.assertEqual(resp['message'], "success")
        self.assertTrue(resp['access_token'])
        self.assertEqual(self.response.status_code, 201)

    def test_login(self):
        '''login with credential test'''
        payload = {"username": 'testuser2@yopmail.com','password':'Insure@12'}
        url = "/login/"
        response = self.client.post(url,data=payload)
        resp=response.json()
        self.assertTrue(resp['status'])
        self.assertEqual(resp['message'], "success")
        self.assertTrue(resp['access_token'])
        self.assertEqual(response.status_code, 200)
