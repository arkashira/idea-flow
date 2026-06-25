from dataclasses import dataclass
from enum import Enum
from typing import List, Dict

class Role(Enum):
    ADMIN = 1
    VIEWER = 2

@dataclass
class TeamMember:
    name: str
    role: Role

class IdeaFlow:
    def __init__(self):
        self.team_members: Dict[str, TeamMember] = {}
        self.ideas: List[str] = []

    def assign_role(self, name: str, role: Role):
        if name in self.team_members:
            self.team_members[name].role = role
        else:
            self.team_members[name] = TeamMember(name, role)

    def add_idea(self, idea: str, member_name: str):
        if self.team_members[member_name].role == Role.ADMIN:
            self.ideas.append(idea)
        else:
            raise PermissionError("Only admins can add ideas")

    def view_ideas(self, member_name: str):
        if self.team_members[member_name].role in [Role.ADMIN, Role.VIEWER]:
            return self.ideas
        else:
            raise PermissionError("Only admins and viewers can view ideas")

    def edit_idea(self, idea_index: int, new_idea: str, member_name: str):
        if self.team_members[member_name].role == Role.ADMIN:
            if idea_index < len(self.ideas):
                self.ideas[idea_index] = new_idea
            else:
                raise IndexError("Idea index out of range")
        else:
            raise PermissionError("Only admins can edit ideas")
