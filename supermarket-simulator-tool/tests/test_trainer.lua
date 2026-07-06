local luaunit = require("luaunit")
local trainer = require("../src/trainer")
local logger = require("../src/logger")

TestTrainer = {}

function TestTrainer:setUp()
    trainer:initialize()
end

function TestTrainer:test_initialization()
    luaunit.assertTrue(trainer.active)
    luaunit.assertFalse(trainer.features.unlimited_money)
    luaunit.assertFalse(trainer.features.instant_restock)
end

function TestTrainer:test_toggle_feature()
    trainer:toggle_feature("unlimited_money")
    luaunit.assertTrue(trainer.features.unlimited_money)
    trainer:toggle_feature("unlimited_money")
    luaunit.assertFalse(trainer.features.unlimited_money)
end

function TestTrainer:test_toggle_invalid_feature()
    trainer:toggle_feature("nonexistent")
    luaunit.assertNil(trainer.features.nonexistent)
end

function TestTrainer:test_shutdown()
    trainer:shutdown()
    luaunit.assertFalse(trainer.active)
end

os.exit(luaunit.LuaUnit.run())