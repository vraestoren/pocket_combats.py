# <img src="https://play-lh.googleusercontent.com/rzNSMs_pLFbOmbew09S_pYbRYzTdXIOJvEy5MZLYNRJXQ8WKF2B7miuA7Xa_-UmCag=w240-h480-rw" width="28" style="vertical-align:middle;" /> pocket_combats.py

> Mobile-API for [Pocket Combats](https://game.pocketcombats.com) a mobile RPG combat game.

## Quick Start

```python
from pocket_combats import PocketCombats

game = PocketCombats()
game.login_with_token("your_auth_token")

player = game.get_current_player()
print(player)
```

## Usage

### Authentication

```python
# Login with existing token
game.login_with_token("your_auth_token")

# Register with Google
game.register(google_id_token="...", username="Hero")

# Register a new character
game.register_new_character(google_id_token="...", username="Hero2")
```

### Player

```python
game.get_current_player()
game.get_equipment()
game.get_skills()
game.get_backpack()
```

### Combat

```python
# Move to a location
game.route_location(route_id=3)

# Start a battle
game.start_battle(battle_id="abc123", hp=100, position=1)

# Attack during battle
game.attack_monster(action_id=1, target_id=0)

# Get current battle state
game.get_current_battle()

# Finish battle
game.finish_battle()

# Pick up dropped item
game.pick_up_item(item_id=42)

# Get monster info
game.get_monster_info("goblin")
```

### Location

```python
game.get_location_info()
game.route_location(route_id=1)
```

### Quests

```python
game.get_quests_journal()
game.get_battles_history()
```

### Friends

```python
game.get_friends()
game.suggest_friends("alice")
game.send_friend_request(user_id=123)
game.cancel_friend_request(user_id=123)
```

### Chat

```python
game.get_chat_channels()
game.get_chat_history()
game.send_message(channel_id=1, text="Hello!")
```

## API Reference

| Method | Description |
|---|---|
| `login_with_token(token)` | Authenticate with an auth token |
| `register(google_id_token, username)` | Register a new account |
| `register_new_character(google_id_token, username)` | Register a new character |
| `get_current_player()` | Get your player info |
| `get_equipment()` | Get equipped items |
| `get_skills()` | Get available skills |
| `get_backpack()` | Get backpack contents |
| `get_location_info()` | Get current location |
| `route_location(route_id)` | Travel to a location |
| `start_battle(battle_id, hp, position)` | Start a battle |
| `attack_monster(action_id, target_id)` | Perform an attack |
| `get_current_battle()` | Get current battle state |
| `finish_battle()` | Finish the current battle |
| `pick_up_item(item_id)` | Pick up a dropped item |
| `get_monster_info(name)` | Get monster details |
| `get_quests_journal()` | Get quest journal |
| `get_battles_history()` | Get battle history |
| `get_friends()` | Get friends list |
| `suggest_friends(username)` | Search for users |
| `send_friend_request(user_id)` | Send a friend request |
| `cancel_friend_request(user_id)` | Cancel a friend request |
| `get_chat_channels()` | Get available chat channels |
| `get_chat_history()` | Get chat history |
| `send_message(channel_id, text)` | Send a chat message |
