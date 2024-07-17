"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    compare_tuple = tuple(azara_record[1])
    return compare_tuple == rui_record[1]


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """

    # result = []
    # for item in combined_record_group:
    #     # Unpack the tuple, ignoring the second element
    #     name, _, location, coordinates, color = item
    #     # Create a new tuple with the desired format
    #     new_item = (name, location, coordinates, color)
    #     # Convert the tuple to a string and append it to the result list
    #     result.append(str(new_item))
    # # Join all strings in the result list with newline characters
    # return '\n'.join(result) + '\n'
    result = []
    for record in combined_record_group:        
        multi_string = f"('{record[0]}', '{record[2]}', {record[3]}, '{record[4]}')"
        result.append(multi_string)
    return '\n'.join(result) + '\n'


print(
    clean_up(
        (
            ("Scrimshawed Whale Tooth", "2A", "Deserted Docks", ("2", "A"), "Blue"),
            ("Brass Spyglass", "4B", "Abandoned Lighthouse", ("4", "B"), "Blue"),
            ("Robot Parrot", "1C", "Seaside Cottages", ("1", "C"), "Blue"),
        )
    )
)
