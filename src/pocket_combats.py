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

    def _post(self, endpoint: str, data: dict = None) -> dict:
        return self.session.post(
            f"{self.api}{endpoint}", data=data).json()

    def _get(self, endpoint: str) -> dict:
        return self.session.get(
            f"{self.api}{endpoint}").json()

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
        return self._post("/api/register", data)

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
            f"{self.api}/auth/register", json=data).json()

    def login_with_token(self, auth_token: str) -> str:
        self.auth_token = auth_token
        self.session.headers["Authorization"] = f"Bearer {self.auth_token}"
        return self.auth_token

    def get_chat_history(self) -> dict:
        return self._post("/api/chat/history")

    def get_chat_channels(self) -> dict:
        return self._get("/api/chat/channels")

    def get_current_player(self) -> dict:
        return self._get("/api/player/self")

    def get_location_info(self) -> dict:
        return self._get("/api/location")

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
        return self._post("/api/chat/send", data)

    def get_equipment(self) -> dict:
        return self._get("/api/equipment")

    def get_skills(self) -> dict:
        return self._get("/api/skills")

    def get_backpack(self) -> dict:
        return self._get("/api/backpack")

    def route_location(self, route_id: int) -> dict:
        data = {
            "routeId": route_id
        }
        return self._post("/api/location/select-route", data)

    def get_quests_journal(self) -> dict:
        return self._get("/api/quest/journal")

    def get_friends(self) -> dict:
        return self._get("/api/friends")

    def suggest_friends(self, username: str) -> dict:
        data = {
            "u": username
        }
        return self._post("/api/friends/suggest", data)

    def send_friend_request(self, user_id: int) -> dict:
        data = {
            "id": user_id
        }
        return self._post("/api/friends/invite", data)

    def cancel_friend_request(self, user_id: int) -> dict:
        data = {
            "id": user_id
        }
        return self._post("/api/friends/invite/cancel", data)

    def get_battles_history(self) -> dict:
        return self._get("/api/battle/history")

    def start_battle(
            self,
            battle_id: str,
            hp: int,
            position: int) -> dict:
        data = {
            "id": battle_id,
            "hp": hp,
            "pos": position
        }
        return self._post("/api/location/attack", data)

    def attack_monster(
            self,
            action_id: int,
            target_id: int = 0) -> dict:
        data = {
            "actionId": action_id,
            "targetId": target_id
        }
        return self._post("/api/battle/current", data)

    def get_current_battle(self) -> dict:
        return self._get("/api/battle/current")

    def finish_battle(self) -> dict:
        return self._post("/api/battle/finish")

    def pick_up_item(self, item_id: int) -> dict:
        data = {
            "itemId": item_id
        }
        return self._post("/api/location/pick-up", data)

    def get_monster_info(self, name: str) -> dict:
        return self._get(f"/api/location/monster/{name}")
