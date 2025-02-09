import pytest
from Project import ProjectAPI

BASE_URL = "https://ru.yougile.com/api-v2"
API_KEY = 


@pytest.fixture
def project_api():
    return ProjectAPI(BASE_URL, API_KEY)


@pytest.fixture
def created_project(project_api):
    title = "Test Project"
    users = {"058b1a6a-4bb5-4a60-b0f5-3b3c3eef2070": "admin"}
    response = project_api.create_project(title, users)

    assert response.status_code == 201, f"Ошибка создания проекта: {response.text}"
    project_id = response.json()["id"]
    yield project_id


@pytest.mark.parametrize("title, users, expected_status_code", [
    ("Test Project", {"058b1a6a-4bb5-4a60-b0f5-3b3c3eef2070": "admin"}, 201),
])
def test_create_project(project_api, title, users, expected_status_code):
    response = project_api.create_project(title, users)

    assert response.status_code == expected_status_code, f"Ошибка: {response.text}"

    if response.status_code == 201:
        response_json = response.json()
        assert "id" in response_json


def test_get_projects(project_api):
    response = project_api.get_projects()

    assert response.status_code == 200, f"Ошибка: {response.text}"
    projects = response.json().get("content", [])

    assert len(projects) > 0, "Список проектов пуст!"


@pytest.mark.parametrize("new_title, expected_status_code", [
    ("Updated Test Project", 200),
])
def test_update_project(project_api, created_project, new_title, expected_status_code):
    project_id = created_project
    users = {"058b1a6a-4bb5-4a60-b0f5-3b3c3eef2070": "admin"}
    response = project_api.update_project(project_id, new_title, users)

    assert response.status_code == expected_status_code, f"Ошибка: {response.text}"

    updated_project = project_api.get_project(project_id)
    assert updated_project.status_code == 200, f"Ошибка при получении обновленного проекта: {updated_project.text}"
    assert updated_project.json().get("title") == new_title, f"Проект не обновлен, получено название: {updated_project.json().get('title')}"
