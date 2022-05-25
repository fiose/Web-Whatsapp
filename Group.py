class Group:
    def __init__(self, name: str, amount_unread_messages: int, is_muted: bool):
        self.name = name
        self.amount_unread_messages = amount_unread_messages
        self.is_muted = is_muted

    def __repr__(self):
        return f'Group(name: {self.name}, amount_unread_messages: {self.amount_unread_messages}, is_muted: {self.is_muted})'
