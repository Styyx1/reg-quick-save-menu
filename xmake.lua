-- include subprojects
includes("lib/commonlibsse", "extern/styyx-utils")

local MOD_NAME = "MenuRegularQuickSave"
local MOD_VERSION = "1.1.0"
local MOD_DESC = "Turns quick saves from within the menu to regular saves"

-- set project constants
set_project(MOD_NAME)
set_version(MOD_VERSION)
set_license("GPL-3.0")
set_languages("c++23")
set_warnings("allextra")



-- add common rules
add_rules("mode.debug", "mode.releasedbg")
add_rules("plugin.vsxmake.autoupdate")

-- define targets
target(MOD_NAME)
    add_deps("styyx-util")
    add_rules("commonlibsse.plugin", {
        name = MOD_NAME,
        author = "styyx",
        description = MOD_DESC
    })

    -- add src files
    add_files("src/**.cpp")
    set_pcxxheader("src/pch.h")
