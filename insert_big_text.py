import redis

# Connect to Redis
r = redis.Redis(host="localhost", port=6379, db=0)


# Function to insert text entries from a file into Redis
def insert_text_entries(file_path):
    full_str = ""
    with open(file_path, "r") as file:
        entries = file.readlines()
        for entry in entries:
            # Remove newline characters from each entry
            entry = entry.strip()
            full_str += entry
            # Add the entry to the Redis list
            r.lpush("text_entries", entry)
    print(f"Inserting big text of { len(full_str)} characters")

    for _ in range(5000):
        # print("inserted")
        r.lpush("fullstr", full_str)


# File path containing the text entries
file_path = "text_entries.txt"

# Insert text entries into Redis

insert_text_entries(file_path)

print("Total entries inserted into Redis  text_entries:", r.llen("text_entries"))
print("Total entries inserted into Redis fullstr :", r.llen("fullstr"))
