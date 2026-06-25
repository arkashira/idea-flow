from idea_flow import IdeaFlow, Role
import pytest

def test_assign_role():
    idea_flow = IdeaFlow()
    idea_flow.assign_role("John", Role.ADMIN)
    assert idea_flow.team_members["John"].role == Role.ADMIN

def test_add_idea():
    idea_flow = IdeaFlow()
    idea_flow.assign_role("John", Role.ADMIN)
    idea_flow.add_idea("New idea", "John")
    assert idea_flow.ideas == ["New idea"]

def test_view_ideas():
    idea_flow = IdeaFlow()
    idea_flow.assign_role("John", Role.ADMIN)
    idea_flow.add_idea("New idea", "John")
    idea_flow.assign_role("Jane", Role.VIEWER)
    assert idea_flow.view_ideas("Jane") == ["New idea"]

def test_edit_idea():
    idea_flow = IdeaFlow()
    idea_flow.assign_role("John", Role.ADMIN)
    idea_flow.add_idea("New idea", "John")
    idea_flow.edit_idea(0, "Updated idea", "John")
    assert idea_flow.ideas == ["Updated idea"]

def test_prohibited_action():
    idea_flow = IdeaFlow()
    idea_flow.assign_role("John", Role.VIEWER)
    with pytest.raises(PermissionError):
        idea_flow.add_idea("New idea", "John")

def test_role_change():
    idea_flow = IdeaFlow()
    idea_flow.assign_role("John", Role.VIEWER)
    idea_flow.assign_role("John", Role.ADMIN)
    idea_flow.add_idea("New idea", "John")
    assert idea_flow.ideas == ["New idea"]

def test_403_error():
    idea_flow = IdeaFlow()
    idea_flow.assign_role("John", Role.VIEWER)
    with pytest.raises(PermissionError):
        idea_flow.edit_idea(0, "Updated idea", "John")
