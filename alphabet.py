import random

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_random_letter():
	return alphabet[random.randint(0, len(alphabet)-1)]