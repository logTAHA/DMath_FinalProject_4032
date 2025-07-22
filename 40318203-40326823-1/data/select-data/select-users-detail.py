import json
import sys

users_detail_path = "user.json"
users_path = "selected-users.txt"
fields_to_keep = ["id", "username", "name", "description", "location", "verified", "protected", "created_at"]

with open(users_detail_path, "r", encoding="utf-8") as jf, \
     open(users_path, "r", encoding="utf-8") as tf:
    users = json.load(jf)
    lines_selected_users = tf.readlines()
    selected_users_id = []
    for line in lines_selected_users:
        selected_users_id.append(line.strip())

selected_users = []

for user_id in selected_users_id:
    user = None
    for u in users:
        if u["id"] == user_id:
            user = u
            break
    if user is None:
        print(f"user {user_id} not found")
        sys.exit()
    # save users specific data
    filtered_user = {}
    for key in fields_to_keep:
        filtered_user[key] = user.get(key)
    selected_users.append(filtered_user)
# save file
output_path = "users-detail.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(selected_users, f, ensure_ascii=False, indent=2)
print("saved to " + output_path)