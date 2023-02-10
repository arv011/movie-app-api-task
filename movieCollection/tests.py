from test_cases.Login_test import APITESTCaseK


class CollectionApiTest(APITESTCaseK):
    
    def setUp(self):
        super(CollectionApiTest,self).setUp()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_user_token())

    def test_get_collections(self):
        '''get collections with authentication -> negative test'''
        url = "/collection/"
        response = self.client.get(url,data={'format': 'json'})
        resp=response.json()
        self.assertTrue(resp['is_success'])
        self.assertEqual(resp['message'], "success")
        self.assertEqual(resp['data']['collections'], 'Empty Collection! please add New collections')
        self.assertEqual(response.status_code, 200)

    def test_create_collections(self):
        '''create, read, delete collection with authentication -> positive'''
        url = "/collection/"
        payload =  {
            "title": "collection 1",
            "description": "test collection 1",
            "movies": [
                {
                    "title": "San Michele aveva un gallo",
                    "description": "Sentenced to life imprisonment for illegal activities, Italian International member Giulio Manieri holds on to his political ideals while struggling against madness in the loneliness of his prison cell.",
                    "genres": "",
                    "uuid": "cc51020f-1bd6-42ad-84e7-e5c0396435a8"
                },
                {
                    "title": "The Morning After",
                    "description": "The Morning After is a feature film that consists of 8 vignettes that are inter-cut throughout the film. The 8 vignettes are about when you wake up next to someone the next morning...",
                    "genres": "Comedy,Drama",
                    "uuid": "9a4fcb67-24f6-4cda-8f49-ad66b689f481"
                },
                {
                    "title": "Maa",
                    "description": "The bliss of a biology teacher's family life in Delhi is shattered when her daughter, Arya  is physically assaulted by Jagan and gang. Does Devki Sabarwal wait for the law to take its course? Or does Devki become Maa Durga and hunt down the perpetrators of the crime?",
                    "genres": "Crime,Drama,Thriller",
                    "uuid": "587a1f5b-d36a-41a3-8bf8-ea0788ebc752"
                }
            ]
        }

        response = self.client.post(url,data=payload,format='json')
        resp=response.json()
        self.assertTrue(resp['status'])
        self.assertEqual(resp['message'], "success")
        self.assertTrue(resp['collection_uuid'])
        self.assertEqual(response.status_code, 201)

        get_response = self.client.get(url,data={'format': 'json'})
        get_resp=get_response.json()
        self.assertTrue(get_resp['is_success'])
        self.assertEqual(get_resp['message'], "success")
        self.assertEqual(get_resp['data']['collections'][0]['uuid'], resp['collection_uuid'])
        self.assertEqual(get_response.status_code, 200)

        del_response = self.client.delete(url,data={'format': 'json','uuid': resp['collection_uuid']})
        del_resp=del_response.json()
        self.assertTrue(del_resp['status'])
        self.assertEqual(del_resp['message'], "collection successully deleted")
        self.assertEqual(del_response.status_code, 202)