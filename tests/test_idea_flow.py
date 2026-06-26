import pytest
from idea_flow import IdeaFlow, Idea, Theme

def test_create_theme():
    idea_flow = IdeaFlow()
    theme = idea_flow.create_theme("Test Theme")
    assert theme.id == 1
    assert theme.name == "Test Theme"
    assert theme.ideas == []

def test_add_idea_to_theme():
    idea_flow = IdeaFlow()
    theme = idea_flow.create_theme("Test Theme")
    idea = idea_flow.add_idea_to_theme(1, "Test Idea")
    assert idea.id == 1
    assert idea.text == "Test Idea"
    assert theme.ideas == [idea]

def test_get_theme():
    idea_flow = IdeaFlow()
    theme = idea_flow.create_theme("Test Theme")
    retrieved_theme = idea_flow.get_theme(1)
    assert retrieved_theme == theme

def test_get_themes():
    idea_flow = IdeaFlow()
    theme1 = idea_flow.create_theme("Test Theme 1")
    theme2 = idea_flow.create_theme("Test Theme 2")
    themes = idea_flow.get_themes()
    assert themes == [theme1, theme2]

def test_get_ideas_per_theme():
    idea_flow = IdeaFlow()
    theme1 = idea_flow.create_theme("Test Theme 1")
    idea_flow.add_idea_to_theme(1, "Test Idea 1")
    theme2 = idea_flow.create_theme("Test Theme 2")
    idea_flow.add_idea_to_theme(2, "Test Idea 2")
    ideas_per_theme = idea_flow.get_ideas_per_theme()
    assert ideas_per_theme == {1: 1, 2: 1}

def test_to_json():
    idea_flow = IdeaFlow()
    theme = idea_flow.create_theme("Test Theme")
    idea_flow.add_idea_to_theme(1, "Test Idea")
    json_string = idea_flow.to_json()
    assert json_string == '[{"id": 1, "name": "Test Theme", "ideas": [{"id": 1, "text": "Test Idea"}]}]'

def test_theme_not_found():
    idea_flow = IdeaFlow()
    with pytest.raises(ValueError):
        idea_flow.add_idea_to_theme(1, "Test Idea")
