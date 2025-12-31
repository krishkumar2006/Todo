# Data Model: Todo CLI Application

## Task Entity

### Attributes
- **id**: `int` - Unique auto-incrementing identifier (starting from 1)
- **title**: `str` - Task title (required, non-empty)
- **description**: `str | None` - Task description (optional, can be None)
- **completed**: `bool` - Completion status (default: False)

### Validation Rules
- ID must be a positive integer
- Title must be a non-empty string
- Description can be None or a string
- Completed status must be a boolean value

### State Transitions
- A Task can transition from incomplete (completed=False) to complete (completed=True)
- A Task can transition from complete (completed=True) back to incomplete (completed=False)

## Task Service Data Flow

### Add Task
1. Input: title (str), description (str, optional)
2. Process: Create new Task with auto-incremented ID, set completed=False
3. Output: Task object with all attributes populated

### Update Task
1. Input: ID (int), new_title (str, optional), new_description (str, optional)
2. Process: Find existing Task by ID, update specified attributes
3. Output: Updated Task object

### Delete Task
1. Input: ID (int)
2. Process: Find and remove Task from storage by ID
3. Output: Boolean indicating success/failure

### Mark Complete/Incomplete
1. Input: ID (int), completed_status (bool)
2. Process: Find existing Task by ID, update completed attribute
3. Output: Updated Task object

### List Tasks
1. Input: None
2. Process: Retrieve all Tasks from storage
3. Output: List of Task objects