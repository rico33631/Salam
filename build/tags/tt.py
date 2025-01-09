import os
import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))
sys.path.append(os.path.join(parent_dir, "data"))

import build
from lang import Lang
from value import Value
from element import Element

if __name__ == "__main__":
    element = Element()
    element.set_is_mother(True)
    element.set_generate_name("u")
    element.set_text(Lang.EN, "u")
    element.set_text(Lang.FA, "زیرخط")

    element_dict = element.to_dict()

    build.print(element_dict)
    base.save(element_dict)
