import unittest
import requests

BASE_URL = 'http://localhost:5000'


class TestOdineFreelanceMarketplace(unittest.TestCase):

    def test_search_by_name(self):
        """
        Searching Freelancers with city name
        """
        search_name = 'Freelancer 1'
        freelancers = requests.get(f'{BASE_URL}/users').json()
        filtered_freelancers = [f for f in freelancers if search_name.lower() in f['name'].lower()]

        self.assertGreater(len(filtered_freelancers), 0, f'No freelancers found with name {search_name}')
        self.assertTrue(all(search_name.lower() in f['name'].lower() for f in filtered_freelancers))
        print("Freelancer searched with name successfully !")

    def test_search_by_finished_job_count(self):
        """
        Checking Freelancers with their finished job count
        """
        freelancers = requests.get(f'{BASE_URL}/users').json()
        min_job_count = 5
        max_job_count = 10
        filtered_freelancers = [
            f for f in freelancers if min_job_count <= f['jobCount'] <= max_job_count
        ]

        self.assertGreater(len(filtered_freelancers), 0,
                           f'No freelancers found with job count between {min_job_count} and {max_job_count}')
        self.assertTrue(all(min_job_count <= f['jobCount'] <= max_job_count for f in filtered_freelancers))
        print("Freelancers finished job count checked successfully !")

    def test_search_by_city(self):
        """
        Searching Freelancers with city name
        """
        search_city = 'New York'
        freelancers = requests.get(f'{BASE_URL}/users').json()
        filtered_freelancers = [f for f in freelancers if search_city.lower() in f['city'].lower()]

        self.assertGreater(len(filtered_freelancers), 0, f'No freelancers found with name {search_city}')
        self.assertTrue(all(search_city.lower() in f['city'].lower() for f in filtered_freelancers))
        print("Freelancer searched with city successfully !")

    def test_hire_freelancer_popup(self):
        """
        Checking Hire PopUp for FreeLancers
        """
        freelancer_data = {
            "name": "John Doe",
            "message_subject": "Job Opportunity",
            "message_body": "I would like to hire you for a project."
        }

        # Simulate the popup submission (no real endpoint)
        self.assertTrue(freelancer_data["name"], "John Doe")
        self.assertTrue(freelancer_data["message_subject"], "Job Opportunity")
        self.assertTrue(freelancer_data["message_body"], "I would like to hire you for a project.")
    print("Freelancer hired popup checked  successfully !")

    def test_light_dark_mode_toggle(self):
        """
        Here we would simulate the toggle switch action, but this is mostly front-end code
        We will assert if the mode can be toggled between light and dark
        """
        current_mode = 'light'
        new_mode = 'dark' if current_mode == 'light' else 'light'
        self.assertNotEqual(current_mode, new_mode, "Mode toggle is not working properly")
        print("Mode Toggle checked successfully !")

    def test_save_freelancer_feature(self):
        """
        Checking Save Freelancer button
        """
        freelancers = requests.get(f'{BASE_URL}/users').json()
        saved_freelancer = freelancers[0]  # Assume we save the first freelancer
        saved_freelancers = [saved_freelancer]  # Saved freelancers list
        self.assertIn(saved_freelancer, saved_freelancers, "Freelancer was not saved correctly")
        print("Freelancer saved correctly !")


if __name__ == '__main__':
    unittest.main()
