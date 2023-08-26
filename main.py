import sys
sys.path.append('/mnt/32346261-2a77-4ea4-ad97-df46c23e0f72/Maya_Scripts/Material_Library')

import importlib
import maya.cmds as cmds
from PySide2.QtWidgets import QMainWindow, QApplication, QListWidgetItem
from UI.Ui_material_library import Ui_material_window

# UI reloading - to be deleted when the UI is finished
def reload_module(module_name):
    if module_name in sys.modules:
        importlib.reload(sys.modules[module_name])

reload_module('UI.Ui_material_library')


class MaterialLibrary(QMainWindow, Ui_material_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.list_arnold_materials()

    # Gets a list of all arnold materials
    def list_arnold_materials(self):
        # Get a list of all shading engines in the scene
        shading_engines = cmds.ls(type='shadingEngine')
        arnold_shaders = []
    
        for sg in shading_engines:
            # Find the shader connected to the shading engine's surfaceShader attribute
            shader_connections = cmds.listConnections(sg + '.surfaceShader', source=True, destination=False)
            # Get the first connected shader - Shading engines can only have one connected shader node
            shader_node = shader_connections[0]
            # Get the type of shader node
            shader_type = cmds.nodeType(shader_node)

            # If the shader type starts with ai (arnold), append it to the arnold_shaders list
            if shader_type.startswith('ai'):
                arnold_shaders.append(shader_node)

        # Create list items and add them to the material_list in the UI
        for material in arnold_shaders:
            item = QListWidgetItem(material)
            self.material_list.addItem(item)


if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    
    window = MaterialLibrary()    
    window.show()