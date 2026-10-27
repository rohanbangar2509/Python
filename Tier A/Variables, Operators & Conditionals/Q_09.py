# Parse command-line-style key=value arguments into a dictionary

# In Python, command-line arguments or configuration settings are often provided as strings in the format key=value.

# Your task is to write a function that takes a collection of such strings and converts them into a dictionary.

# For example, given:
# ["database=production", "batch_size=1000", "format=parquet"]


# The expected dictionary is:

# {
#     "database": "production",
#     "batch_size": "1000",
#     "format": "parquet"
# }

import string

config_1 = ["database=production", "batch_size=1000", "format=parquet"]
config_2 = ["database=production", "batch=size=1000", "format=parquet"]
config_3 = ["database", "batch=size=1000", "format=parquet"]


def configuration_to_dict(config):
    dict = {}

    for i in config:
        if '=' in i:
            ele = i.split('=')

            if len(ele) == 2:
                dict[ele[0]] = ele[-1]
            else:
                return f'configuration data issue in \'{i}\''
        else:
            return f'configuration data issue in \'{i}\''
    

    return dict

print(configuration_to_dict(config_1))
print(configuration_to_dict(config_2))
print(configuration_to_dict(config_3))