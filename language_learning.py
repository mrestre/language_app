import tkinter as tk
import random

# Test Words
word_dict = {
    "apple": "manzana",
    "banana": "plátano",
}

class LanguageLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Learning App")
        self.root.geometry("400x300")

        self.score = 0
        self.total_questions = 0
        self.word_iterator = iter(word_dict.items())

        self.label = tk.Label(root, text="Welcome to the Language Learning App!", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.question_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.question_label.pack()

        self.answer_entry = tk.Entry(root, font=("Helvetica", 12))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=("Helvetica", 12))
        self.submit_button.pack()

        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.feedback_label.pack(pady=10)

        self.next_question()

    def next_question(self):
        try:
            english_word, self.correct_translation = next(self.word_iterator)
            self.question_label.config(text=f"What is the Spanish translation of '{english_word}'?")
            self.answer_entry.delete(0, tk.END)
        except StopIteration:
            self.show_final_score()

    def check_answer(self):
        user_translation = self.answer_entry.get().strip().lower()
        if user_translation == self.correct_translation.lower():
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text=f"Wrong! The correct answer is '{self.correct_translation}'.", fg="red")
        self.total_questions += 1
        self.update_score()
        self.next_question()

    def update_score(self):
        self.label.config(text=f"Score: {self.score}/{self.total_questions}")

    def show_final_score(self):
        self.label.config(text=f"Quiz Completed! Final Score: {self.score}/{self.total_questions}")
        self.question_label.config(text="")
        self.answer_entry.destroy()
        self.submit_button.destroy()
        self.feedback_label.destroy()

def main():
    root = tk.Tk()
    app = LanguageLearningApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()