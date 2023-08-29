import sys
sys.path.append('/mnt/32346261-2a77-4ea4-ad97-df46c23e0f72/Maya_Scripts/Material_Library')

import os
import importlib
import maya.cmds as cmds
import maya.OpenMayaUI as mui
import shiboken2

from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
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

        # List to keep track of imported materials
        self.imported_materials = []
        # Folder to import materials from
        materials_folder = "/mnt/32346261-2a77-4ea4-ad97-df46c23e0f72/Maya/Material_library/Materials/GOLD"
        self.import_materials_from_folder(materials_folder)

        self.display_swatches()

    # Imports all .ma or .mb materials from a specified folder
    def import_materials_from_folder(self, folder_path):
        '''
            Walk through the directory tree rooted at 'folder_path'
            'root' is the current directory being visited
            'dirs' is a list of subdirectories in the current directory
            'files' is a list of filenames in the current directory
        '''
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Checks the file for a maya ascii/binary extension, if not found runs the next step of the lopp
                if not (file.endswith(".ma") or file.endswith(".mb")):
                    continue
                    
                # Creates a full path to the file by joining the root with the file name
                file_path = os.path.join(root, file)
                
                # Extract the material name from the file name (without extension)
                material_name = os.path.splitext(file)[0]
                
                # Skip importing if the material already exists in the scene
                if cmds.objExists(material_name):
                    continue
                
                # Import the file into the scene and add to the list of imported files
                cmds.file(file_path, i=True)
                self.imported_materials.append(file_path)

    # Gets a list of all arnold materials in the scene
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
        
        return arnold_shaders

    # Adds swatches to the UI window
    def display_swatches(self):
        # Get a list of Arnold shaders
        arnold_shaders = self.list_arnold_materials()
        
        # Loop through each shader
        for material in arnold_shaders:
            # Generate a unique name for the swatch control
            swatch_name = f'{material}_swatch'
            
            # Create the swatch using cmds.swatchDisplayPort, specifying the swatch name and size
            swatch_widget = cmds.swatchDisplayPort(f'{swatch_name}', wh=(100, 100), sn=material)
            
            # Convert the C++ swatch_widget pointer to a PySide2 QWidget instance
            swatch_qt_widget = shiboken2.wrapInstance(int(mui.MQtUtil.findControl(swatch_widget)), QWidget)
            
            # Add the PySide2 QWidget to the grid layout, displaying the swatch
            self.gridLayout.addWidget(swatch_qt_widget)


if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    
    window = MaterialLibrary()
    window.show()