# Step 1
import pickle
import json
import random

name = "Rich Rabbit NFT #"
fee = "10%"
description = "Crazy Rich Rabbit NFT @Montage Collection"
image = "https://ipfs.io/ipfs/QmUneJUsj9A4Dt8JfrrR28BAnoDNTGqa2HG6BfXGezKfcZ/"
count = 111

like = ["CARROT", "RICE CAKE", "RADISH", "CUCUMBER", "BORCCOLI"]

# Step 2
for i in range(count):
	print(i)
	filename = "metadata/" + str(i) + ".json";

	#metadata
	metadata = {'name': name + str(i), 'description': description, 'image': image + str(i) + '.jpg', 'attributes': []}
	metadata["attributes"].append({"trait_type": "PASSIVE SKILL 1", "value": "DOUBLE SHOT"})
	percent = random.randint(0,100)
	if percent < 20:
		metadata["attributes"].append({"trait_type": "PASSIVE SKILL 2", "value": "DRONE PILOT CERTIFICATE"})
	metadata["attributes"].append({"trait_type": "LUCK", "value": random.randint(10,30)})
	metadata["attributes"].append({"trait_type": "LIKE", "value": like[random.randint(0,4)]})
	metadata["attributes"].append({"trait_type": "COME FROM", "value": "MOON"})
	metadata["attributes"].append({"trait_type": "SPECIAL FEATURE", "value": "MONTAGE"})

	# Serializing json
	json_object = json.dumps(metadata, indent=4)

	with open(filename, 'w') as file:
	 
	  # Step 3
	  file.write(json_object)