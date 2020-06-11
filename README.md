# Castle

Castle is a Django web application built as part of a school project. It provides an interface for a hypothetical client to help him choose the security solution that he needs, among a predefined list.

## Installation

First, install required packages with

```bash
python3.6 -m pip install -r requirements.txt
```

Then, run the server locally with

```bash
python3.6 manage.py runserver
```

## Usage


This web application comes with a default database. It already has 2 groups of users:
- `staff`
- `customers`

These groups are not meant to be modified, they are essential to the proper functioning of the application.  
They contain default users, which are just examples and can be modified:
- `castle` (member of `staff`), the administrator
- `danone` (member of `customers`), an example customer

Both of them have `bonjour` as password.

`staff` members are able to access all the website pages, whereas `customers` members cannot access `/staff/` endpoints.
