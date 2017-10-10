# Stick Wars : IN SPACE

## Code Infrastructure:

Notes on how the code packages and modules are setup. Please read this before coding anything!

### Package Naming and Organization
__main__.py is the main entry point for the whole program and is what starts the entire game. It loads all the packages by default.

Each python package represents a "module" of the game. For example all classes that do UI related tasks are in the "UI" package. This allows for quick and easy referencing of code and makes the code easier to manage.

## Modules
A list of the main modules that are in the project and how they should be used and referenced.
### Scenes
The Scene system represents a "view" of the game. For example there is a Scene for the main menu, but when you hit start it loads the game scene which would run the actual game.

All scenes reference the SceneBase class, refer to that class for more information.

### ImageCache
The ImageCache package provides utility methods to load images for the game. This makes sure we don't load copies of images and saves memory in the long run. Only use these methods for loading image files from the Images folder.

### UI
The UI package provides useful classes and methods for displaying information onto the screen, such as text or buttons. Use this package to create UI elements within the game. Refer to the package for further information. 

### UnitMangement
The UnitManagement package contains all of the Units for the game. It also includes the UnitLoader class which is responsible for the creation and deletion of units in the game. Refer to the package for more information.K

