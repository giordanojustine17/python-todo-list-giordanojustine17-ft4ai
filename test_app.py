import app
import csv


def test_delete_task_uses_displayed_number():
    app.tasks[:] = ["Workout", "Study Python"]

    app.delete_task(2)

    assert app.tasks == ["Workout"]


def test_delete_task_ignores_invalid_number():
    app.tasks[:] = ["Workout", "Study Python"]

    app.delete_task("not a number")

    assert app.tasks == ["Workout", "Study Python"]


def test_save_todos_writes_each_task_as_a_csv_row(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    app.tasks[:] = ["Workout", "Study Python"]

    app.save_todos()

    with open("todos.csv", newline="") as file:
        rows = list(csv.reader(file))

    assert rows == [["Workout"], ["Study Python"]]


def test_save_todos_creates_empty_csv_when_there_are_no_tasks(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    app.tasks.clear()

    app.save_todos()

    with open("todos.csv", newline="") as file:
        rows = list(csv.reader(file))

    assert rows == []


def test_load_todos_reads_saved_tasks_without_adding_duplicates(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    app.tasks[:] = ["Workout", "Study Python"]
    app.save_todos()
    app.tasks.clear()

    app.load_todos()
    app.load_todos()

    assert app.tasks == ["Workout", "Study Python"]


def test_load_todos_handles_a_missing_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    app.tasks.clear()

    app.load_todos()

    assert app.tasks == []


def test_run_menu_adds_views_saves_loads_and_deletes_tasks(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    app.tasks.clear()
    answers = iter(["1", "Check mail", "4", "1", "Temporary task", "5", "2", "3", "1", "6"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    app.run_menu()

    assert app.tasks == []
    assert "1. Check mail" in capsys.readouterr().out
