# Todo list

This app defines a RESTful API to create and maintain To-Do lists.

### Setup

Use `pipenv install` to install dependencies.

### API

All input and output is in json format.

#### Authentication

| Endpoint      | Action | Input                                      | Result         |
| ------------- |:------:| :------------------------------------------| --------------:|
| /signup       | `POST` | email, name, password | auth_token:jwt |
| /auth/login   | `POST` | email, password       | auth_token:jwt |

Set the Authorization header type to `Bearer` and insert the jwt token for all subsequent API calls.

#### To-Do lists

Lists of items to complete.

| Endpoint        | Action        | Input        | Result                           |
| --------------- |:-------------:| :------------| :--------------------------------|
| /api/todos/     | `POST`        | title        | Creates a new To-Do list         |
| /api/todos/     | `GET`         |              | List of the users To-Do lists    |
| /api/todos/<id> | `GET`         |              | Details of a specific To-Do list |
| /api/todos/<id> | `PUT` `PATCH` | To-Do fields | Replace or modify To-Do list     |
| /api/todos/<id> | `DELETE`      |              | Deletes the To-Do list           |

#### To-Do list items

Individual items in To-Do lists have a name, due date and priority.

| Endpoint                              | Action        | Input       | Result                           |
| ------------------------------------- |:-------------:| -----------:| :--------------------------------|
| /api/todos/<todo_id>/items/           | `POST`        | name, done  | Creates a new To-Do item         |
| /api/todos/<id>/items/                | `GET`         |             | List of the users To-Do lists    |
| /api/todos/<todo_id>/items/<item_id>/ | `GET`         |             | Details of a specific To-Do list |
| /api/todos/<todo_id>/items/<item_id>/ | `PUT` `PATCH` | item fields | Replace or modify todo list      |
| /api/todos/<todo_id>/items/<item_id>/ | `DELETE`      |             | Deletes the To-Do list           |

#### Sorting and filtering

Todo items can be sorted on their due date or priority: `/todos/<todo_id:int>/items/<item_id:int>/?sort=priority`

Prepend the field name with a minus sign to sort in descending order: `/todos/<todo_id:int>/items/<item_id:int>/?sort=-priority`

