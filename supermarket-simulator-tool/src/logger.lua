local logger = {}
local config = require("config")

local levels = {
    debug = 1,
    info = 2,
    warn = 3,
    error = 4
}

local function should_log(level)
    return levels[level] >= levels[config.LOG_LEVEL]
end

function logger.debug(msg)
    if should_log("debug") then
        print("[DEBUG] " .. msg)
    end
end

function logger.info(msg)
    if should_log("info") then
        print("[INFO] " .. msg)
    end
end

function logger.warn(msg)
    if should_log("warn") then
        print("[WARN] " .. msg)
    end
end

function logger.error(msg)
    if should_log("error") then
        print("[ERROR] " .. msg)
    end
end

return logger