import pymongo

class DB:
	
	def __init__(self):
		self.client = pymongo.MongoClient()
		self.db = self.client.player_database
		self.players = self.db.players

	def insert(self, player_obj):
		player_id = self.players.insert(player_obj)
		return player_id

	def list_all(self):
		return self.db.collection_names()

	def get_player_by_name(self, name):
		return self.players.find_one({"name": name})

	def get_player_by_id(self, summoner_id):
		return self.players.find_one({"id": summoner_id})