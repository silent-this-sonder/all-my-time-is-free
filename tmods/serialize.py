"""Stores the data for the tasks & projects.
Creates directories for projects and uses JSON for the tasks."""

import json
import os

# save the path to the tasks directory
TASKS_DIR = os.path.join(os.getcwd(), "tasks")


def save_task(task: dict, project, file):
    """Write the task to the .json file."""
    
    file = os.path.join(project, file)
    with open(file, "w") as f:
        json_data = json.dump(task, f)

    return json_data


def create_project(title: str, desc=""):
    """Create a project (a directory container project info and related tasks)
        title - str, name of the project
        desc - str, detailed explanation of the project
        Returns a value if a problem occurs."""

    # create the directory
    project_dir = os.path.join(TASKS_DIR, title)
    # check that project of the same name does not exist yet
    if os.path.isdir(project_dir) == False:
        os.mkdir(project_dir)
    else:
        return "Already exists."

    # create the JSON to store project metadata
    project_f = os.path.join(project_dir, "project_info.json")
    project_meta = {
        "desc": desc,
    }

    with open(project_f, "w") as f:
        json.dump(project_meta, f)