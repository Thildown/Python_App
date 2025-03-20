import unittest
from health_utils import calculate_bmi, calculate_bmr
import json
from app import app

class TestHealthUtils(unittest.TestCase):
    def test_calculate_bmi(self):
        # Test avec un BMI normal
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
        
        # Test avec un BMI faible
        self.assertAlmostEqual(calculate_bmi(1.80, 55), 16.98, places=2)
        
        # Test avec un BMI élevé
        self.assertAlmostEqual(calculate_bmi(1.65, 90), 33.06, places=2)
        
        # Test des exceptions
        with self.assertRaises(ValueError):
            calculate_bmi(0, 70)
        with self.assertRaises(ValueError):
            calculate_bmi(1.75, 0)

    def test_calculate_bmr_male(self):
        # Test pour homme
        self.assertAlmostEqual(calculate_bmr(175, 70, 30, 'male'), 1695.67, places=2)
        
        # Test des exceptions
        with self.assertRaises(ValueError):
            calculate_bmr(0, 70, 30, 'male')
        with self.assertRaises(ValueError):
            calculate_bmr(175, 0, 30, 'male')
        with self.assertRaises(ValueError):
            calculate_bmr(175, 70, 0, 'male')
        with self.assertRaises(ValueError):
            calculate_bmr(175, 70, 30, 'autre')

    def test_calculate_bmr_female(self):
        # Test pour femme
        self.assertAlmostEqual(calculate_bmr(165, 60, 25, 'female'), 1405.33, places=2)

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_bmi_endpoint(self):
        data = {
            'height': 1.75,
            'weight': 70
        }
        response = self.app.post('/bmi', 
                                json=data,
                                content_type='application/json')
        result = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(result['bmi'], 22.86, places=2)
        self.assertEqual(result['category'], 'Poids normal')

    def test_bmr_endpoint(self):
        data = {
            'height': 175,
            'weight': 70,
            'age': 30,
            'gender': 'male'
        }
        response = self.app.post('/bmr', 
                                json=data,
                                content_type='application/json')
        result = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(result['bmr'], 1695.67, places=2)

if __name__ == '__main__':
    unittest.main()