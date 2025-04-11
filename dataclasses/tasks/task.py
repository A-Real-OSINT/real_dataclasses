from datetime import datetime
from uuid import uuid4

class Task:
    """
    This class represents a task in the system and will be used to manage tasks.
    """
    
    def __init__(self, task_type: str) -> str:
        """
        creates an instance of Task.
        :param task_type: The type of the task.
        :type task_type: str
        :return: task_id
        :rtype: str
        """
        self.task_id = uuid4()
        self.created_at = datetime.now()    
        self.status = "created"
        self.result = None
        self.blob_id = None
        self.result_id = None
        self.task_type = task_type
        
        return self.task_id
        