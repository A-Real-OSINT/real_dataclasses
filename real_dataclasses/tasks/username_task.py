from task import Task

class UsernameTask(Task):
    """
    This class represents a username task in the system and will be used to manage username tasks.
    """
    
    def __init__(self, username: str) -> str:
        """
        Creates an instance of UsernameTask.
        :param task_id: The unique identifier for the task.
        :type task_id: str
        :param username: The username associated with the task.
        :type username: str
        :return: The task_id of the newly created task.
        :rtype: str
        """
        
        self.username = username
        return super().__init__("username")
        
    
    def __str__(self):
        """
        Returns a string representation of the UsernameTask instance.
        :return: A string representation of the UsernameTask instance.
        :rtype: str
        """
        return f"UsernameTask(task_id={self.task_id}, username={self.username})"