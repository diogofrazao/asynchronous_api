# asynchronous_api
Asynchronous API using Python Flask

## Start Application:
`` python main.py ``


### Endpoints

```
$ POST http://localhost:3000/create

{
  "id": 1,
  "type_id": 1,
}

```



```
$ POST http://localhost:3000/remove

{
  "worker_id": 1
}

```


```
$ Get http://localhost:3000/info

```
| Status Code   | Description    | 
| ------------- |:--------------:|
| 200           | OK             | 
| 201           | Created        | 
| 400           | Bad Request    | 
| 404           | URL Not Found  | 
| 409           | TODO           | 
| 422           | TODO           | 
| 500           | Internal Error | 


