# Compare two configuration dictionaries and report changed keys

# Explaination
# In Data Engineering, applications often use configuration dictionaries to store settings such as database names, batch sizes, file formats, and environment details.

# Your task is to compare an old configuration with a new configuration and identify which keys have changed.

# For this exercise, consider a key changed if:
# - Its value is different in both dictionaries.
# - It exists in only one of the dictionaries (added or removed).

old_config = {
    "database": "production",
    "batch_size": 1000,
    "format": "csv",
    "retries": 3
}

new_config = {
    "database": "production",
    "batch_size": 2000,
    "format": "parquet",
    "timeout": 30
}

def compare_config(old_config,new_config):
    result = dict()

    for i in old_config:
        if i in new_config:
            if old_config[i] != new_config[i]:
                result[i] = (old_config[i],new_config[i])

        else:
            result[i] = (old_config[i],None)

    for i in new_config:
        if i not in old_config:
            result[i] = (None,new_config[i])

    return result

print(compare_config(old_config,new_config))
