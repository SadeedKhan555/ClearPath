-- FlyWithLua script to spawn an object on runway 25R at KDAB

-- Define the coordinates for the middle of runway 25R at KDAB
local runway_25R_lat = 29.1795  -- Latitude of the runway center
local runway_25R_lon = -81.0583 -- Longitude of the runway center
local runway_25R_elev = 10.0    -- Elevation in meters (adjust as needed)

-- Load a default X-Plane object (replace with your object's path if using a custom object)
local obj_path = "lib/airport/Common_Elements/Miscellaneous/Cones.obj" -- Example: X-Plane's cone object

-- Create a new command to spawn the object
create_command("FlyWithLua/spawn_object", "Spawn Object on Runway 25R", 
    function() -- Command handler
        -- Load the object at the specified location
        local obj_ref = loadObject(obj_path, runway_25R_lat, runway_25R_lon, runway_25R_elev)
        if obj_ref then
            print("FlyWithLua: Object spawned on runway 25R at KDAB")
        else
            print("FlyWithLua Error: Failed to load object at " .. obj_path)
        end
    end
)
