import sys
import os

project_home = os.path.dirname(os.path.abspath(__file__))
if project_home not in sys.path:
    sys.path.insert(0, project_home)

src_path = os.path.join(project_home, 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

os.chdir(project_home)

from src.main import app as application
