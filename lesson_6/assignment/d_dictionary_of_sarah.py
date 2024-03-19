# Complex data structure

sarah_professional_profile = {
    "name": "Sarah Brown",
    "occupation": "Software Engineer",
    "preferred OS": "Windows",
    "languages": ["python", "javascript", "HTML", "CSS", "C sharp", "PHP"],
    "technologies": {
        "python frameworks": ["Django"],
        "javascript libraries": ["jquery", "React JS", "AJAX"],
        "react frameworks" : ["Next JS", "Gatsby", "CRA"],
        "javascript environments": ["Node.js"],
        "infrastructure": ["AWS"]
	},
    "CLG projects": {
        "School of Code": { 
            "infrastructure": "AWS",
            "front end": ("React JS", "CRA"),
            "back end": ("Node JS", "Serverless"),
            "CMS": "static"
		},
        "Internship Platform": { 
            "infrastructure": "AWS",
            "front end": ("React JS", "Next JS"),
            "back end": ("Node JS", "Serverless"),
            "CMS": "Contentful"
		}
	}
}

for key, value in sarah_professional_profile.items():
    if type(value) == str:
        print(f"My {key} is {value}.")
    elif type(value) == list:
        print(f"My {key} are {', '.join(value)}.")
    elif type(value) == dict:
        print(f"My {key}:")
        for sub_key, sub_value in value.items():
            if type(sub_value) in [list, tuple]:
                formatted_values = ', '.join(sub_value)
                print(f"  - {sub_key}: {formatted_values}")
            elif type(sub_value) == dict:
                print(f"  - {sub_key}:")
                for inner_key, inner_value in sub_value.items():
                    if type(inner_value) in [list, tuple]:
                        inner_formatted_values = ', '.join(inner_value)
                        print(f"    - {inner_key}: {inner_formatted_values}")
                    else:
                        print(f"    - {inner_key}: {inner_value}")
            else:
                print(f"  - {sub_key}: {sub_value}")