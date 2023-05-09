import re

inputFile = "CompVersion.txt"
filtertext = "rba.CUBAS."

regex_onlynums = r"(AR\d\S\S?[.|_]+[\d]+[.|_]+[\d]+[.|_]+\d+)"  # 162/211 matches
regex_numsandwords = r"(AR\d\S\S?[.|_]+\w+[.|_]\w+[.|_]\w+)"  # 188/211 matches


def read_file(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    data_structure = {line: { "version": ""} for line in lines}
    # print(data_structure)
    return data_structure



def filter_cubas_components(data_structure):
    filtered_dict = {
        k: {"version": ""} for k in data_structure if (k.startswith(filtertext) & ("_self" not in k))
    }
    #print(filtered_dict)
    return filtered_dict

def get_version_using_regex1(filtered_dict):

    matching_comps_count = 0
    missing_comps_count = 0

    for key in filtered_dict.keys():
        match = re.search(regex_onlynums, key)
        if match:
            filtered_dict[key]["version"] = match.group(1)
            matching_comps_count += 1

        else:
            missing_comps_count += 1

    print("matching_comps_count = " + str(matching_comps_count))
    print("missing_comps_count = " + str(missing_comps_count))

    return filtered_dict


def get_version_using_regex2(filtered_dict):

    matching_comps_count = 0
    missing_comps_count = 0

    for key in filtered_dict.keys():
        match = re.search(regex_numsandwords, key)
        if match:
            filtered_dict[key]["version"] = match.group(1)
            matching_comps_count += 1

        else:
            missing_comps_count += 1

    print("matching_comps_count = " + str(matching_comps_count))
    print("missing_comps_count = " + str(missing_comps_count))

    return filtered_dict


def print_dict(normalized_dict):
    for key, value in normalized_dict.items():
        print(f"Component: {key}")
        print(f"Version: {value['version']}")
        # print(f"{value['version']}")
        print()


if __name__ == "__main__":

    data_structure = read_file(inputFile)
    filtered_dict = filter_cubas_components(data_structure)
    versioned_components = get_version_using_regex2(filtered_dict)  # two method variations: 1 and 2

    # pprint.pprint(normalized_dict)
    print_dict(versioned_components)

