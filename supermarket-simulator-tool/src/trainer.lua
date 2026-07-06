local logger = require("logger")
local config = require("config")

local trainer = {
    active = false,
    features = {}
}

function trainer:initialize()
    self.active = true
    self.features = {
        unlimited_money = false,
        instant_restock = false,
        no_customer_limit = false
    }
    logger.info("Trainer initialized with features: " .. table.concat(config.DEFAULT_FEATURES, ", "))
end

function trainer:update()
    for _, feature in ipairs(config.DEFAULT_FEATURES) do
        if self.features[feature] then
            logger.debug("Feature active: " .. feature)
        end
    end
end

function trainer:toggle_feature(feature_name)
    if self.features[feature_name] ~= nil then
        self.features[feature_name] = not self.features[feature_name]
        local status = self.features[feature_name] and "enabled" or "disabled"
        logger.info("Feature '" .. feature_name .. "' " .. status)
    else
        logger.error("Unknown feature: " .. feature_name)
    end
end

function trainer:print_help()
    print("Available commands:")
    print("  toggle <feature> - Enable/disable a feature")
    print("  list            - Show all features and status")
    print("  exit            - Quit trainer")
    print("  help            - Show this help")
end

function trainer:shutdown()
    self.active = false
    logger.info("Trainer shutdown complete.")
end

return trainer