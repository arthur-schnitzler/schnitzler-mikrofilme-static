def get_id_and_title(metadata_title: str) -> tuple:
    """takes a metadata_title and returns meaningful ID and a better title

    Args:
        metadata_title (str): the metadata_title e.g. B_20_Zwischenspiel

    Returns:
        tuple: e.g. ("B_20", "Zwischenspiel" )
    """
    title = " ".join(metadata_title.split()[1:])
    doc_id = metadata_title.split()[0]
    return doc_id, title
