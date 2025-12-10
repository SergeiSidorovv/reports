import pytest

from report.models_report import PerformanceReport
from report.work_reports import ReportFactory


@pytest.fixture
def employess_data():
    data = [
        ("Backend Developer", 4.85),
        ("DevOps Engineer", 4.7),
        ("Data Engineer", 4.7),
        ("Data Scientist", 4.7),
        ("Mobile Developer", 4.6),
        ("Frontend Developer", 4.6),
        ("QA Engineer", 4.5),
    ]
    return data


@pytest.fixture
def employess2_data():
    data = [
        ("DevOps Engineer", 4.9),
        ("Backend Developer", 4.8),
        ("Frontend Developer", 4.7),
        ("Data Scientist", 4.6),
        ("QA Engineer", 4.5),
    ]
    return data


@pytest.fixture
def employess_and_employess2_data():
    data = [
        ("Backend Developer", 4.83),
        ("DevOps Engineer", 4.8),
        ("Data Engineer", 4.7),
        ("Frontend Developer", 4.65),
        ("Data Scientist", 4.65),
        ("Mobile Developer", 4.6),
        ("QA Engineer", 4.5),
    ]
    return data


@pytest.fixture
def paremeters_performance_report():
    data = ["position", "performance"]
    return data


@pytest.fixture
def paremeters_report_factory():
    data = {
        "performance": PerformanceReport(),
    }
    return data


@pytest.fixture
def rows_employess2():
    data = [
        {
            "name": "Alex Ivanov",
            "position": "Backend Developer",
            "completed_tasks": "45",
            "performance": "4.8",
            "skills": "Python, Django, PostgreSQL, Docker",
            "team": "API Team",
            "experience_years": "5",
        },
        {
            "name": "Maria Petrova",
            "position": "Frontend Developer",
            "completed_tasks": "38",
            "performance": "4.7",
            "skills": "React, TypeScript, Redux, CSS",
            "team": "Web Team",
            "experience_years": "4",
        },
        {
            "name": "John Smith",
            "position": "Data Scientist",
            "completed_tasks": "29",
            "performance": "4.6",
            "skills": "Python, ML, SQL, Pandas",
            "team": "AI Team",
            "experience_years": "3",
        },
        {
            "name": "Anna Lee",
            "position": "DevOps Engineer",
            "completed_tasks": "52",
            "performance": "4.9",
            "skills": "AWS, Kubernetes, Terraform, Ansible",
            "team": "Infrastructure Team",
            "experience_years": "6",
        },
        {
            "name": "Mike Brown",
            "position": "QA Engineer",
            "completed_tasks": "41",
            "performance": "4.5",
            "skills": "Selenium, Jest, Cypress, Postman",
            "team": "Testing Team",
            "experience_years": "4",
        },
    ]
    return data


@pytest.fixture
def rows_employess():
    data = [
        {
            "name": "David Chen",
            "position": "Mobile Developer",
            "completed_tasks": "36",
            "performance": "4.6",
            "skills": "Swift, Kotlin, React Native, iOS",
            "team": "Mobile Team",
            "experience_years": "3",
        },
        {
            "name": "Elena Popova",
            "position": "Backend Developer",
            "completed_tasks": "43",
            "performance": "4.8",
            "skills": "Java,SpringBoot,MySQL,Redis",
            "team": "API Team",
            "experience_years": "4",
        },
        {
            "name": "Chris Wilson",
            "position": "DevOps Engineer",
            "completed_tasks": "39",
            "performance": "4.7",
            "skills": "Docker, Jenkins, GitLab CI,AWS",
            "team": "Infrastructure Team",
            "experience_years": "5",
        },
        {
            "name": "Olga Kuznetsova",
            "position": "Frontend Developer",
            "completed_tasks": "42",
            "performance": "4.6",
            "skills": "Vue.js, JavaScript, Webpack, Sass",
            "team": "Web Team",
            "experience_years": "3",
        },
        {
            "name": "Robert Kim",
            "position": "Data Engineer",
            "completed_tasks": "34",
            "performance": "4.7",
            "skills": "Python, Apache Spark, Airflow, Kafka",
            "team": "Data Team",
            "experience_years": "4",
        },
        {
            "name": "Julia Martin",
            "position": "QA Engineer",
            "completed_tasks": "38",
            "performance": "4.5",
            "skills": "Playwright, Jest, API Testing",
            "team": "Testing Team",
            "experience_years": "3",
        },
        {
            "name": "Tom Anderson",
            "position": "Backend Developer",
            "completed_tasks": "49",
            "performance": "4.9",
            "skills": "Go, Microservices, gRPC, PostgreSQL",
            "team": "API Team",
            "experience_years": "7",
        },
        {
            "name": "Lisa Wang",
            "position": "Mobile Developer",
            "completed_tasks": "33",
            "performance": "4.6",
            "skills": "Flutter, Dart, Android, Firebase",
            "team": "Mobile Team",
            "experience_years": "2",
        },
        {
            "name": "Mark Thompson",
            "position": "Data Scientist",
            "completed_tasks": "31",
            "performance": "4.7",
            "skills": "R, Python, TensorFlow, SQL",
            "team": "AI Team",
            "experience_years": "4",
        },
    ]


