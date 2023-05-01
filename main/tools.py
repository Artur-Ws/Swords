import json

debug_refs = []


def debug_log():
    for i, debug in enumerate(debug_refs):
        debug.log_info(i)
        debug.remove_if_expired()


def add_json_field(file, parameter, default_value):
    with open(str(file), "r") as f:
        data = json.load(f)
    for enemy in data:
        data[enemy][parameter] = default_value
    with open(str(file), "w") as f:
        json.dump(data, f, indent=4)


# add_json_field("../data/enemies.json", "loot", 44)
