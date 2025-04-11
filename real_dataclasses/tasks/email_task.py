from task import Task
from typing import override
import json


class EmailTask(Task):
    """
    This class represents an email adress task in the system and will be used to manage email tasks.
    """
    
    def __init__(self, e_mail: str) -> str:
        """
        Creates an instance of EmailTask.
        :param task_id: The unique identifier for the task.
        :type task_id: str
        :param e_mail: The email address associated with the task.
        :type e_mail: str
        :return: The task_id of the newly created task.
        :rtype: str
        """
        
        self.e_mail = e_mail
        return super().__init__("email")

    
    def __str__(self):
        """
        Returns a string representation of the EmailTask instance.
        :return: A string representation of the EmailTask instance.
        :rtype: str
        """

        return f"EmailTask(task_id={self.task_id}, e_mail={self.e_mail})"


    @override
    def _json_str(self) -> str:
        """
        Converts the EmailTask to a JSON string.
        :return: JSON string representation of the EmailTask.
        :rtype: str
        """

        task_as_dict = super()._jsonify()
        task_as_dict["e_mail"] = self.e_mail
        return json.dumps(task_as_dict)