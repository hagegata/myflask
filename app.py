import os
import redis
from flask import Flask

app=Flask(__name__)

redis_host=os.getenv ("REDIS_HOST", "localhost")
redis_port=int(os.getenv("REDIS_PORT","6380"))

r=redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route("/")
def index():
  msg=os.getenv("WELCOME_MSG","Привет")
  visits=r.incr("hits")
  return f"{msg}! Visits: {visits}"
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)

