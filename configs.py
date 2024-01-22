try:
    import detectron2
except:
    import git
    git.Repo.clone_from("https://github.com/facebookresearch/detectron2.git", "detectron2")

import numpy as np
import sys, os, distutils
import subprocess

###### DO this below step initially ########

dist = distutils.core.run_setup("./detectron2/setup.py")

for x in dist.install_requires:
    subprocess.check_call([sys.executable, "-m", "pip", "install", f"{x}"])