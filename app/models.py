# app/models.py
class Task:
    tasks = []
    id_counter = 1

    @classmethod
    def create(cls, title):
        task = {"id": cls.id_counter, "title": title, "done": False}
        cls.tasks.append(task)
        cls.id_counter += 1
        return task

    @classmethod
    def list(cls):
        return cls.tasks

    @classmethod
    def update(cls, task_id, done):
        for task in cls.tasks:
            if task["id"] == task_id:
                task["done"] = done
                return task
        return None

    @classmethod
    def delete(cls, task_id):
        for task in cls.tasks:
            if task["id"] == task_id:
                cls.tasks.remove(task)
                return task
        return None
