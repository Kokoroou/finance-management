import os

import yaml


def get_intents():
    all_intents = {}
    for file_name in os.listdir("./custom_data/intent"):
        # Remove prefix and suffix of file name
        intent = file_name[len("intent_"):-len(".yml")]

        all_intents[intent] = {}

        with open("./custom_data/intent/" + file_name, "r") as f:
            data = yaml.safe_load(f)

            # Number of detail intents in a retrieval intent
            all_intents[intent]["count"] = len(data)

    return all_intents
