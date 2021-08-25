#in this app we create two container that work with each other trough network./
# one container (redis) that store name and age and another (python app) /
# container that use python image for writing name and age to the redis trough network

# 1. create a network in docker for conecting containers together with name (mynet)
# 1.1 CODE : sudo  docker network create mynet  

# 2. run a redis image with name (myredis) on (mynet) network
# 2.2 CODE : sudo docker run --name myredis --rm -p6379:6379 --network mynet redis
# 2.3 note -p6379:6379 is optional to see redis cli in my os


# 3.in python app we use redis container name (myredis) for connecting to
        

# 4. create image for python app with Docker file:
# 4.1  CODE : sudo docker build -t redisapp:v1 .

#5. run python app with :
#5.1 CODE : docker run --rm --network mynet -it redisapp:v1




import redis

print('hello docker users.')

r = redis.Redis()
r = redis.Redis(host='myredis', port=6379, db=0)
r.set('age','31')
r.get('age')
print(r.get('name'))
