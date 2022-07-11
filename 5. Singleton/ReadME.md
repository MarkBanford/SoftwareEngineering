Sometimes you need an object in an app where there is ONLY 1 instance (i.e Database connection, Account Balance). 
With Singleton pattern you can enforce  that even if a second instance is created, it will still refer to the original.
Singleton should not contain any reference to self, but use static variable, static methods and/or class methods


EXAMPLE

3 games are created, they are all independent instances created from their own class, but they all share the same
leaderboard. The leaderboard is a singleton.
Each game independently adds a winner, and all games can read the altered leaderboard regardless of which game
updated it