import redis

r = redis.Redis(
    host='127.0.0.1',
    port=6379)


r.set('foo', 'bar')
value = r.get('foo')
print(value)