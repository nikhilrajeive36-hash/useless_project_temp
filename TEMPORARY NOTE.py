import tkinter as tk
import random

class TemporaryNotepad:

    def __init__(self, root):

        self.root = root
        self.root.title("Temporary Notepad")
        self.root.geometry("1000x650")
        self.root.configure(bg="#C2B280LJFJCJHB,MVN")

        self.after_id = None
        self.deleted_count = 0

        self.messages = [
            "Solving problems that never existed.",
    "Maximum effort, minimum usefulness.",
    "Innovation has officially peaked.",
    "Built after rejecting all good ideas.",
    "A solution desperately searching for a problem.",
    "Future generations did not ask for this.",
    "Productivity left the chat.",
    "Congratulations. You blinked into a website.",
    "This could have been an Excel sheet.",
    "AI was available. We chose this.",
    "Millions of years of evolution led to this.",
    "Nobody asked. We delivered anyway.",
    "The problem is not the solution.",
    "Technically, it works.",
    "Useful? Absolutely not.",
        ]

        title = tk.Label(
            root,
            text="DEATH NOTEPAD",
            font=("papyrus", 28, "bold"),
            bg="#C2B280",
            fg="#ff5555"
        )
        title.pack(pady=15)

        self.counter = tk.Label(
            root,
            text="Notes Deleted: 0",
            font=("Arial", 14, "bold"),
            bg="#111111",
            fg="#00ff88"
        )
        self.counter.pack()

        self.message = tk.Label(
            root,
            text="Everything disappears ",
            font=("Arial", 12, "italic"),
            bg="#111111",
            fg="white"
        )
        self.message.pack(pady=10)

        self.textbox = tk.Text(
            root,
            font=("Consolas", 16),
            bg="#1a1a1a",
            fg="white",
            insertbackground="white"
        )
        self.textbox.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.textbox.bind("<KeyRelease>", self.reset_timer)

        root.bind("<Escape>", self.close_app)

    def reset_timer(self, event=None):

        if self.after_id:
            self.root.after_cancel(self.after_id)

        self.after_id = self.root.after(
            1000,
            self.delete_text
        )

    def delete_text(self):

        content = self.textbox.get("1.0", tk.END).strip()

        if content:

            self.deleted_count += 1

            self.counter.config(
                text=f"Notes Deleted: {self.deleted_count}"
            )

            self.message.config(
                text=random.choice(self.messages)
            )

            self.textbox.delete(
                "1.0",
                tk.END
            )

    def close_app(self, event=None):
        self.root.destroy()


if __name__ == "__main__":

    root = tk.Tk()

    app = TemporaryNotepad(root)

    root.mainloop()