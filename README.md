# dynamodb-stream-handler-python-lambda
AWS python lambda for listening to dynamoDB stream. Lambda then publishes event to a sns topic

##Test Event for testing out the lambda

```
{
  "Records": [
    {
      "eventID": "1",
      "eventVersion": "1.0",
      "dynamodb": {
        "Keys": {
          "Id": {
            "N": "101"
          }
        },
        "NewImage": {
          "Message": {
            "S": "New item!"
          },
          "Id": {
            "N": "101"
          }
        },
        "StreamViewType": "NEW_AND_OLD_IMAGES",
        "SequenceNumber": "111",
        "SizeBytes": 26
      },
      "awsRegion": "ap-southeast-1",
      "eventName": "INSERT",
      "eventSourceARN": "arn:aws:dynamodb:ap-southeast-1:account-id:table/ExampleTableWithStream/stream/2015-06-27T00:48:05.899",
      "eventSource": "aws:dynamodb"
    },
    {
      "eventID": "2",
      "eventVersion": "1.0",
      "dynamodb": {
        "OldImage": {
          "Message": {
            "S": "New item!"
          },
          "Id": {
            "N": "101"
          }
        },
        "SequenceNumber": "222",
        "Keys": {
          "Id": {
            "N": "101"
          }
        },
        "SizeBytes": 59,
        "NewImage": {
          "Message": {
            "S": "This item has changed"
          },
          "Id": {
            "N": "101"
          }
        },
        "StreamViewType": "NEW_AND_OLD_IMAGES"
      },
      "awsRegion": "ap-southeast-1",
      "eventName": "MODIFY",
      "eventSourceARN": "arn:aws:dynamodb:ap-southeast-1:account-id:table/ExampleTableWithStream/stream/2015-06-27T00:48:05.899",
      "eventSource": "aws:dynamodb"
    },
    {
      "eventID": "3",
      "eventVersion": "1.0",
      "dynamodb": {
        "Keys": {
          "Id": {
            "N": "101"
          }
        },
        "SizeBytes": 38,
        "SequenceNumber": "333",
        "OldImage": {
          "Message": {
            "S": "This item has changed"
          },
          "Id": {
            "N": "101"
          }
        },
        "StreamViewType": "NEW_AND_OLD_IMAGES"
      },
      "awsRegion": "ap-southeast-1",
      "eventName": "REMOVE",
      "eventSourceARN": "arn:aws:dynamodb:ap-southeast-1:account-id:table/ExampleTableWithStream/stream/2015-06-27T00:48:05.899",
      "eventSource": "aws:dynamodb"
    }
  ]
}
```

##Output log

```
record : {"eventID": "1", "eventVersion": "1.0", "dynamodb": {"Keys": {"Id": {"N": "101"}}, "NewImage": {"Message": {"S": "New item!"}, "Id": {"N": "101"}}, "StreamViewType": "NEW_AND_OLD_IMAGES", "SequenceNumber": "111", "SizeBytes": 26}, "awsRegion": "ap-southeast-1", "eventName": "INSERT", "eventSourceARN": "arn:aws:dynamodb:ap-southeast-1:account-id:table/ExampleTableWithStream/stream/2015-06-27T00:48:05.899", "eventSource": "aws:dynamodb"}
response : {'MessageId': '30edf390-01a0-5fb1-8694-a48525df6ae6', 'ResponseMetadata': {'RequestId': '65d7483c-aed5-56f3-a808-1f298aabe3a4', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '65d7483c-aed5-56f3-a808-1f298aabe3a4', 'content-type': 'text/xml', 'content-length': '294', 'date': 'Sat, 18 Apr 2020 15:52:30 GMT'}, 'RetryAttempts': 0}} for request (keys) {'Id': {'N': '101'}}
........................................................
record : {"eventID": "2", "eventVersion": "1.0", "dynamodb": {"OldImage": {"Message": {"S": "New item!"}, "Id": {"N": "101"}}, "SequenceNumber": "222", "Keys": {"Id": {"N": "101"}}, "SizeBytes": 59, "NewImage": {"Message": {"S": "This item has changed"}, "Id": {"N": "101"}}, "StreamViewType": "NEW_AND_OLD_IMAGES"}, "awsRegion": "ap-southeast-1", "eventName": "MODIFY", "eventSourceARN": "arn:aws:dynamodb:ap-southeast-1:account-id:table/ExampleTableWithStream/stream/2015-06-27T00:48:05.899", "eventSource": "aws:dynamodb"}
response : {'MessageId': 'f41e9117-905f-5af0-84c3-c602b420ffa7', 'ResponseMetadata': {'RequestId': '254a8dfc-2db0-51ea-b0e5-dae909cf74bd', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '254a8dfc-2db0-51ea-b0e5-dae909cf74bd', 'content-type': 'text/xml', 'content-length': '294', 'date': 'Sat, 18 Apr 2020 15:52:30 GMT'}, 'RetryAttempts': 0}} for request (keys) {'Id': {'N': '101'}}
........................................................
record : {"eventID": "3", "eventVersion": "1.0", "dynamodb": {"Keys": {"Id": {"N": "101"}}, "SizeBytes": 38, "SequenceNumber": "333", "OldImage": {"Message": {"S": "This item has changed"}, "Id": {"N": "101"}}, "StreamViewType": "NEW_AND_OLD_IMAGES"}, "awsRegion": "ap-southeast-1", "eventName": "REMOVE", "eventSourceARN": "arn:aws:dynamodb:ap-southeast-1:account-id:table/ExampleTableWithStream/stream/2015-06-27T00:48:05.899", "eventSource": "aws:dynamodb"}
response : {'MessageId': 'cc5a5ed1-cbc8-550c-86fa-09c4efb7805b', 'ResponseMetadata': {'RequestId': 'b3a35b26-5113-52c0-a3e3-0c33756c4797', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'b3a35b26-5113-52c0-a3e3-0c33756c4797', 'content-type': 'text/xml', 'content-length': '294', 'date': 'Sat, 18 Apr 2020 15:52:30 GMT'}, 'RetryAttempts': 0}} for request (keys) {'Id': {'N': '101'}}
........................................................
``` 
