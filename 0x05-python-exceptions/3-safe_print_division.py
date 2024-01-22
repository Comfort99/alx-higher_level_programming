#!/usr/bin/python3
def safe_print_division(a, b):
  result = None
  try:
    # Perform the division
    result = a / b
  except ZeroDivisionError:
    # Handle division by zero
    pass
  finally:
    # Print the result
    print("Inside result: {}".format(result))
  # Return the result
  return result
