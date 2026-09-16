import random




AFFIRMATIONS = [

    "Asking for help is a sign of self-respect and self-awareness.",
    "Changing my mind is a strength, not a weakness.",
    "Every decision I make is supported by my whole and inarguable experience.",
    "I affirm and encourage others, as I do myself.",
    "I alone hold the truth of who I am.",
    'A sticky note held up reading, "I alone hold the trust of who I am".',
    "I am allowed to ask for what I want and what I need.",
    "I am allowed to feel good.",
    "I am capable of balancing ease and effort in my life.",
    "I am complete as I am, others simply support me.",
    "I am content and free from pain.",
    "I am doing the work that works for me.",
    "I am good and getting better.",
    "I am growing and I am going at my own pace.",
    "I am held and supported by those who love me.",
    "I am in charge of how I feel and I choose to feel happy.",
    "I am listening and open to the messages the universe has to offer today.",
    "I am loved and worthy.",
    "I am more than my circumstances dictate.",
    "I am open to healing.",
    "I am optimistic because today is a new day.",
    'A sticky note being held up to the sky, reading "I hold community for others, and am held in community by others".',
    "I am peaceful and whole.",
    "I am proof enough of who I am and what I deserve.",
    "I am responsible for myself, and I start there.",
    "I am safe and surrounded by love and support.",
    "I am still learning so it’s okay to make mistakes.",
    "I am understood and my perspective is important.",
    "I am valued and helpful.",
    "I am well-rested and excited for the day.",
    "I am worthy of investing in myself.",
    "I belong here, and I deserve to take up space.",
    "I breathe in healing, I exhale the painful things that burden my heart.",
    "I breathe in trust, I exhale doubt.",
    "I can be soft in my heart and firm in my boundaries.",
    "I can control how I respond to things that are confronting.",
    "I can hold two opposing feelings at once, it means I am processing.",
    "I celebrate the good qualities in others and myself.",
    "I deserve an affirming touch on my own terms.",
    "I deserve information and I deserve moments of silence, too.",
    "I deserve self-respect and a clean space.",
    "I do all things in love.",
    "I do not have to linger in dark places; there is help for me here.",
    "I do not pretend to be anyone or anything other than who I am.",
    "I do not rise and fall for another.",
    "I do not rush through my life, I temper speed with stillness.",
    "I embrace change seamlessly and rise to the new opportunity it presents.",
    'A sticky note held up reading "I nourish myself with kind words and joyful foods".',
    "I embrace the questions in my heart and welcome the answers in their own time.",
    "I grow towards my interests, like a plant reaching for the sun.",
    "I have come farther than I would have ever thought possible, and I’m learning along the way.",
    "I have everything I need to succeed.",
    "I hold community for others, and am held in community by others.",
    "I hold wisdom beyond knowledge.",
    "I invite abundance and a generous heart.",
    "I invite art and music into my life.",
    "I leave room in my life for spontaneity.",
    "I let go of the things that sit achingly out of reach.",
    "I look forward to tomorrow and the opportunities that await me.",
    "I love that I love what I love.",
    "I make decisions based on a good gut, I make changes based on a growing heart.",
    "I make time to experience grief and sadness when necessary.",
    "I nourish myself with kind words and joyful foods.",
    "I practice gratitude for all that I have, and all that is yet to come.",
    "I release the fears that do not serve me.",
    "I respect the cycle of the seasons.",
    "I seek out mystery in the ordinary.",
    "I strive for joy, not for perfection.",
    'A sticky note held up, reading "I welcome the wisdom that comes with growing older".',
    "I tell the truth about who I am and what I need from others.",
    "I uplift my joy and the joy of others.",
    "I welcome the wisdom that comes with growing older.",
    "I welcome what is, I welcome what comes.",
    "I will allow myself to evolve.",
    "Letting go creates space for opportunities to come.",
    "My body is beautiful in this moment and at its current size.",
    "My body is worthy of being cared for and adorned in beautiful garments.",
    "My feelings deserve names, deserve recognition, deserve to be felt.",
    "My heart is open to helpfulness from myself and from others.",
    "My heart knows its own way.",
    "My life is not a race or competition.",
    "My perspective is unique and important.",
    "My pleasure does not require someone else’s pain.",
    "My sensitivity is beautiful, and my feelings and emotions are valid.",
    'A sticky note held up in front of a brick wall, reading "My sensitivity is beautiful, and my feelings and emotions are valid".',
    "My weirdness is wonderful.",
    "Saying “no” is an act of self-affirmation, too.",
    "Sometimes the work is resting.",
    "There is growth in stillness.",
    "There is peace in changing your mind when it is done in love.",
    "There is poetry in everything, if I look for it.",
    "There is room for me at the table.",
    "There is something in this world that only I can do. That is why I am here.",
    "There is strength in quiet, there is vulnerability in being loud.",
    "Today I celebrate that I am younger than I’m ever going to be.",
    "Today is an opportunity to grow and learn.",
    "When I feel fear, I feed trust.",
    "When I focus on my reason for being, I am infinitely brave.",
    "When I forgive myself, I free myself.",
    "When I release shame, I move into myself more beautifully.",
    "When I root into the earth, the earth rises to support me.",
    "When I speak my needs, I receive them abundantly.",
    "When I talk to myself as I would a friend, I see all my best qualities and I allow myself to shine.",
    "Words may shape me, but they do not make me. I am here already."
]


class AffirmationApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Daily Affirmation")
    self.root.geometry("500x350")
    self.root.config(bg="#F4F6F9")

    # Center the window on the screen
    self.center_window()

    # Define Fonts
    self.title_font = font.Font(family="Helvetica", size=18, weight="bold")
    self.quote_font = font.Font(family="Georgia", size=14, slant="italic")
    self.button_font = font.Font(family="Helvetica", size=11, weight="bold")

    # Build UI Components
    self.create_widgets()

    # Show first affirmation
    self.new_affirmation()

  def center_window(self):
    self.root.update_idletasks()
    width = self.root.winfo_width()
    height = self.root.winfo_height()
    x = (self.root.winfo_screenwidth() // 2) - (width // 2)
    y = (self.root.winfo_screenheight() // 2) - (height // 2)
    self.root.geometry(f"{width}x{height}+{x}+{y}")

  def create_widgets(self):
    # App Header / Title
    title_label = tk.Label(
        self.root,
        text="✨ Your Daily Dose of Positivity ✨",
        font=self.title_font,
        bg="#F4F6F9",
        fg="#2C3E50",
    )
    title_label.pack(pady=(30, 20))

    # Affirmation Display Box (using a Label with text wrapping)
    self.affirmation_label = tk.Label(
        self.root,
        text="",
        font=self.quote_font,
        bg="#FFFFFF",
        fg="#34495E",
        wraplength=400,
        justify="center",
        relief="flat",
        padx=20,
        pady=20,
    )
    self.affirmation_label.pack(
        pady=10, padx=30, fill="both", expand=True
    )  # Added padding inside frame concept via Label

    # New Affirmation Button
    btn = tk.Button(
        self.root,
        text="Give Me Another",
        font=self.button_font,
        bg="#3498DB",
        fg="#FFFFFF",
        activebackground="#2980B9",
        activeforeground="#FFFFFF",
        relief="flat",
        padx=15,
        pady=10,
        command=self.new_affirmation,
    )
    btn.pack(pady=(10, 30))

  def new_affirmation(self):
    # Pick a random affirmation from the list
    chosen = random.choice(AFFIRMATIONS)
    self.affirmation_label.config(text=f'"{chosen}"')


if __name__ == "__main__":
  root = tk.Tk()
  app = AffirmationApp(root)
  root.mainloop()
