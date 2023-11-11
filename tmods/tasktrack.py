import datetime


def create_taskdict(title: str, creation: str, duedate: str, desc="", project=""):
    """Create a task in the form of a dictionary.
        title - str, short name for the task
        duedate - MM-DD-YYYY format that tells when it is due
        desc - str, longer description of the task
        project - str, project/school subject the task is for"""
    
    task = {
        "title": title,
        "creation": creation,
        "duedate": duedate,
        "desc": desc,
        "project": project
    }

    return task