# UKD Student DB

Educational project for the course "Principles of Development Using Modern Technologies"

## Installation

1. Clone the repository:

`git clone https://github.com/ProlorenzoAndrii/ukd.git`

3. Change dir to django_project

`cd ./django_project`

3. Run docker-compose:

`docker-compose up`

4. Run migration:

`python manage.py migrate`

5. Access the application at `http://localhost:8000/`.

## Usage

- View Students: Visit the "View Students" page to see the list of students.
- Add Student: Click on the "Add Student" link to add a new student to the database.
- Delete Student: On the "View Students" page, each student record has a "Delete" button. Click on it to delete a student.
