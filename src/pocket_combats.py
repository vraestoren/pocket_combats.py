from requests import Session

class PocketCombats:
    def __init__(self) -> None:
        self.api = "https://game.pocketcombats.com"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "okhttp/3.10.0",
            "Content-Type": "application/json"
        }
        self.auth_token = None

    def register(
            self, 
            google_id_token: str, 
            username: str, 
            gender: str = "MALE", 
            sdk_version: int = 238, 
            vendor: str = "samsung SM-N976N 7.1.2") -> dict:
        data = {
            "gender": gender,
            "id_token": google_id_token,
            "sdk_version": sdk_version,
            "username": username,
            "vendor": vendor
        }
        return self.session.post(
            f"{self.api}/api/register", data=data).json()

    def register_new_character(
            self,
            google_id_token: str,
            username: str,
            gender: str = "MALE",
            sdk_version: int = 238,
            vendor: str = "samsung SM-G9880 7.1.2") -> dict:
        data = {
            "gender": gender,
            "id_token": google_id_token,
            "sdk_version": sdk_version,
            "username": username,
            "vendor": vendor
        }
        return self.session.post(
            f"{self.api}/auth/register",  json=data).json()

    def login_with_token(self, auth_token: str) -> str:
        self.auth_token = auth_token
        self.session.headers["Authorization"] = f"Bearer {self.auth_token}"
        return self.auth_token

    def get_chat_history(self) -> dict:
        return self.session.post(
         f"{self.api}/api/chat/history").json()

    def get_chat_channels(self) -> dict:
        return self.session.get(f"{self.api}/api/chat/channels").json()

    def get_current_player(self) -> dict:
        return self.session.get(f"{self.api}/api/player/self").json()

    def get_location_info(self) -> dict:
        return self.session.get(f"{self.api}/api/location").json()

    def send_message(
            self,
            channel_id: int, 
            text: str, 
            last_received_id: int = 0) -> dict:
        data = {
            "channel_id": channel_id,
            "last_received_id": last_received_id,
            "text": text
        }
        return self.session.post(
            f"{self.api}/api/chat/send", data=data).json()

    def get_equipment(self) -> dict:
        return self.session.get(
            f"{self.api}/api/equipment").json()

    def get_skills(self) -> dict:
        return self.session.get(
            f"{self.api}/api/skills").json()

    def get_backpack(self) -> dict:
        return self.session.get(
            f"{self.api}/api/backpack").json()

    def route_location(self, route_id: int) -> dict:
        data = {
            "routeId": route_id
        }
        return self.session.post(
            f"{self.api}/api/location/select-route", 
            data=data).json()

    def get_quests_journal(self) -> dict:
        return self.session.get(
            f"{self.api}/api/quest/journal").json()

    def get_friends(self) -> dict:
        return self.session.get(
            f"{self.api}/api/friends").json()

    def suggest_friends(self, username: str) -> dict:
        data = {
            "u": username
        }
        return self.session.post(
            f"{self.api}/api/friends/suggest",
            data=data).json()

    def send_friend_request(self, user_id: int) -> dict:
        data = {
            "id": user_id
        }
        return self.session.post(
            f"{self.api}/api/friends/invite",
            data=data).json()

    def cancel_friend_request(self, user_id: int) -> dict:
        data = {
            "id": user_id
        }
        return self.session.post(
            f"{self.api}/api/friends/invite/cancel",
            data=data).json()

    def get_battles_history(self) -> dict:
        return self.session.get(
            f"{self.api}/api/battle/history").json()

    def start_battle(
            self,
            id: str,
            hp: int,
            position: int) -> dict:
        data = {
            "id": id,
            "hp": hp,
            "pos": position
        }
        return self.session.post(
            f"{self.api}/api/location/attack",  data=data).json()

    def attack_monster(
            self,
            action_id: int,
            target_id: int = 0) -> dict:
        data = {
            "actionId": action_id,
            "targetId": target_id
        }
        return self.session.post(
            f"{self.api}/api/battle/current",  data=data).json()

    def get_current_battle(self) -> dict:
        return self.session.get(
            f"{self.api}/api/battle/current").json()

    def finish_battle(self) -> dict:
        return self.session.post(
            f"{self.api}/api/battle/finish").json()

    def pick_up_item(self, item_id: int) -> dict:
        data = {
            "itemId": item_id
        }
        return self.session.post(
            f"{self.api}/api/location/pick-up", 
            data=data).json()

    def get_monster_info(self, name: str) -> dict:
        return self.session.get(
            f"{self.api}/api/location/monster/{name}").json()
