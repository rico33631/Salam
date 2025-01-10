import os
import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))
sys.path.append(os.path.join(parent_dir, "data", "styles"))
sys.path.append(os.path.join(parent_dir, "data", "styles", "values"))

from prebuild import Prebuild

import single_animation_directions
from lang import Lang
from type import Type
from property import Property

if __name__ == "__main__":
    property = Property()
    property.set_generate_name("animation-fill-mode")
    property.add_text(Lang.EN, "animation-fill-mode")
    property.add_text(Lang.FA, "شیوه پر شدن انیمیشن")
    property.set_type(Type.Strings)
    property.add_reserve_values(single_animation_directions.single_animation_directions)

    property_dict = property.to_dict()

    property_str = Prebuild.to_string(property_dict)
    Prebuild.print(property_str)
    Prebuild.save(property_str, __file__)

# https://developer.mozilla.org/en-US/docs/Web/CSS/animation-fill-mode
# animation-fill-mode = 
#   <single-animation-fill-mode>#  

# <single-animation-fill-mode> = 
#   none       |
#   forwards   |
#   backwards  |
#   both       