@pytest.fixture
def rows_employess_and_employess2():
    data = [
        {
            "name": "David Chen",
            "position": "Mobile Developer",
            "completed_tasks": "36",
            "performance": "4.6",
            "skills": "Swift, Kotlin, React Native, iOS",
            "team": "Mobile Team",
            "experience_years": "3",
        },
        {
            "name": "Elena Popova",
            "position": "Backend Developer",
            "completed_tasks": "43",
            "performance": "4.8",
            "skills": "Java,SpringBoot,MySQL,Redis",
            "team": "API Team",
            "experience_years": "4",
        },
        {
            "name": "Chris Wilson",
            "position": "DevOps Engineer",
            "completed_tasks": "39",
            "performance": "4.7",
            "skills": "Docker, Jenkins, GitLab CI, AWS",
            "team": "Infrastructure Team",
            "experience_years": "5",
        },
        {
            "name": "Olga Kuznetsova",
            "position": "Frontend Developer",
            "completed_tasks": "42",
            "performance": "4.6",
            "skills": "Vue.js, JavaScript, Webpack, Sass",
            "team": "Web Team",
            "experience_years": "3",
        },
        {
            "name": "Robert Kim",
            "position": "Data Engineer",
            "completed_tasks": "34",
            "performance": "4.7",
            "skills": "Python, Apache Spark, Airflow, Kafka",
            "team": "Data Team",
            "experience_years": "4",
        },
        {
            "name": "Julia Martin",
            "position": "QA Engineer",
            "completed_tasks": "38",
            "performance": "4.5",
            "skills": "Playwright, Jest, API Testing",
            "team": "Testing Team",
            "experience_years": "3",
        },
        {
            "name": "Tom Anderson",
            "position": "Backend Developer",
            "completed_tasks": "49",
            "performance": "4.9",
            "skills": "Go, Microservices, gRPC, PostgreSQL",
            "team": "API Team",
            "experience_years": "7",
        },
        {
            "name": "Lisa Wang",
            "position": "Mobile Developer",
            "completed_tasks": "33",
            "performance": "4.6",
            "skills": "Flutter, Dart, Android, Firebase",
            "team": "Mobile Team",
            "experience_years": "2",
        },
        {
            "name": "Mark Thompson",
            "position": "Data Scientist",
            "completed_tasks": "31",
            "performance": "4.7",
            "skills": "R, Python, TensorFlow, SQL",
            "team": "AI Team",
            "experience_years": "4",
        },
        {
            "name": "Alex Ivanov",
            "position": "Backend Developer",
            "completed_tasks": "45",
            "performance": "4.8",
            "skills": "Python, Django, PostgreSQL, Docker",
            "team": "API Team",
            "experience_years": "5",
        },
        {
            "name": "Maria Petrova",
            "position": "Frontend Developer",
            "completed_tasks": "38",
            "performance": "4.7",
            "skills": "React, TypeScript, Redux, CSS",
            "team": "Web Team",
            "experience_years": "4",
        },
        {
            "name": "John Smith",
            "position": "Data Scientist",
            "completed_tasks": "29",
            "performance": "4.6",
            "skills": "Python, ML, SQL, Pandas",
            "team": "AI Team",
            "experience_years": "3",
        },
        {
            "name": "Anna Lee",
            "position": "DevOps Engineer",
            "completed_tasks": "52",
            "performance": "4.9",
            "skills": "AWS, Kubernetes, Terraform, Ansible",
            "team": "Infrastructure Team",
            "experience_years": "6",
        },
        {
            "name": "Mike Brown",
            "position": "QA Engineer",
            "completed_tasks": "41",
            "performance": "4.5",
            "skills": "Selenium, Jest, Cypress, Postman",
            "team": "Testing Team",
            "experience_years": "4",
        },
    ]
