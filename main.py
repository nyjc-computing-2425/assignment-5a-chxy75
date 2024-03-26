from os import error


def to_hms(seconds: int) -> list:
  """
    Converts seconds to hours, minutes, and seconds, and returns it as a list.

    Parameters
    ---------
    seconds: int
        the seconds to be calculated

    Returns
    ---------
    list
        a list of integers representing hours, minutes, seconds

    Example:
    >>> to_hms(10)
    [0, 0, 10]
    >>> to_hms(61)
    [0, 1, 1]
    >>> to_hms(7199)
    [1, 59, 59]
    """
  # Type your code below
  # print(type(seconds))
  valid = True

  #check if the input is valid
  if isinstance(seconds, str):
    valid = False
  elif (float(seconds).is_integer) and (float(seconds) >= 0):
    valid = True
  else:
    valid = False

  if valid is True:
    minutes, seconds = divmod(int(seconds), int(60))
    #print(minutes, seconds)
    hours, minutes = divmod(int(minutes), int(60))
    #print(minutes,60)
    list = [hours, minutes, seconds]
    return list
  else:
    print('Unsupported input type.')
  pass
to_hms(9177)