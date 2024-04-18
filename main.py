import tkinter as tk
from tkinter import ttk
from Vocab import *
from customButton import TextLikeButton as TButton
from Quiz import Quiz


class GermanVocabularyGUI:
    def __init__(self):

        self.InitStyle()

        self.root = tk.Tk()
        self.root.title("German Vocabulary Practice")
        self.root.geometry("1050x660")  # Set the size of the GUI
        self.root.configure(bg=self.color_m)

        self.noun = Nomen()
        self.verb = Verb()
        self.adj = Adjektiv()
        self.vocabulary = Mixed()
        self.questions = []
        self.question_index = 0
        self.load_progress()

        style = ttk.Style()
        style.theme_use('classic')
        style.configure("TLabel", font=(self.font, 35), background=self.color_m, foreground=self.color_s)
        style.configure('TButton', font=(self.font, 20), foreground=self.color_d, background=self.color_s)
        style.configure("Custom.TCheckbutton",
                        font=(self.font, 20),
                        foreground=self.color_s,
                        background=self.color_m,
                        bd=0, highlightthickness=0,
                        indicatorbackground=self.color_m,
                        indicatorforeground=self.color_s,
                        indicatordiameter=15,
                        indicatorrelief="flat")
        # style.configure("Custom.TCheckbutton", indicatorbackground=self.color_m, indicatordiameter=15, indicatorrelief="flat")
        # style.map("Custom.TCheckbutton", indicatorbackground=[("active", "green")])
        # Main Menu Frame
        self.main_menu_frame = tk.Frame(self.root, bg=self.color_m)  # Set background color
        self.main_menu_frame.pack(expand=True)
        self.create_main_frame()

        self.practice_menu_frame = tk.Frame(self.root, bg=self.color_m)
        self.practice_meaning_frame = tk.Frame(self.root, bg=self.color_m)
        self.practice_gender_frame = tk.Frame(self.root, bg=self.color_m)
        self.practice_plural_frame = tk.Frame(self.root, bg=self.color_m)
        self.practice_verb_frame = tk.Frame(self.root, bg=self.color_m)
        self.practice_adj_frame = tk.Frame(self.root, bg=self.color_m)

        title4_label = ttk.Label(self.practice_verb_frame, text='verb', font=(self.font, 30))
        title5_label = ttk.Label(self.practice_adj_frame, text='adj', font=(self.font, 30))
        title4_label.pack(side=tk.TOP, anchor='n')
        title5_label.pack(side=tk.TOP, anchor='n')

        self.create_practice_menu_frame()

        self.create_practice_gender_frame(self.practice_gender_frame)
        self.create_practice_plural_frame(self.practice_plural_frame)
        self.create_practice_meaning_frame(self.practice_meaning_frame)

        self.word_menu_frame = tk.Frame(self.root, background=self.color_m)
        self.create_word_menu_frame()

        # Noun Frame
        self.noun_frame = tk.Frame(self.root, bg=self.color_m)
        self.create_word_frame(self.noun_frame, 1)

        # Verb Frame
        self.verb_frame = tk.Frame(self.root, bg=self.color_m)
        self.create_word_frame(self.verb_frame, 2)

        # Adjective Frame
        self.adj_frame = tk.Frame(self.root, bg=self.color_m)
        self.create_word_frame(self.adj_frame, 3)

    def InitStyle(self):
        self.color_m = '#6CA08B'
        self.color_d = '#0E705B'
        self.color_s = '#E2DDB7'
        self.font = 'Futura'

    # Create the main frame
    def create_main_frame(self):
        welcome_text_1 = 'Hello!'
        welcome_text_2 = 'Welcome to your vocabulary training app.'
        welcome_label_1 = ttk.Label(self.main_menu_frame, font=(self.font, 35), text=welcome_text_1)
        welcome_label_2 = ttk.Label(self.main_menu_frame, text=welcome_text_2)

        welcome_label_1.pack(side="top", anchor="center")
        welcome_label_2.pack(side="top", anchor="center", pady=(0, 50))

        # add buttons to menu page
        buttons_frame = tk.Frame(self.main_menu_frame, background=self.color_m)  # Separate frame for buttons
        buttons_frame.pack(expand=True)

        add_button = ttk.Button(buttons_frame, text="Manage word list",
                                    command=lambda: self.forward(self.main_menu_frame, self.word_menu_frame))
        practice_button = ttk.Button(buttons_frame, text="Practice",
                                   command=lambda: self.forward(self.main_menu_frame, self.practice_menu_frame))
        exit_Button = ttk.Button(buttons_frame, text="Exit",
                               command=self.exit_program)

        add_button.grid(row=1, column=0, pady=6, sticky="ew")
        practice_button.grid(row=0, column=0, pady=6, sticky="ew")
        exit_Button.grid(row=2, column=0, pady=6, sticky="ew")

    # Create the word menu frame
    def create_word_menu_frame(self):
        root = self.word_menu_frame
        nounButton = ttk.Button(root, text="Nomen", command=lambda: self.forward(root, self.noun_frame))
        verbButton = ttk.Button(root, text="Verb", command=lambda: self.forward(root, self.verb_frame))
        adjButton = ttk.Button(root, text="Adjektiv", command=lambda: self.forward(root, self.adj_frame))
        back_button = ttk.Button(root, text="Back", command=lambda: self.forward(root, self.main_menu_frame))

        nounButton.grid(row=0, column=0, pady=6, sticky="ew")
        verbButton.grid(row=1, column=0, pady=6, sticky="ew")
        #adjButton.grid(row=2, column=0, pady=6, sticky="ew")
        back_button.grid(row=3, column=0, pady=6, sticky='ew')

    # setting the layout of the practice gender frame
    def create_practice_gender_frame(self, root):

        self.start_frame_gender = tk.Frame(root, bg=self.color_m)
        self.start_frame_gender.pack(expand=True)
        title_label = ttk.Label(self.start_frame_gender, text='Ready?', font=(self.font, 40))
        start_button = ttk.Button(self.start_frame_gender, text='Start', command=lambda: self.start_quiz(root, 'gender', self.noun))
        back_button = ttk.Button(self.start_frame_gender, text='Back', command=lambda: self.forward(root, self.practice_menu_frame))
        title_label.grid(row=0, column=0, pady=(0, 20),padx=100)
        start_button.grid(row=1, column=0, pady=10, sticky='ew', padx=100)
        back_button.grid(row=2, column=0, pady=10, sticky='ew', padx=100)

    def create_practice_plural_frame(self, root):
        self.start_frame_plural = tk.Frame(root, bg=self.color_m)
        self.start_frame_plural.pack(expand=True)
        title_label = ttk.Label(self.start_frame_plural, text='Ready?', font=(self.font, 40))
        start_button = ttk.Button(self.start_frame_plural, text='Start', command=lambda: self.start_quiz(root, 'plural', self.noun))
        back_button = ttk.Button(self.start_frame_plural, text='Back', command=lambda: self.forward(root, self.practice_menu_frame))
        title_label.grid(row=0, column=0, pady=(0, 20), padx=100)
        start_button.grid(row=1, column=0, pady=10, sticky='ew', padx=100)
        back_button.grid(row=2, column=0, pady=10, sticky='ew', padx=100)

    def create_practice_meaning_frame(self, root):
        self.start_frame_meaning = tk.Frame(root, bg=self.color_m)
        self.start_frame_meaning.pack(expand=True)
        title_label = ttk.Label(self.start_frame_meaning, text='Ready?', font=(self.font, 40))
        start_button = ttk.Button(self.start_frame_meaning, text='Start',
                                  command=lambda: self.start_quiz(root, 'meaning', self.vocabulary))
        back_button = ttk.Button(self.start_frame_meaning, text='Back',
                                 command=lambda: self.forward(root, self.practice_menu_frame))
        title_label.grid(row=0, column=0, pady=(0, 20), padx=100)
        start_button.grid(row=1, column=0, pady=10, sticky='ew', padx=100)
        back_button.grid(row=2, column=0, pady=10, sticky='ew', padx=100)



    def start_quiz(self, root, attribute, vocab):
        if attribute == 'gender':
            self.start_frame_gender.pack_forget()
        if attribute == 'plural':
            self.start_frame_plural.pack_forget()
        if attribute == 'meaning':
            self.start_frame_meaning.pack_forget()
        quiz = Quiz(vocab, attribute=attribute)
        self.create_question_frame(root, quiz)

    def check_choice(self, button, buttons, feedback, index, quiz, current_frame, root):
        buttons[-2].configure(state='disabled')
        buttons[-1].configure(state='disabled')
        user_response = button.cget("text")
        answer = buttons[index].cget("text")

        if user_response == answer:
            quiz.if_correct[quiz.question_index] = 1
            quiz.score += 1
            quiz.vocab.gain_points(quiz.questions[quiz.question_index], quiz.attribute)
            button.configure(fg=self.color_d)
            feedback.configure(text="Correct!")

        elif user_response != answer:
            quiz.if_correct[quiz.question_index] = 0
            quiz.vocab.lose_points(quiz.questions[quiz.question_index], quiz.attribute)
            button.configure(fg='#DA3229')
            buttons[index].configure(fg=self.color_d)
            feedback.configure(text="Hmmmm...")

        for btn in buttons[:-2]:
            btn.unbind("<Button-1>")

        self.root.after(1000, lambda: self.next_question(current_frame, root, quiz))

    def create_question_frame(self, root, quiz):
        if quiz.question_index < len(quiz.questions):
            question_frame = tk.Frame(root, padx=20, bg=self.color_m)
            question_frame.pack(expand=True)
            word = quiz.questions[quiz.question_index]
            answer = quiz.vocab.words[word][quiz.attribute]
            quiz.answers[quiz.question_index] = answer
            question_text = 'fuck you'

            if quiz.attribute == 'gender':
                question_text = f" ___ {word}"
            if quiz.attribute == 'plural':
                question_text = f"{quiz.vocab.words[word]['gender']} {word},"
            if quiz.attribute == 'meaning':
                empty = ttk.Label(question_frame, text='')
                empty.pack(pady=50)
                if quiz.vocab.words[word]['pos'] == 'n.':
                    gender = self.noun.words[word].get('gender', '')
                    question_text = f'{gender} {word}'
                else:
                    question_text = f'{word}'
            
            index_text = f"Q{quiz.question_index + 1}. "
            question_label = ttk.Label(question_frame, text=index_text+question_text, font=(self.font, 30))
            question_label.pack(anchor='w')

            user_entry_frame = tk.Frame(question_frame, bg=self.color_m)
            user_entry_frame.config(width=300, height=80)
            user_entry_frame.pack(expand=True)

            feedbacklabel = ttk.Label(question_frame, text=' ', font=(self.font, 25))

            if quiz.attribute == 'gender':
                solutions = ['der', 'die', 'das']
                correct_index = solutions.index(answer)
                command = lambda btn: self.check_choice(btn, [btn1, btn2, btn3, skip_button, quit_button],
                                                        feedbacklabel, correct_index,
                                                        quiz, question_frame, root)
                btn1 = TButton(user_entry_frame, text=solutions[0], command=command)
                btn2 = TButton(user_entry_frame, text=solutions[1], command=command)
                btn3 = TButton(user_entry_frame, text=solutions[2], command=command)

                btn1.place(x=0, y=30)
                btn2.place(x=120, y=30)
                btn3.place(x=240, y=30)

            if quiz.attribute == 'plural':
                prompt = ttk.Label(user_entry_frame, text='die', font=(self.font, 30))
                prompt.place(x=45, y=30)
                answer_entry = tk.Entry(user_entry_frame, width=12, font=(self.font, 30),
                                         bg=self.color_m, fg=self.color_s, bd=0,
                                         highlightthickness=0
                                         )
                answer_entry.place(x=100, y=31)
                answer_entry.focus_set()  # Set the focus to the entry box
                answer_entry.bind("<Return>", lambda event: self.check_answer(answer_entry, feedbacklabel, quiz, question_frame, root))
                canvas = tk.Canvas(user_entry_frame, height=10, width=180, bg=self.color_m, highlightthickness=0)
                canvas.create_line(0, 0, 180, 0, width=3, fill=self.color_s)
                canvas.place(x=100, y=70)
            if quiz.attribute == 'meaning':
                user_entry_frame.config(width=300, height=240)
                if quiz.vocab.words[word]['pos'] == 'n.':
                    solutions = self.noun.get_solution(word, 'meaning', 4)
                elif quiz.vocab.words[word]['pos'] == 'v.':
                    solutions = self.verb.get_solution(word, 'meaning', 4)
                else:
                    solutions = self.adj.get_solution(word, 'meaning', 4)
                correct_index = solutions.index(answer)
                buttons = []
                index = ['A', 'B', 'C', 'D']
                command = lambda btn: self.check_choice(btn, buttons + [skip_button, quit_button], feedbacklabel,
                                                          correct_index, quiz, question_frame, root)
                for i in range(4):
                    text = index[i] + '. ' + solutions[i]
                    btn = TButton(user_entry_frame, text=text, font_size=25, command=command)
                    buttons.append(btn)
                    btn.place(x=0, y=55*i+30)

            feedbacklabel.pack(pady=10)

            button_frame = tk.Frame(question_frame, bg=self.color_m)
            button_frame.pack()

            skip_button = ttk.Button(button_frame, text="Skip", command=lambda: self.next_question(question_frame, root, quiz))
            skip_button.grid(row=1, column=1, pady=30, padx=40, ipadx=2, sticky='ew')
            quit_button = ttk.Button(button_frame, text="Quit", command=lambda: self.quit_practice(question_frame, root, quiz))
            quit_button.grid(row=1, column=0, pady=30, padx=40, sticky='ew')

            hint = 'haha'
            hint_frame = tk.Frame(question_frame, bg=self.color_m)
            hint_text = 'hint: '+hint
            hint_label = TButton(hint_frame, text=hint_text, overeffect='color', fg=self.color_m)
            if hint is not None:
                hint_frame.pack()
                hint_label.pack(anchor='center')


    def next_question(self, current_frame, root_frame, quiz):
        if quiz.question_index < len(quiz.questions)-1:
            current_frame.destroy()  # Destroy the current frame
            quiz.question_index = quiz.question_index + 1
            # print('current question index: ' + str(quiz.question_index))
            self.create_question_frame(root_frame, quiz)
        else:
            quiz.question_index = 0
            current_frame.destroy()
            self.create_summary_frame(root_frame, quiz)

    def create_summary_frame(self, root_frame, quiz):
        summary_frame = tk.Frame(root_frame, bg=self.color_m)
        summary_frame.pack(expand=True)
        score = quiz.score
        total = len(quiz.questions)
        score_label = ttk.Label(summary_frame, text=f'Your score is {score}/{total}', font=(self.font, 30))
        score_label.pack(pady=(0, 20))

        for i in range(len(quiz.questions)):
            word, answer = quiz.questions[i], quiz.answers[i]
            correct = quiz.if_correct[i]
            if correct:
                color = self.color_d
            elif correct == 0:
                color = '#DA3229'
            else:
                color = 'grey'

            question_text = ''
            if quiz.attribute == 'gender':
                question_text = f"{i+1}. {answer} {word}"
            if quiz.attribute == 'plural':
                question_text = f"{i+1}. die {answer}"
            if quiz.attribute == 'meaning':
                question_text = f"{i + 1}. {word}   {answer}"


            question_label = ttk.Label(summary_frame, text=question_text, font=(self.font, 20), foreground=color)
            question_label.pack(anchor='w')
        back_button = ttk.Button(summary_frame, text="Back", command=lambda: self.quit_practice(summary_frame, root_frame, quiz))
        back_button.pack(pady=(25, 0))

    def quit_practice(self, current_frame, root_frame, quiz):
        current_frame.destroy()
        if quiz.attribute == 'gender':
            self.start_frame_gender.pack(expand=True)
        if quiz.attribute == 'plural':
            self.start_frame_plural.pack(expand=True)
        if quiz.attribute == 'meaning':
            self.start_frame_meaning.pack(expand=True)
        root_frame.pack_forget()
        self.practice_menu_frame.pack(expand=True)
        quiz.question_index = 0

    def check_answer(self, entry, feedbacklabel, quiz, current_frame, root):
        user_response = entry.get().capitalize()
        answer = quiz.answers[quiz.question_index]
        if user_response == answer:
            quiz.if_correct[quiz.question_index] = 1
            quiz.score += 1
            quiz.vocab.gain_points(quiz.questions[quiz.question_index], quiz.attribute)
            feedbacklabel.config(text="Correct!")
            self.root.after(1000, lambda: self.next_question(current_frame, root, quiz))
        else:
            quiz.if_correct[quiz.question_index] = 0
            quiz.vocab.lose_points(quiz.questions[quiz.question_index], quiz.attribute)
            feedbacklabel.config(text=f'correct answer: {answer}')
            self.root.after(2000, lambda: self.next_question(current_frame, root, quiz))

    def create_practice_menu_frame(self):
        root = self.practice_menu_frame

        title = ['Vocab', 'Gender', 'Plural']
        frame = [
            self.practice_meaning_frame,
            self.practice_gender_frame,
            self.practice_plural_frame
            #self.practice_verb_frame,
            #self.practice_adj_frame
        ]
        for i in range(len(title)):
            button = ttk.Button(root, text=title[i], command=lambda k=i: self.forward(self.practice_menu_frame, frame[k], fill='both', expand=True))
            button.grid(row=i, column=0, pady=6, sticky='ew')

        back_button = ttk.Button(root, text="Back",
                                 command=lambda: self.forward(root, self.main_menu_frame))
        back_button.grid(row=5, column=0, pady=6, sticky='ew')

    def create_word_frame(self, root, type):
        title1_label = ttk.Label(root, text='word list', font=(self.font, 30))
        title1_label.grid(row=0, column=0, pady=(0, 30), padx=(0, 20))
        title2_label = ttk.Label(root, text='add/delete a word', font=(self.font, 30))
        title2_label.grid(row=0, column=1, pady=(0, 30))

        word_frame = tk.Frame(root, bg=self.color_m)
        word_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        if type == 1:
            self.create_add_noun_frame(word_frame)
            self.feedback_label1 = ttk.Label(root, text='', font=(self.font, 20))
            self.feedback_label1.grid(row=2, column=0, columnspan=2, pady=(2, 8))
        if type == 2:
            self.create_add_verb_frame(word_frame)
            self.feedback_label2 = ttk.Label(root, text='', font=(self.font, 20))
            self.feedback_label2.grid(row=2, column=0, columnspan=2, pady=(2, 8))
        if type == 3:
            self.create_add_adj_frame(word_frame)
            self.feedback_label3 = ttk.Label(root, text='', font=(self.font, 20))
            self.feedback_label3.grid(row=2, column=0, columnspan=2, pady=(2, 8))


        # Frame for viewing the word list
        word_list_frame = tk.Frame(root, bg=self.color_m)
        word_list_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        if type == 1:
            self.noun_list = tk.Text(word_list_frame, font=(self.font, 25), wrap="none", height=10, width=18,
                                     background=self.color_m,
                                     foreground=self.color_s, bd=0, highlightthickness=0)
            self.noun_list.pack()
            self.update_word_list(self.noun_list, self.noun)
        if type == 2:
            self.verb_list = tk.Text(word_list_frame, font=(self.font, 25), wrap='word', height=10, width=22,
                                     background=self.color_m,
                                     foreground=self.color_s, bd=0, highlightthickness=0)
            self.verb_list.pack()
            self.update_word_list(self.verb_list, self.verb)

        if type == 3:
            self.adj_list = tk.Text(word_list_frame, font=(self.font, 25), wrap="none", height=10, width=18,
                                     background=self.color_m,
                                     foreground=self.color_s, bd=0, highlightthickness=0)
            self.adj_list.pack()
            self.update_word_list(self.adj_list, self.adj)


        back_button = ttk.Button(root, text="Back",
                                 command=lambda: self.forward(root, self.word_menu_frame))
        back_button.grid(row=3, column=0, columnspan=2, pady=10)

    def forward(self, current_frame, target_frame, expand=True, fill=None):
        current_frame.pack_forget()
        target_frame.pack(expand=expand, fill=fill)

    def create_add_noun_frame(self, root):
        prompt = ['der/die/das:', 'word:', 'plural:', 'meaning:']
        prompt_label1 = ttk.Label(root, text=prompt[0], font=(self.font, 20))
        prompt_label2 = ttk.Label(root, text=prompt[1], font=(self.font, 20))
        prompt_label3 = ttk.Label(root, text=prompt[2], font=(self.font, 20))
        prompt_label5 = ttk.Label(root, text=prompt[3], font=(self.font, 20))
        prompt_label1.grid(row=0, column=0, padx=(0, 10), sticky='s')
        prompt_label2.grid(row=2, column=0, padx=(0, 10), pady=(5, 0), sticky='s')
        prompt_label3.grid(row=4, column=0, padx=(0, 10), pady=(5, 0), sticky='s')
        prompt_label5.grid(row=6, column=0, padx=(0, 10), pady=(5, 0), sticky='s')


        user_entry1 = tk.Entry(root, width=8, font=(self.font, 30), bg=self.color_m, fg=self.color_s, bd=0, highlightthickness=0)
        user_entry2 = tk.Entry(root, width=8, font=(self.font, 30), bg=self.color_m, fg=self.color_s, bd=0, highlightthickness=0)
        user_entry3 = tk.Entry(root, width=8, font=(self.font, 30), bg=self.color_m, fg=self.color_s, bd=0, highlightthickness=0)
        user_entry4 = tk.Entry(root, width=8, font=(self.font, 30), bg=self.color_m, fg=self.color_s, bd=0, highlightthickness=0)

        user_entry1.grid(row=0, column=1, sticky='s')
        user_entry2.grid(row=2, column=1, sticky='s')
        user_entry3.grid(row=4, column=1, sticky='s')
        user_entry4.grid(row=6, column=1, sticky='s')

        canvas1 = tk.Canvas(root, height=2, width=160, bg=self.color_m, highlightthickness=0)
        canvas1.create_line(0, 0, 160, 0, width=5, fill=self.color_s)
        canvas2 = tk.Canvas(root, height=2, width=160, bg=self.color_m, highlightthickness=0)
        canvas2.create_line(0, 0, 160, 0, width=5, fill=self.color_s)
        canvas3 = tk.Canvas(root, height=2, width=160, bg=self.color_m, highlightthickness=0)
        canvas3.create_line(0, 0, 160, 0, width=5, fill=self.color_s)
        canvas4 = tk.Canvas(root, height=2, width=160, bg=self.color_m, highlightthickness=0)
        canvas4.create_line(0, 0, 160, 0, width=5, fill=self.color_s)
        canvas1.grid(row=1, column=1)
        canvas2.grid(row=3, column=1)
        canvas3.grid(row=5, column=1)
        canvas4.grid(row=7, column=1)

        add_word_button = ttk.Button(root, text='Add',
                                     command=lambda: self.submit_noun(user_entry1, user_entry2, user_entry3, user_entry4,
                                                                      self.feedback_label1))
        add_word_button.grid(row=0, column=2, rowspan=7, padx=(30, 0), sticky='esw')

        separator = ttk.Label(root, text='')
        separator.grid(row=8, pady=20)

        prompt_label5 = ttk.Label(root, text='word to delete:', font=(self.font, 20))
        prompt_label5.grid(row=9, column=0, sticky='s')
        user_entry5 = tk.Entry(root, width=8, font=(self.font, 30), bg=self.color_m, fg=self.color_s, bd=0,
                               highlightthickness=0)
        user_entry5.grid(row=9, column=1)

        canvas5 = tk.Canvas(root, height=2, width=160, bg=self.color_m, highlightthickness=0)
        canvas5.create_line(0, 0, 160, 0, width=5, fill=self.color_s)
        canvas5.grid(row=10, column=1)

        delete_button = ttk.Button(root, text='Delete', command=lambda: self.submit_delete_word(user_entry5, self.noun_list, self.noun, self.feedback_label1))
        delete_button.grid(row=9, column=2, rowspan=3, padx=(30, 0), sticky='ew')

    def create_add_verb_frame(self, root):
        prompt = ['infinitiv:', 'ich:', 'du:', 'er/sie/es:', 'perfekt:', 'meaning:']
        user_entry = [None] * 6
        for i in range(len(prompt)):
            prompt_label = ttk.Label(root, text=prompt[i], font=(self.font, 20))
            prompt_label.grid(row=2*i, column=0, padx=(0, 10), sticky='s')
            user_entry[i] = tk.Entry(root, width=8, font=(self.font, 20), bg=self.color_m, fg=self.color_s, bd=0,
                                   highlightthickness=0)
            user_entry[i].grid(row=2*i, column=1, sticky='s')
            canvas = tk.Canvas(root, height=10, width=160, bg=self.color_m, highlightthickness=0)
            canvas.create_line(0, 0, 160, 0, width=3, fill=self.color_s)
            canvas.grid(row=2*i+1, column=1)


        add_word_button = ttk.Button(root, text='Add', command=lambda: self.submit_verb(user_entry))
        add_word_button.grid(row=0, column=2, rowspan=13, padx=(30, 0), sticky='esw')

        separator = ttk.Label(root, text='')
        separator.grid(row=14, pady=10)

        prompt_label2 = ttk.Label(root, text='word to delete:', font=(self.font, 20))
        prompt_label2.grid(row=15, column=0, sticky='s')
        user_entry5 = tk.Entry(root, width=8, font=(self.font, 30), bg=self.color_m, fg=self.color_s, bd=0,
                               highlightthickness=0)
        user_entry5.grid(row=15, column=1)

        canvas5 = tk.Canvas(root, height=2, width=160, bg=self.color_m, highlightthickness=0)
        canvas5.create_line(0, 0, 160, 0, width=5, fill=self.color_s)
        canvas5.grid(row=16, column=1)

        delete_button = ttk.Button(root, text='Delete', command=lambda: self.submit_delete_word(user_entry5, self.verb_list, self.verb, self.feedback_label2))
        delete_button.grid(row=15, column=2, rowspan=3, padx=(30, 0), sticky='ew')

    def create_add_adj_frame(self, root):
        pass
    def submit_noun(self, entry1, entry2, entry3, entry4, feedbacklabel):
        gender = entry1.get().lower().strip()
        word = entry2.get().capitalize().strip()
        plural = entry3.get().capitalize().strip()
        meaning = entry4.get().lower().strip()
        noun = [word, gender, plural, meaning]
        if meaning != '':
            self.vocabulary.add_word(word, meaning, 'n.')

        if self.noun.add_word(noun):
            feedbacklabel.config(text='Added!')
            self.root.after(2000, lambda: feedbacklabel.config(text=''))
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')
            entry3.delete(0, 'end')
            entry4.delete(0, 'end')
            self.update_word_list(self.noun_list, self.noun)

        else:
            feedbacklabel.config(text='Emmm..maybe check your input again')
            self.root.after(2000, lambda: feedbacklabel.config(text=''))

    def submit_verb(self, user_entry):
        verb = [entry.get().lower().strip() for entry in user_entry]
        word, ich, du, es, past, meaning = verb
        if meaning != '':
            self.vocabulary.add_word(word, meaning, 'v.')

        if self.verb.add_word(verb):
            self.feedback_label2.config(text='Added!')
            self.root.after(2000, lambda: self.feedback_label2.config(text=''))
            for entry in user_entry:
                entry.delete(0, 'end')
            self.update_word_list(self.verb_list, self.verb)
        else:
            self.feedback_label2.config(text='Emmm..maybe check your input again')
            self.root.after(2000, lambda: self.feedback_label2.config(text=''))

    def submit_delete_word(self, entry, vocab_list, vocab, feedback_label):
        if vocab == self.noun:
            word = entry.get().capitalize().strip()
        else:
            word = entry.get().lower().strip()
        if vocab.delete_word(word):
            feedback_label.config(text='deleted!')
            self.update_word_list(vocab_list, vocab)
            self.root.after(2000, lambda: feedback_label.config(text=''))
        else:
            feedback_label.config(text='cannot find word')
            self.root.after(2000, lambda: feedback_label.config(text=''))
        entry.delete(0, 'end')

    def update_word_list(self, vocab_list, vocab):

        word_list = vocab.get_word_list()

        # Clear the current content and insert the updated word list
        vocab_list.delete("1.0", tk.END)
        for word_entry in word_list:
            vocab_list.insert(tk.END, f"{word_entry}\n")

    def save_progress(self):
        self.noun.save_progress()
        self.verb.save_progress()
        self.vocabulary.save_progress()

    def load_progress(self):
        self.noun.load_progress()
        self.verb.load_progress()
        self.vocabulary.load_progress()


    def exit_program(self):
        self.save_progress()
        self.root.destroy()



if __name__ == "__main__":
    gui = GermanVocabularyGUI()
    gui.root.mainloop()
