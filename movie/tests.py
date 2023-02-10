from test_cases.Login_test import APITESTCaseK


class MovieApiTest(APITESTCaseK):
    
    def setUp(self):
        super(MovieApiTest,self).setUp()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_user_token())

    def test_get_movies(self):
        '''get movies with authentication'''
        url = "/movies/"
        response = self.client.get(url,data={'format': 'json'})
        resp=response.json()
        self.assertTrue(resp['count'] > 1)
        self.assertEqual(resp['next'], "https://demo.credy.in/api/v1/maya/movies/?page=2")
        self.assertTrue(len(resp['results']) > 1)
        self.assertEqual(response.status_code, 200)
