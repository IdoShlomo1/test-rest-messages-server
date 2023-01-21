


## Convexum assignment


### Test Plan

| #    | Case Name                                          | Steps | Test Data  | Expected | Status | 
| ---  |-----------------------------------                 | -----:| ----------:| --------:|--------:|
| 1    | Test Add message                                   | Send post |$1600       |
| 1    | Test Add existing message                          | $1600 |$1600       |
| 2    | Test Add invalid message                           |   $12 |$12         |
| 2    | Test Delete message                                |    $1 |$1          |
| 2    | Test Delete non existing message                   |    $1 |$1          |
| 2    | Test Delete multiple messages                      |    $1 |$1          |
| 2    | Test Get multiple messages by query param          |    $1 |$1          |
| 2    | Test Delete multiple messages                      |    $1 |$1          |
| 2    | Test Delete multiple messages                      |    $1 |$1          |
| 2    | Test Delete multiple messages                      |    $1 |$1          |

1. Name: Test Add message 
Test Data: <br>
    Random message

Step: <br>
 - Send post request to add message
     
Expected: <br>
 - Status code is equal to 200.
 - Response body schema is
 ```json
    {
        "Record Added": {
            "application": int,
            "content": str,
            "message_id": str,
            "participants": [str],
            "session_id": str
        }
    }
```
 - Response contain the message that being sent.

Step: <br>
  Get the new message by message id

Expected: <br>
  Message exists
  


2. Name: Test Add message with existing message_id
Test Data: <br>
    Random message

Step: <br>
 - Send post request to add message
     
Expected: <br>
 - Status code is equal to 200.
 - Response body schema is
 ```json
    {
        "Record Added": {
            "application": int,
            "content": str,
            "message_id": str,
            "participants": [str],
            "session_id": str
        }
    }
```
 - Response contain the message that being sent.

Step:
 - Generate new message with the message_id of the previous 'message_id'
<br>

 Expected:
  - Status code is equal to 400
  - Response body is equal to ```{"Error": "Record already exists"}```
  

3. Name: Test add invalid message
    1. with invalid schema
    2. with empty object `{}`
    3. with missing data
    4. with session_id not string
    5. with session_id null
    6. with message_id not string
    7. with message_id null
    8. with participants not list
    9. with participants null
    10. with content null
    11. with content not string
    12. with application null
    13. with application not int

Test Data

| #   | Description                     | RequestData        |
|:--- | :---                            |    :----:   |
| 1   | invalid schema                  | ```{"application_key": random_int, "content": random_str, "message_id": random_str, "participants": random_list}``` |
| 2   | empty object                    |`{}` |
| 3   | missing data                    | ```{"content": random_str, "message_id": random_str, "participants": random_list}```                               |
| 4   | session_id not string           | ```{"application": random_int, "content": random_str, "message_id": random_str, "participants": random_list, "session_id": int}```  |
| 5   | session_id is null              | ```{"application": random_int, "content": random_str, "message_id": random_str, "participants": random_list, "session_id": null}``` |
| 6   | message_id is null              | ```{"application": random_int, "content": random_str, "message_id": null, "participants": random_list, "session_id": random_str}``` |
| 7   | message_id not string           | ```{"application": random_int, "content": random_str, "message_id": int, "participants": random_list, "session_id": null}``` |
| 8   | participants is not list        | ```{"application": random_int, "content": random_str, "message_id": int, "participants": str, "session_id": null}``` |
| 9   | participants is null            | ```{"application": random_int, "content": random_str, "message_id": int, "participants": null, "session_id": random_str}``` |
| 10  | content is null                 | ```{"application": random_int, "content": null, "message_id": int, "participants": random_list, "session_id": random_str}``` |
| 11  | content is not string           | ```{"application": random_int, "content": int, "message_id": int, "participants": random_list, "session_id": random_str}``` |
| 12  | application is null             | ```{"application": null, "content": random_str, "message_id": int, "participants": random_list, "session_id": random_str}``` |
| 13  | application is not int       | ```{"application": str, "content": random_str, "message_id": int, "participants": random_list, "session_id": random_str}``` |

Step:
 - Add message using `{RequestData}`

Expected:
   - Status code is equal to 400
   - Response body
   ```{"Error": "Records data is not valid"}```
   
  
<br>

4. Name: Test delete message by value
    1. value: application
    2. value: application
    3. value: application
    4. value: application

5. Name: Test delete non existing message

6. Name: Test delete message by invalid value
