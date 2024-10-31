from open_dread_rando.cosmetic_patches import apply_tunable_patches
from open_dread_rando.misc_patches import lua_util
from open_dread_rando.patcher_editor import ActorLayer
from dread_mod_loader.mod import DreadMod

scenarios = [
    "s010_cave",
    "s020_magma",
    "s030_baselab",
    "s040_aqua",
    "s050_forest",
    "s060_quarantine",
    "s070_basesanc",
    "s080_shipyard",
    "s090_skybase",
]


class LightsOut(DreadMod):
    def format_actor(self, scenario_name: str, sublayer_name: str, actor_name: str) -> dict[str, str]:
        return {
            "scenario": scenario_name,
            "actor_layer": "rLightsLayer",
            "sublayer": sublayer_name,
            "actor": actor_name
        }

    def patch(self):
        # Remove all lights
        for scenario_name in scenarios:
            scenario = self.editor.get_scenario(scenario_name)

            to_remove = [
                self.format_actor(scenario_name, sublayer_name, actor_name)
                for sublayer_name, actor_name, actor
                in scenario.all_actors_in_actor_layer(ActorLayer.LIGHTS)
            ]

            for actor in to_remove:
                self.editor.remove_entity(actor, None)

        # Replace Lua scripts
        if self.settings["default_skip_intro_checkbox"]:
            lua_util.create_script_copy(self.editor, "system/scripts/init")
            self.editor.replace_asset("system/scripts/init.lc", (self.mod_path / "custom_init.lua").read_bytes())

            lua_util.create_script_copy(self.editor, "maps/levels/c10_samus/s010_cave/s010_cave")
            self.editor.replace_asset("maps/levels/c10_samus/s010_cave/s010_cave.lc", (self.mod_path / "s010_cave.lua").read_bytes())

        # Patch tunables
        tunables = self.apply_cosmetics({})["config"]

        if self.settings["default_emmi_dot_checkbox"]:
            tunables["EmmyAIComponent"] = { "iMinimapMode": 0 }

        apply_tunable_patches(self.editor, tunables)
