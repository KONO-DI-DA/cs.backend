# Kono-di-da Endpoints

Base URL: https://kono-di-da.herokuapp.com/


## Register & Login

Method | Endpoint | Description
------ | -------- | -----------
POST | `api/auth/register` | accepts `username`, `email`, and `password`. creates and returns a `user` and authorization `token`
POST | `api/auth/login` | accepts `username` and `password`. returns a `user` and creates an authorization `token`

#### Accepted Register Schema - POST

```
{
	"username": "testing",
	"email": "testing@mail.com",
	"password": "donuts"
}
```

##### Response Body

```
{
  "user": {
    "id": 3,
    "username": "testing",
    "email": "testing@mail.com"
  },
  "token": "ba1d5b746e210b2216378ba911f09c0fb41d6014346212057942f611c1141baa"
}
```

#### Accepted Login Schema - POST

```
{
	"username": "testing",
	"password": "donuts"
}
```

##### Response Body

```
{
  "user": {
    "id": 3,
    "username": "testing",
    "email": "testing@mail.com"
  },
  "token": "770099eecce57f207d01238fa476db59e83742f8c2ab2466636ca628df92850e"
}
```


## All of the following endpoints require an `Authorization` token


## User

Method | Endpoint | Description
------ | -------- | -----------
GET | `api/auth/user` | returns `user` info

##### Response Body - GET

```
{
  "id": 3,
  "username": "testing",
  "email": "testing@mail.com"
}
```


## Logout

Method | Endpoint | Description
------ | -------- | -----------
POST | `api/auth/logout` | logouts the user and invalidates the user token


## Players

Method | Endpoint | Description
------ | -------- | -----------
POST | `api/players/` | creates a player and returns player info
GET | `api/players` | returns a list of players for the user, should just be one player
PUT | `api/players/{player_id}/` | updates player info

#### Accepted Player Schema - POST

```
{
	"name": "testing",
	"room_id": 1,
	"item_id": 0
}
```

##### Response Body

```
{
  "id": 8,
  "name": "testing",
  "room_id": 1,
  "item_id": 0,
  "owner": 3
}
```

##### Response Body - GET

```
{
  "id": 8,
  "name": "testing",
  "room_id": 1,
  "item_id": 0,
  "owner": 3
}
```

#### Accepted Player Schema - PUT

```
{
  "id": 8,
  "name": "testing",
  "room_id": 22,
  "item_id": 1,
  "owner": 3
}
```

##### Response Body

```
{
  "id": 8,
  "name": "testing",
  "room_id": 22,
  "item_id": 1,
  "owner": 3
}
```

## Rooms

Method | Endpoint | Description
------ | -------- | -----------
GET | `api/room` | returns data for all rooms and how they are connected.
GET | `api/room/{room_id}` | returns data for the one room and how it are connected.

##### Response Body - GET all rooms

```
[
  {
    "id": 1,
    "name": "Dec20-26",
    "season_id": 1,
    "left_id": 0,
    "right_id": 2,
    "up_id": 0,
    "down_id": 5,
    "outside_id": 53,
    "inside_id": 0,
    "item_id": 11,
    "top_tile": 0,
    "bottom_tile": 0
  },
  {
    "id": 2,
    "name": "Jan1-4",
    "season_id": 1,
    "left_id": 1,
    "right_id": 3,
    "up_id": 0,
    "down_id": 6,
    "outside_id": 54,
    "inside_id": 0,
    "item_id": 0,
    "top_tile": 0,
    "bottom_tile": 0
  }
]
```

##### Response Body - GET room by room_id

```
[
  {
    "id": 1,
    "name": "Dec20-26",
    "season_id": 1,
    "left_id": 0,
    "right_id": 2,
    "up_id": 0,
    "down_id": 5,
    "outside_id": 53,
    "inside_id": 0,
    "item_id": 11,
    "top_tile": 0,
    "bottom_tile": 0
  }
]
```


## Items

Method | Endpoint | Description
------ | -------- | -----------
GET | `api/items` | returns all the item objects with info

##### Response Body - GET

```
[
  {
    "id": 10,
    "season_id": 1,
    "name": "Christmas Tree",
    "description": "A decorative tree fo celebrating a holiday."
  },
  {
    "id": 11,
    "season_id": 2,
    "name": "Egg",
    "description": "A Colorfully died egg."
  }
]
```


## Seasons

Method | Endpoint | Description
------ | -------- | -----------
GET | `api/season` | returns all seasons, with name and is_solved (if item is placed into correct season)
PUT | `api/season/{season_id}/` | updates season info

##### Response Body

```
[
  {
    "id": 13,
    "name": "winter",
    "is_solved": 0
  },
  {
    "id": 14,
    "name": "spring",
    "is_solved": 0
  }
]
```

#### Accepted Season Schema - PUT

```
{
  "id": 13,
  "name": "winter",
  "is_solved": 1
}
```

##### Response Body

```
{
  "id": 13,
  "name": "winter",
  "is_solved": 1
}
```
