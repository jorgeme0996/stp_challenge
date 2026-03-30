import time

def retry(func, key_to_check:str, value_for_success:any, retries: int = 3, delay: int = 1, **kwargs):
  print('Hla retry')
  print(retries)
  for i in range(retries):
    try:
      response = func(**kwargs)
      if response.get(key_to_check) == value_for_success:
        return response
      else:
        raise Exception(f"Response did not contain the expected value: {value_for_success}")
    except Exception as e:
      print(f"Error: {e} on attempt {i + 1}")
      time.sleep(delay)
      continue
    return None
  return None