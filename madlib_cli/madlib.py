import re


def read_template(read_file):
    with open(read_file) as file:
        return file.read().strip()



#Got help with this from Kassie 
def parse_template(string):
  
  incoming_string = string
  
  parts = tuple(re.findall(r"\{(.*?\}", incoming_string))
  
  string = re.sub(r"\{(.*?\}", "{}", incoming_string)
  
  print(string, parts)
  return(string, parts)
   
print(parse_template(string))
    

def test_merge():
  pass

if __name__ == "__main__":
    path = 'assets/dark_and_stromy_night_template.txt'
    print(read_template(path))
   
