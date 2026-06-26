import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Idea:
    id: int
    text: str

@dataclass
class Theme:
    id: int
    name: str
    ideas: List[Idea]

class IdeaFlow:
    def __init__(self):
        self.themes: Dict[int, Theme] = {}
        self.next_theme_id = 1
        self.next_idea_id = 1

    def create_theme(self, name: str) -> Theme:
        theme = Theme(self.next_theme_id, name, [])
        self.themes[self.next_theme_id] = theme
        self.next_theme_id += 1
        return theme

    def add_idea_to_theme(self, theme_id: int, idea_text: str) -> Idea:
        if theme_id not in self.themes:
            raise ValueError("Theme not found")
        idea = Idea(self.next_idea_id, idea_text)
        self.themes[theme_id].ideas.append(idea)
        self.next_idea_id += 1
        return idea

    def get_theme(self, theme_id: int) -> Theme:
        return self.themes.get(theme_id)

    def get_themes(self) -> List[Theme]:
        return list(self.themes.values())

    def get_ideas_per_theme(self) -> Dict[int, int]:
        return {theme_id: len(theme.ideas) for theme_id, theme in self.themes.items()}

    def to_json(self) -> str:
        themes = [{"id": theme.id, "name": theme.name, "ideas": [{"id": idea.id, "text": idea.text} for idea in theme.ideas]} for theme in self.themes.values()]
        return json.dumps(themes)
