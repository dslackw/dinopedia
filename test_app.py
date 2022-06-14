#!/usr/bin/env python

import unittest
from app import app


class TestCaseDinopedia(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.dino_name = 'Aardonyx'
        self.dino_images = ['Aardonyx_1.jpg', 'Aardonyx_2.jpg']

    def test_admin(self):
        response = self.client.get('/admin/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_index(self):
        response = self.client.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_api_dinopedia(self):
        response = self.client.get('/dinosaurs')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_api_favourites(self):
        response = self.client.get('/dinosaurs/favourites')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_api_post(self):
        response = self.client.post(f'/dinosaurs/{self.dino_name}',
                                    content_type='application/json')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_api_dinopedia_json(self):
        response = self.client.get('/dinosaurs')
        self.assertEqual(response.content_type, 'application/json')

    def test_api_favourites_json(self):
        response = self.client.get('/dinosaurs/favourites')
        self.assertEqual(response.content_type, 'application/json')

    def test_api_images(self):
        expect = {'images': self.dino_images}
        response = self.client.get(f'/dinosaurs/{self.dino_name}')
        received = response.get_json()
        self.assertDictEqual(received, expect)


if __name__ == '__main__':
    unittest.main()
