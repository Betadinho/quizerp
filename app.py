import eel
import constants
from pathlib import Path
import json
eel.init('web')
eel.start(constants.MAIN_PAGE_DIR, jinja_templates=constants.JINJA_TEMPLATE_DIR)

SAVE_FILE_PATH = Path(constants.SAVE_FILE_DIR) / constants.SAVE_FILE_NAME

def create_save_file():
  with open(SAVE_FILE_PATH, 'w') as f:
    content = {'quizlist' : {}}
    json.dump(content, f, indent=2)
             
def read_save_file():
  with open(SAVE_FILE_PATH, 'r') as f:
    result = json.load(f)
  return result

def init_data():
  if Path(SAVE_FILE_PATH).exists() == False:
    create_save_file()

  data = read_save_file()
  return data

data = init_data()
