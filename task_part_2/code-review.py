def get_value(data, key, default, lookup=None, mapper=None):
    """
    Finds the value from data associated with key, or default if the key isn't present.
    If a lookup enum is provided, this value is then transformed to its enum value.
    If a mapper function is provided, this value is then transformed by applying mapper to it.
    """
    return_value = data.get(key, default)  
    if return_value in [None, ""]:
        return_value = default
    if lookup and return_value in lookup:
        return_value = lookup[return_value]  
    if mapper:
        return_value = mapper(return_value)
    return return_value


def ftp_file_prefix(namespace):
    """
    Given a namespace string with dot-separated tokens, returns the
    string with the final token replaced by 'ftp'.
    Example: a.b.c => a.b.ftp
    """
    if not namespace:
        return namespace 
    parts = namespace.split(".")
    if len(parts) == 1:
        return namespace  
    return ".".join(parts[:-1]) + '.ftp'


def string_to_bool(string):
    """
    Returns True if the given string is 'true' case-insensitive,
    False if it is 'false' case-insensitive.
    Raises ValueError for any other input.
    """
    if isinstance(string, str):
        lower_string = string.lower()
        if lower_string == 'true':
            return True
        if lower_string == 'false':
            return False
    raise ValueError(f'String {string} is neither true nor false')


def config_from_dict(dictionary):
    """
    Given a dict representing a row from a namespaces csv file,
    returns a DAG configuration as a pair whose first element is the
    DAG name and whose second element is a dict describing the DAG's properties.
    """
    namespace = dictionary.get('Namespace')
    if not namespace:  # Check for missing namespace
        raise KeyError('Namespace is required')

    return (dictionary.get('Airflow DAG', 'Default DAG'), {
        "earliest_available_delta_days": 0,
        "lif_encoding": 'json',
        "earliest_available_time": get_value(dictionary, 'Available Start Time', '07:00'),
        "latest_available_time": get_value(dictionary, 'Available End Time', '08:00'),
        "require_schema_match": get_value(dictionary, 'Requires Schema Match', 'True', mapper=string_to_bool),
        "schedule_interval": get_value(dictionary, 'Schedule', '1 7 * * * '),
        "delta_days": get_value(dictionary, 'Delta Days', 'DAY_BEFORE'),
        "ftp_file_wildcard": get_value(dictionary, 'File Naming Pattern', None),
        "ftp_file_prefix": ftp_file_prefix(namespace),
        "namespace": namespace
    })
