def is_isogram(string):
    # the characteres '-' and empty-space are not relevant to consider an isogram
    string = string.replace("-", "").replace(" ", "").lower()

    # set() removes duplicates, therefore if the "prepared string" has the same length,
    # we have an isogram
    if len(string) == len(set(string)):
        return True

    return False
