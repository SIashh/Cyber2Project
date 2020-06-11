# Castle
## Run
- First, install required packages with `python3.6 -m pip install -r requirements.txt`
- Then, run the server locally with `python3.6 manage.py runserver`

## Setup
This web application comes with a default database.  
It involves 2 groups of users:
    - `staff`
    - `customers`
These groups are not meant to be modified, they are essential to the proper functioning of the application.  
They contain default users, which are just examples and can be modified:
    - `castle` (member of `staff`)
    - `danone` (memeber of `customers`)
Both of them have `bonjour` as password.  
`staff` members are able to access all the website pages, whereas `customers` members cannot access `/staff/` endpoints.