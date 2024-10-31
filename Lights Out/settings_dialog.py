from PySide6.QtWidgets import QWidget

from dread_mod_loader.gui.custom_widgets.saved_checkbox import SavedCheckBox
from dread_mod_loader.settings import UserSettings
from dread_mod_loader.gui.settings_dialog import SettingsDialog


class LightsOutSettings(SettingsDialog):
    def __init__(self, parent: QWidget, settings: UserSettings, disabled = []) -> None:
        super().__init__(parent, settings, disabled)

        skip_intro_checkbox = SavedCheckBox(self.settings, "Skip intro cutscene", self)
        skip_intro_checkbox.setObjectName("skip_intro_checkbox")
        self.cosmetic_tab.display_layout.addWidget(skip_intro_checkbox)

        emmi_dot_checkbox = SavedCheckBox(self.settings, "Remove EMMI minimap dot", self)
        emmi_dot_checkbox.setObjectName("emmi_dot_checkbox")
        self.cosmetic_tab.display_layout.addWidget(emmi_dot_checkbox)
