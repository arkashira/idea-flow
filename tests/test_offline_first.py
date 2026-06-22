from offline_first import OfflineFirstApp, Idea, Board

def test_create_board():
    app = OfflineFirstApp()
    board = app.create_board("Test Board")
    assert board.id == 1
    assert board.name == "Test Board"
    assert len(board.ideas) == 0

def test_add_idea():
    app = OfflineFirstApp()
    board = app.create_board("Test Board")
    idea = app.add_idea(1, "Test Idea")
    assert idea.id == 1
    assert idea.text == "Test Idea"
    assert len(board.ideas) == 1

def test_update_idea():
    app = OfflineFirstApp()
    board = app.create_board("Test Board")
    idea = app.add_idea(1, "Test Idea")
    updated_idea = app.update_idea(1, 1, "Updated Test Idea")
    assert updated_idea.text == "Updated Test Idea"

def test_delete_idea():
    app = OfflineFirstApp()
    board = app.create_board("Test Board")
    idea = app.add_idea(1, "Test Idea")
    app.delete_idea(1, 1)
    assert len(board.ideas) == 0

def test_sync():
    app = OfflineFirstApp()
    board = app.create_board("Test Board")
    idea = app.add_idea(1, "Test Idea")
    app.sync()
    assert app.get_offline_status() == False

def test_get_offline_status():
    app = OfflineFirstApp()
    board = app.create_board("Test Board")
    idea = app.add_idea(1, "Test Idea")
    assert app.get_offline_status() == True

def test_get_sync_progress():
    app = OfflineFirstApp()
    board = app.create_board("Test Board")
    idea = app.add_idea(1, "Test Idea")
    assert app.get_sync_progress() == 1
