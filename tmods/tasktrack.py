import datetime

def create_taskdict(title: str, duedate: datetime.date, desc="", project=""):
    """Create a task in the form of a dictionary.
        title - str, short name for the task
        duedate - datetime.date instance that tells when it is due
        desc - str, longer description of the task
        project - str, project/school subject the task is for"""
    
    task = {
        "title": title,
        "duedate": str(duedate),
        "desc": desc,
        "project": project
    }

    return task

t = create_taskdict("Hello World", datetime.date.today())