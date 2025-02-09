import requests

class ProjectAPI:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def create_project(self, title, users):
        url = f"{self.base_url}/projects"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "title": title,
            "users": users
        }
        response = requests.post(url, headers=headers, json=payload)
        return response

    def get_project(self, project_id):
        url = f"{self.base_url}/projects/{project_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        return response

    def update_project(self, project_id, title, users, deleted=False):
        url = f"{self.base_url}/projects/{project_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "title": "Updated Test Project",
            "users": users,
            "deleted": deleted
        }
        response = requests.put(url, headers=headers, json=payload)
        return response

    def get_projects(self):
        url = f"{self.base_url}/projects"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        return response
