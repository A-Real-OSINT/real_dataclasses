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
        self.task_id = str(uuid4())
        self.created_at = datetime.now()    
        self.status = "created"
        self.result = None
        self.blob_id = None
        self.result_id = None
        self.task_type = task_type
        
        return self.task_id
    
    def _json_str(self) -> str:
        """
        Converts the task to a JSON string.
        :return: JSON string representation of the task.
        :rtype: str
        """
        
        raise NotImplementedError("This method should be implemented in a subclass.")
    
    def _jsonify(self) -> dict:
        """
        Converts the task to a JSON-compatible dictionary.
        :return: Dictionary representation of the task.
        :rtype: dict
        """
        
        return {
            "task_id": self.task_id,
            "created_at": self.created_at.isoformat(),
            "status": self.status,
            "result": self.result,
            "blob_id": self.blob_id,
            "result_id": self.result_id,
            "task_type": self.task_type
        }