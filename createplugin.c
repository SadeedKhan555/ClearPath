#include "XPLMPlugin.h"
#include "XPLMInstance.h"
#include "XPLMDataAccess.h"
#include "XPLMGraphics.h"
#include "XPLMScenery.h"

XPLMObjectRef objRef;
XPLMInstanceRef instanceRef;

PLUGIN_API int XPluginStart(char *outName, char *outSig, char *outDesc) {
    strcpy(outName, "SpawnObjectPlugin");
    strcpy(outSig, "com.example.spawnobject");
    strcpy(outDesc, "A plugin to spawn objects in X-Plane.");

    // Load the object
    objRef = XPLMLoadObject("lib/airport/Common_Elements/Miscellaneous/Cones.obj");
    if (objRef == NULL) {
        return 0; // Failed to load object
    }

    // Create an instance of the object
    instanceRef = XPLMCreateInstance(objRef, NULL);

    return 1; // Plugin started successfully
}

PLUGIN_API void XPluginStop(void) {
    // Clean up
    if (instanceRef) XPLMDestroyInstance(instanceRef);
    if (objRef) XPLMUnloadObject(objRef);
}

PLUGIN_API void XPluginDisable(void) {
    // Plugin disabled
}

PLUGIN_API int XPluginEnable(void) {
    return 1; // Plugin enabled
}

PLUGIN_API void XPluginReceiveMessage(XPLMPluginID inFrom, int inMsg, void *inParam) {
    // Handle messages
}
