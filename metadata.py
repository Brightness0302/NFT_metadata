# Step 1
import pickle
import json
import random

name = ""
fee = "10%"
description = "Crazy Rich Rabbit NFT @Montage Collection"
count = 110

# Step 2
for i in range(count):
	print(i)
	filename = "metadata/" + str(i) + ".json";

	#metadata
	metadata = {'name': name, 'Royal fee': fee, 'description': description, 'attributes': []}
	metadata["attributes"].append({"trait_type": "PASSIVE SKILL 1", "value": "DOUBLE SHOT"})
	percent = random.randint(0,100)
	if percent < 20:
		metadata["attributes"].append({"trait_type": "PASSIVE SKILL 2", "value": "DRONE PILOT CERTIFICATE"})
	metadata["attributes"].append({"trait_type": "LUCK", "value": random.randint(10,30)})
	metadata["attributes"].append({"trait_type": "LIKE", "value": ["CARROT", "RICE CAKE", "RADISH", "CUCUMBER", "BORCCOLI"]})
	metadata["attributes"].append({"trait_type": "COME FROM", "value": "MOON"})
	metadata["attributes"].append({"trait_type": "SPECIAL FEATURE", "value": "MONTAGE"})
	metadata["attributes"].append({"trait_type": "background", "value": "silver"})
	metadata["attributes"].append({"trait_type": "background", "value": "silver"})
	metadata["attributes"].append({"trait_type": "background", "value": "silver"})

	# Serializing json
	json_object = json.dumps(metadata, indent=4)

	with open(filename, 'w') as file:
	 
	  # Step 3
	  file.write(json_object)