import re


def read_template(read_file):
  with open(read_file) as file:
    try:
      return file.read().strip()
    except FileNotFoundError:
      return 'File not Found'

# Got help with this from Kassie 
def parse_template(string):
  
  new_string = string
  
  parts = tuple(re.findall(r"\{(.*?)\}", new_string))
  string = re.sub(r"\{(.*?)\}", "{}", new_string)
  
  print(string, parts)
  return(string, parts)
    

def merge(str, tuple):
  return str.format(*tuple)


if __name__ == "__main__":
    path = 'assets/dark_and_stromy_night_template.txt'
    print(read_template(path))
   
