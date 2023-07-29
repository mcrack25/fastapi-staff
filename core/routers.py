from tasks.routes import router as router_tasks
from accounts.routes import router as router_users

all_routers = [
    router_tasks,
    router_users,
]
