import json
from dataclasses import dataclass
from typing import List

@dataclass
class Idea:
    id: int
    text: str

@dataclass
class Board:
    id: int
    name: str
    ideas: List[Idea]

class OfflineFirstApp:
    def __init__(self):
        self.boards = []
        self.offline_queue = []

    def create_board(self, name: str) -> Board:
        board = Board(len(self.boards) + 1, name, [])
        self.boards.append(board)
        return board

    def add_idea(self, board_id: int, text: str) -> Idea:
        board = next((b for b in self.boards if b.id == board_id), None)
        if board:
            idea = Idea(len(board.ideas) + 1, text)
            board.ideas.append(idea)
            self.offline_queue.append({"action": "add_idea", "board_id": board_id, "idea": idea})
            return idea
        else:
            raise ValueError("Board not found")

    def update_idea(self, board_id: int, idea_id: int, text: str) -> Idea:
        board = next((b for b in self.boards if b.id == board_id), None)
        if board:
            idea = next((i for i in board.ideas if i.id == idea_id), None)
            if idea:
                idea.text = text
                self.offline_queue.append({"action": "update_idea", "board_id": board_id, "idea_id": idea_id, "text": text})
                return idea
            else:
                raise ValueError("Idea not found")
        else:
            raise ValueError("Board not found")

    def delete_idea(self, board_id: int, idea_id: int) -> None:
        board = next((b for b in self.boards if b.id == board_id), None)
        if board:
            idea = next((i for i in board.ideas if i.id == idea_id), None)
            if idea:
                board.ideas.remove(idea)
                self.offline_queue.append({"action": "delete_idea", "board_id": board_id, "idea_id": idea_id})
            else:
                raise ValueError("Idea not found")
        else:
            raise ValueError("Board not found")

    def sync(self) -> None:
        # Simulate syncing with a server
        print("Syncing with server...")
        for action in self.offline_queue:
            print(f"Syncing {action['action']}...")
        self.offline_queue = []

    def get_offline_status(self) -> bool:
        return len(self.offline_queue) > 0

    def get_sync_progress(self) -> int:
        return len(self.offline_queue)
