import os, sys
def file_path(rel_path):
  return os.path.join(sys.path[0], rel_path)