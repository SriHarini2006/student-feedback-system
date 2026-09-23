from app import app, load_feedbacks
import unittest

class TestFeedbackApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Student Feedback Management System", response.data)
        self.assertIn(b"Easy Feedback Submission", response.data)
        self.assertIn(b"Dockerized Application", response.data)
        self.assertIn(b"Jenkins Automation", response.data)

    def test_feedback_page_get(self):
        response = self.client.get('/feedback')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Student Feedback Form", response.data)

    def test_feedback_submission_and_persistence(self):
        test_payload = {
            "name": "DevOps Tester",
            "department": "Computer Science & Engineering",
            "email": "test@college.edu",
            "rating": "5",
            "message": "CI/CD testing pipeline verified successfully!"
        }
        response = self.client.post('/feedback', data=test_payload, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Feedback submitted successfully", response.data)

        # Check view feedback
        view_response = self.client.get('/view-feedback')
        self.assertEqual(view_response.status_code, 200)
        self.assertIn(b"DevOps Tester", view_response.data)
        self.assertIn(b"CI/CD testing pipeline verified successfully!", view_response.data)

if __name__ == '__main__':
    unittest.main()
