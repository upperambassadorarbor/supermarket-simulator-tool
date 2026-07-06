local trainer = require("trainer")
local config = require("config")
local logger = require("logger")

local function main()
    logger.info("Supermarket Simulator Trainer v" .. config.VERSION)
    trainer:initialize()
    
    local running = true
    while running do
        trainer:update()
        local cmd = io.read()
        if cmd == "exit" then
            running = false
        elseif cmd == "help" then
            trainer:print_help()
        else
            logger.warn("Unknown command: " .. cmd)
        end
    end
    
    trainer:shutdown()
    logger.info("Trainer closed.")
end

main()