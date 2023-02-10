# from accounts.models import User
# from rest_framework.test import APIClient
# from rest_framework.test import APITestCase
# from Login_test import APITESTCaseK

# class AccountApiTest(APITESTCaseK):
    
#     def setUp(self):
#         super(APITESTCaseK,self).setUp()
#         # self.client = APIClient()
#         # self.client.credentials(HTTP_AUTHORIZATION='bearer ' + self.token)

#     def test_register_user(self):
#         '''register user and get token'''
        
#         url = "/register/"
#         payload = {"username": 'testuser@yopmail.com','password':'Insure@12'}
#         response = self.get_client().post(url,data=payload)
#         resp=response.json()

#         self.assertTrue(resp['status'])
#         self.assertEqual(resp['message'], "success")
#         self.assertEqual(resp['access_token'], self.get_user_token())
