import sys
sys.path.append('/mnt/32346261-2a77-4ea4-ad97-df46c23e0f72/Maya_Scripts/Material_Library')

import importlib
import maya.cmds as cmds
from PySide2.QtWidgets import QMainWindow, QApplication
from UI.Ui_material_library import Ui_material_window

def reload_module(module_name):
    if module_name in sys.modules:
        importlib.reload(sys.modules[module_name])

module_name = 'UI.Ui_material_library'
reload_module(module_name)

class MaterialLibrary(QMainWindow, Ui_material_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.list_arnold_materials()

    def list_arnold_materials(self):
        arnold_shaders = []
        all_materials = cmds.ls(materials=True)

        for material in all_materials:
            if material.startswith('ai'):
                arnold_shaders.append(material)

        print(arnold_shaders)

if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    
    window = MaterialLibrary()    
    window.show()