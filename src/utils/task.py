class Task:
    def __init__(
            self, title=None, description=None, due_date=None, priority=None
    ):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def markdone(self):
        self.completed = True
