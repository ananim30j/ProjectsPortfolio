import redis
import json
import random

class Chatbot:
    def __init__(self, host='redis', port=6379):
        """
        [Task 1: Setting up Redis connection]
        Connect to Redis running on 'redis' host (in a Docker container) on the default port 6379.
        """
        self.client = redis.StrictRedis(host=host, port=port)
        self.pubsub = self.client.pubsub()  # Allows subscribing to and publishing messages to channels
        self.username = None  # No user identified initially
        
        # [Task 5: Storing mock weather updates in Redis]
        weather_data = {
            "New York": "Sunny, 75°F", "London": "Rainy, 60°F", "San Francisco": "Humid, 93°F",
            "Tokyo": "Cloudy, 55°F", "Mumbai": "Rainy, 88°F", "Paris": "Overcast, 64°F",
            "Sydney": "Sunny, 77°F", "Berlin": "Windy, 58°F", "Moscow": "Snowy, 30°F",
            "Cairo": "Hot, 102°F", "Buenos Aires": "Mild, 68°F", "Cape Town": "Breezy, 65°F",
            "Rio de Janeiro": "Humid, 85°F", "Beijing": "Smoggy, 50°F", "Dubai": "Hot, 110°F",
            "Mexico City": "Hazy, 72°F", "Singapore": "Thunderstorms, 90°F", "Toronto": "Cold, 45°F",
            "Rome": "Sunny, 70°F", "Vancouver": "Rainy, 55°F"
        }
        
        for city, weather in weather_data.items():
            self.client.set(city.lower(), weather)  # Store weather data in Redis for easy retrieval

        # [Task 7: Extra command - recipe suggestion feature]
        self.recipe_data = {
            "chicken": """🍗 Grilled Chicken with Lemon:
Ingredients:
- Chicken, Lemon, Olive Oil, Garlic
Steps:
1. Marinate chicken with lemon juice, olive oil, and garlic.
2. Preheat grill to medium heat and cook for 6-8 minutes per side.""",
            
            "pasta": """🍝 Spaghetti Carbonara:
Ingredients:
- Spaghetti, Eggs, Parmesan, Bacon
Steps:
1. Cook spaghetti and fry bacon.
2. Mix with whisked eggs and cheese, then stir in bacon.""",
            
            "beef": """🥩 Beef Stroganoff:
Ingredients:
- Beef, Mushrooms, Onions, Sour Cream
Steps:
1. Sauté beef, onions, mushrooms.
2. Add sour cream and simmer for 10 minutes.""",
            
            "salmon": """🍣 Baked Salmon:
Ingredients:
- Salmon, Olive Oil, Garlic, Lemon
Steps:
1. Rub salmon with oil, garlic, lemon.
2. Bake at 375°F for 15-20 minutes.""",
            
            "vegetables": """🥗 Stir-fried Vegetables:
Ingredients:
- Broccoli, Carrots, Bell Peppers, Soy Sauce
Steps:
1. Stir-fry vegetables and toss with soy sauce.""",
        }

        for ingredient, recipe in self.recipe_data.items():
            self.client.set(f"recipe:{ingredient.lower()}", recipe)  # Store recipes in Redis

        # [Task 7: Extra command - joke feature]
        jokes_data = [
            "Why don't skeletons fight each other? They don't have the guts! 😂",
            "What do you call fake spaghetti? An impasta! 🍝",
            "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
            "How does a penguin build its house? Igloos it together! 🐧",
            "What do you call cheese that isn't yours? Nacho cheese! 🧀"
        ]
        for i, joke in enumerate(jokes_data):
            self.client.set(f"joke:{i}", joke)  # Store jokes in Redis

        # [Task 7: Extra command - horoscope feature]
        horoscope_data = {
            "aries": "🔮 Aries: Take bold action today!", "taurus": "🔮 Taurus: Patience is your strength today.",
            "gemini": "🔮 Gemini: Expect exciting communication.", "cancer": "🔮 Cancer: Focus on family today.",
            "leo": "🔮 Leo: Share your bold ideas!", "virgo": "🔮 Virgo: Details will lead to success.",
            "libra": "🔮 Libra: Balance brings peace.", "scorpio": "🔮 Scorpio: Trust your instincts.",
            "sagittarius": "🔮 Sagittarius: Adventure awaits!", "capricorn": "🔮 Capricorn: Hard work pays off.",
            "aquarius": "🔮 Aquarius: Creativity brings breakthroughs.", "pisces": "🔮 Pisces: Follow your intuition."
        }

        for sign, horoscope in horoscope_data.items():
            self.client.set(sign.lower(), horoscope)  # Store horoscopes in Redis
        
        # [Task 4: Users should be able to join or leave a channel]
        self.available_channels = ["sports", "food", "news", "tech", "music"]  # Channels

    def introduce(self):
        """
        [Task 2: Chatbot initialization and introduction]
        Display a welcome message and list of available commands.
        """
        intro = """
        ╔══════════════════════════════════════════════════════╗
        ║     Welcome! I am PowerHouse, your friendly chatbot! ║
        ╚══════════════════════════════════════════════════════╝
        Commands you can use:
        1. !help: List of available commands
        2. !identify: Identify yourself
        3. !whoami: Get information about your user
        4. !weather <city>: Get a weather update
        5. !fact: Get a random fun fact
        6. !recipe <ingredient>: Get a recipe suggestion
        7. !joke: Get a random joke
        8. !horoscope <zodiac_sign>: Get your daily horoscope
        9. !join <channel>: Join a channel (available channels: sports, food, news, tech, music)
        10. !leave <channel>: Leave a channel
        11. !message <channel> <message>: Send a message to a channel
        """
        print(intro)

    def identify(self):
        """
        [Task 3: User identification]
        Conversational prompt to gather username, age, gender, and location.
        """
        print("👋 Let's get to know you!")
        username = input("📝 Enter your username: ").strip()
        age = input(f"👶 How old are you, {username}? ").strip()
        gender = input("⚧ Your gender (M/F/Other): ").strip().capitalize()
        location = input(f"📍 Where are you from, {username}? ").strip()
        
        user_info = {'username': username, 'age': age, 'gender': gender, 'location': location}
        self.client.set(f"user:{username}", json.dumps(user_info))  # Store in Redis
        self.username = username  # Set the bot's active username
        print(f"✔ Info stored, {username}! You're all set! 🎉")

    def join_channel(self, channel):
        """[Task 4: Join a channel]"""
        if channel not in self.available_channels:
            print(f"⚠ Channel '{channel}' is not available. Choose from: {', '.join(self.available_channels)}")
        else:
            self.pubsub.subscribe(channel)  # Subscribe to the channel
            print(f"✔ Joined channel: {channel.upper()}")

    def leave_channel(self, channel):
        """[Task 4: Leave a channel]"""
        if channel not in self.available_channels:
            print(f"⚠ Not in the channel '{channel}'.")
        else:
            self.pubsub.unsubscribe(channel)  # Unsubscribe from the channel
            print(f"✔ Left channel: {channel.upper()}")

    def send_message(self, channel, message):
        """[Task 4: Send message to a channel]"""
        if channel not in self.available_channels:
            print(f"⚠ Channel '{channel}' is unavailable. You must join first.")
        else:
            self.client.publish(channel, f"{self.username}: {message}")  # Publish to channel
            print(f"📢 Message sent to {channel.upper()}: {message}")

    def read_message(self):
        """[Task 4: Read messages from channels]"""
        print("👂 Listening for messages...")
        for item in self.pubsub.listen():
            if item['type'] == 'message':
                print(f"🔔 [{item['channel'].decode('utf-8').upper()}] {item['data'].decode('utf-8')}")

    def process_commands(self, message):
        """Handles commands and responds accordingly."""
        if message.startswith('!help'):
            self.introduce()
        elif message.startswith('!whoami'):
            # [Task 5: Display user information with !whoami]
            if self.username:
                user_data = self.client.get(f"user:{self.username}")
                if user_data:
                    user_info = json.loads(user_data)
                    print(f"👤 {self.username}'s Info:\n{user_info}")
                else:
                    print(f"⚠ No info for '{self.username}'.")
            else:
                print("⚠ You haven't identified yourself yet. Use the !identify command.")
        elif message.startswith('!identify'):
            self.identify()
        elif message.startswith('!fact'):
            # [Task 5: Provide random fun fact]
            facts = [
                "Bananas are berries, strawberries are not.", "Honey never spoils.",
                "Octopuses have three hearts.", "Sharks existed before trees.",
                "More stars in the universe than grains of sand.", "Venus day > Venus year.",
                "Wombat poop is cube-shaped.", "Hot water freezes faster than cold.",
                "Cleopatra closer to iPhone than pyramids.", "Immortal jellyfish exists."
            ]
            fact = random.choice(facts)
            self.client.publish("fact_channel", fact)  # Publish to Redis
            print(f"🔎 Fun Fact: {fact}")
        elif message.startswith('!weather'):
            try:
                _, city = message.split(maxsplit=1)
                weather = self.client.get(city.lower())
                if weather:
                    print(f"🌤️ Weather in {city}: {weather.decode('utf-8')}")
                else:
                    print(f"⚠ No weather info for {city}.")
            except ValueError:
                print("⚠ Format: !weather <city>")
        elif message.startswith('!recipe'):
            try:
                _, ingredient = message.split()
                recipe = self.client.get(f"recipe:{ingredient.lower()}")
                if recipe:
                    print(f"🍽️ Recipe for {ingredient.capitalize()}:\n{recipe.decode('utf-8')}")
                else:
                    print(f"⚠ No recipe for {ingredient}.")
            except ValueError:
                print("⚠ Format: !recipe <ingredient>")
        elif message.startswith('!joke'):
            joke_count = 5
            joke_index = random.randint(0, joke_count - 1)
            joke = self.client.get(f"joke:{joke_index}")
            if joke:
                print(f"😂 Joke: {joke.decode('utf-8')}")
        elif message.startswith('!horoscope'):
            try:
                _, sign = message.split(maxsplit=1)
                horoscope = self.client.get(sign.lower())
                if horoscope:
                    print(f"🔮 Horoscope for {sign.capitalize()}: {horoscope.decode('utf-8')}")
                else:
                    print(f"⚠ No horoscope info for {sign.capitalize()}.")
            except ValueError:
                print("⚠ Format: !horoscope <zodiac_sign>")

    def direct_message(self, message):
        """Handles user input directly."""
        self.process_commands(message)

if __name__ == "__main__":
    bot = Chatbot()
    bot.introduce()

    # Start reading messages in the background
    import threading
    threading.Thread(target=bot.read_message, daemon=True).start()

    # Main interaction loop
    while True:
        user_input = input("You: ").strip()
        print(f"Received input: {user_input}")
        
        # Conversational identification
        if user_input.startswith('!identify'):
            bot.identify()
        elif user_input.startswith('!join'):
            try:
                _, channel = user_input.split()
                bot.join_channel(channel)
            except ValueError:
                print("⚠ Provide the channel name.")
        elif user_input.startswith('!leave'):
            try:
                _, channel = user_input.split()
                bot.leave_channel(channel)
            except ValueError:
                print("⚠ Provide the channel name.")
        elif user_input.startswith('!message'):
            try:
                _, channel, *msg = user_input.split()
                message = " ".join(msg)
                bot.send_message(channel, message)
            except ValueError:
                print("⚠ Provide message in the format: !message <channel> <message>")
        else:
            bot.direct_message(user_input)
