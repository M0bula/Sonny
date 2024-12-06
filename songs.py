import random

# Corrected Song Database
songs = [
    {
        "name": "Blowin' in the Wind",
        "lyrics": "How many roads must a man walk down before you call him a man?",
        "artist": "Bob Dylan",
        "famous_line": "The answer, my friend, is blowin' in the wind."
    },
    {
        "name": "Nonsense",
        "lyrics": "Think I only want one number in my phone. I might change your contact to 'Don't Leave Me Alone'.",
        "artist": "Sabrina Carpenter",
        "famous_line": "Lookin' at you got me thinkin' nonsense."
    },
    {
        "name": "Cupid",
        "lyrics": "A hopeless romantic all my life. Surrounded by couples all the time.",
        "artist": "FIFTY FIFTY",
        "famous_line": "I gave a second chance to Cupid, but now I'm left here feeling stupid."
    },
    {
        "name": "Yellow",
        "lyrics": "Look at the stars, look how they shine for you, and everything you do.",
        "artist": "Coldplay",
        "famous_line": "It was all yellow."
    },
    {
        "name": "Sunroof",
        "lyrics": "I'm blasting our favorite tunes.",
        "artist": "Nicky Youre",
        "famous_line": "I got my head out the sunroof."
    },
    {
        "name": "Hotel California",
        "lyrics": "On a dark desert highway, cool wind in my hair.",
        "artist": "Eagles",
        "famous_line": "Welcome to the Hotel California."
    },
    {
        "name": "Highway to Hell",
        "lyrics": "Living easy, living free, season ticket on a one-way ride.",
        "artist": "AC/DC",
        "famous_line": "I'm on the highway to hell."
    },
    {
        "name": "Call Me Maybe",
        "lyrics": "Before you came into my life, I missed you so bad.",
        "artist": "Carly Rae Jepsen",
        "famous_line": "Hey, I just met you, and this is crazy, but here's my number, so call me maybe."
    },
    {
        "name": "Sunflower",
        "lyrics": "Needless to say, I keep her in check. She was all bad-bad, nevertheless.",
        "artist": "Post Malone and Swae Lee",
        "famous_line": "You're a sunflower, I think your love would be too much."
    },
    {
        "name": "The Nights",
        "lyrics": "He said, 'One day you'll leave this world behind.'",
        "artist": "Avicii",
        "famous_line": "These are the nights that never die."
    },
    {
        "name": "Bohemian Rhapsody",
        "lyrics": "Is this the real life? Is this just fantasy?",
        "artist": "Queen",
        "famous_line": "Scaramouche, Scaramouche, will you do the Fandango?"
    },
    {
        "name": "Closer",
        "lyrics": "Pull me closer in the back seat of your Rover.",
        "artist": "The Chainsmokers ft. Halsey",
        "famous_line": "We ain't ever getting older."
    },
    {
        "name": "Take Me to Church",
        "lyrics": "Offer me that deathless death.",
        "artist": "Hozier",
        "famous_line": "Take me to church, I'll worship like a dog at the shrine of your lies."
    },
    {
        "name": "Counting Stars",
        "lyrics": "Lately, I've been, I've been losing sleep.",
        "artist": "OneRepublic",
        "famous_line": "No more counting dollars, we'll be counting stars."
    },
    {
        "name": "Uptown Funk",
        "lyrics": "This hit, that ice cold, Michelle Pfeiffer, that white gold.",
        "artist": "Mark Ronson ft. Bruno Mars",
        "famous_line": "Don't believe me, just watch."
    },
    {
        "name": "We Are Young",
        "lyrics": "Give me a second, I need to get my story straight.",
        "artist": "Fun.",
        "famous_line": "Tonight, we are young, so let's set the world on fire."
    },
    {
        "name": "Shivers",
        "lyrics": "I took an arrow to the heart. I never kissed a mouth that tastes like yours.",
        "artist": "Ed Sheeran",
        "famous_line": "Ooh, I love it when you do it like that."
    },
    {
        "name": "Killer Queen",
        "lyrics": "She keeps Moët et Chandon in her pretty cabinet.",
        "artist": "Queen",
        "famous_line": "She's a Killer Queen, gunpowder, gelatine."
    },
    {
        "name": "Demons",
        "lyrics": "When the days are cold and the cards all fold.",
        "artist": "Imagine Dragons",
        "famous_line": "It's where my demons hide."
    },
    {
        "name": "Shape of You",
        "lyrics": "The club isn't the best place to find a lover, so the bar is where I go.",
        "artist": "Ed Sheeran",
        "famous_line": "I'm in love with the shape of you."
    },
    {
        "name": "Hello",
        "lyrics": "Hello, it's me. I was wondering if after all these years you'd like to meet.",
        "artist": "Adele",
        "famous_line": "Hello from the other side."
    },
    {
        "name": "Old Town Road",
        "lyrics": "Can't nobody tell me nothing.",
        "artist": "Lil Nas X",
        "famous_line": "Yeah, I'm gonna take my horse to the old town road."
    }
]

def get_random_song():
    """Return a random song from the database."""
    return random.choice(songs)
