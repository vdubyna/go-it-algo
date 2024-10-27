class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, comment):
        self.replies.append(comment)

    def remove_reply(self, index):
        if 0 <= index < len(self.replies):
            self.replies[index].is_deleted = True
            self.replies[index].text = "Цей коментар було видалено."

    def display(self, level=0):
        indent = "    " * level
        deletion_notice = "(видалено)" if self.is_deleted else ""
        print(f"{indent}{self.author}: {self.text} {deletion_notice}")
        for reply in self.replies:
            reply.display(level + 1)

# Демонстрація використання класу Comment
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

root_comment.remove_reply(0)

root_comment.display()