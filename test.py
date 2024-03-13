import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Set a key-value pair
r.set('example_key', 'example_value')

# Get the value for a key
value = r.get('example_key')
print("Value for 'example_key':", value.decode())

# Increment a key
r.incr('example_counter')
counter_value = r.get('example_counter')
print("Value of 'example_counter':", counter_value.decode())

# List operations
r.lpush('example_list', 'item1', 'item2', 'item3')
list_values = r.lrange('example_list', 0, -1)
print("Values of 'example_list':", [val.decode() for val in list_values])

# Set operations
r.sadd('example_set', 'member1', 'member2', 'member3')
set_values = r.smembers('example_set')
print("Values of 'example_set':", [val.decode() for val in set_values])

# Hash operations
r.hset('example_hash', 'field1', 'value1')
r.hset('example_hash', 'field2', 'value2')
hash_values = r.hgetall('example_hash')
print("Values of 'example_hash':", {key.decode(): val.decode() for key, val in hash_values.items()})

# Delete a key
r.delete('example_key')

